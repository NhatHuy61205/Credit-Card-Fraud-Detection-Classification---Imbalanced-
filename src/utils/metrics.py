import numpy as np
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    brier_score_loss)
from .config import COST_FP as FP, COST_FN as FN, SEED
from .thresholds import thr_min_cost

np.random.seed(SEED)

def evaluate(y_true, y_score, thr=0.5):
    """Hàm tính các chỉ số đánh giá mô hình dựa trên ngưỡng threshold."""
    y_pred = (y_score >= thr).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0,1]).ravel()
    
    return dict(
        threshold=float(thr),
        precision=precision_score(y_true, y_pred, zero_division=0),
        recall=recall_score(y_true, y_pred),
        f1=f1_score(y_true, y_pred, zero_division=0),
        roc_auc=roc_auc_score(y_true, y_score),
        auprc=average_precision_score(y_true, y_score),
        brier=brier_score_loss(y_true, y_score),
        tp=int(tp), fp=int(fp), fn=int(fn), tn=int(tn)
    )
    
    
def realized_cost(y_true, y_score, thr, COST_FP = FP, COST_FN = FN):
    """Hàm tính chi phí thực tế dựa trên ngưỡng threshold và chi phí của FP, FN."""
    yhat = (y_score >= thr).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, yhat, labels=[0,1]).ravel()
    return fp*COST_FP + fn*COST_FN


def expected_calibration_error(y_true, y_prob, n_bins=10):
    """Đo mức chênh lệch giữa xác suất dự đoán và xác suất thực tế."""
    bins = np.linspace(0, 1, n_bins + 1)
    idx = np.digitize(y_prob, bins) - 1
    ece = 0.0
    for b in range(n_bins):
        mask = idx == b
        if not np.any(mask):
            continue
        conf = y_prob[mask].mean()
        acc = y_true[mask].mean()
        ece += np.abs(conf - acc) * mask.mean()
    return ece

rng = np.random.default_rng(SEED)
def bootstrap_ci(y_true, y_score, metric_func, n_bootstraps=300, alpha=0.05):
    """Hàm này dùng bootstrap để tính confidence interval (CI) cho một metric (ví dụ: AUC, F1, ECE…).
    Nghĩa là: thay vì chỉ có 1 giá trị metric, ta ước lượng khoảng mà giá trị thật có thể nằm trong đó.
    Nếu metric của mô hình nằm ngoài khoảng này, ta có thể nói rằng mô hình có sự khác biệt đáng kể so với baseline."""
    n = len(y_true)
    boot_metrics = []
    for _ in range(n_bootstraps): 
        idx = rng.integers(0, n, size=n)
        boot_metrics.append(metric_func(y_true[idx], y_score[idx]))
    lower = np.quantile(boot_metrics,  alpha / 2)
    upper = np.quantile(boot_metrics, 1 - alpha / 2)
    return float(lower), float(upper)

def log_eval(y_true, y_score):
    rs_eval = evaluate(y_true, y_score)
    rs_best_thr, rs_best_cost = thr_min_cost(y_true, y_score)

    return dict(
        threshold = rs_best_thr,
        Cost = rs_best_cost,
        ROC_AUC = rs_eval["roc_auc"],
        PR_AUC = rs_eval["auprc"]
    )
    

def adaptive_ece(y_true, y_prob, n_bins=10):
    """Hàm tính ECE theo cách adaptive, tức là chia dữ liệu 
    thành các bin sao cho mỗi bin có số lượng mẫu xấp xỉ nhau, thay vì chia theo khoảng cố định."""
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)

    sort_idx = np.argsort(y_prob)
    y_true = y_true[sort_idx]
    y_prob = y_prob[sort_idx]

    bins = np.array_split(np.arange(len(y_prob)), n_bins)

    ece = 0.0
    total = len(y_prob)

    for b in bins:
        if len(b) == 0:
            continue

        conf = np.mean(y_prob[b])
        acc = np.mean(y_true[b])

        ece += (len(b) / total) * abs(acc - conf)

    return ece

def debiased_ece(y_true, y_prob, n_bins=10):
    """Hàm tính ECE đã được điều chỉnh để giảm bias, 
    bằng cách trừ đi một ước lượng về độ lệch ngẫu nhiên do số lượng mẫu trong mỗi bin."""
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)

    bins = np.linspace(0, 1, n_bins + 1)
    bin_ids = np.digitize(y_prob, bins) - 1

    ece = 0.0
    total = len(y_prob)

    for i in range(n_bins):
        idx = bin_ids == i
        n = np.sum(idx)

        if n == 0:
            continue

        conf = np.mean(y_prob[idx])
        acc = np.mean(y_true[idx])

        var = acc * (1 - acc) / n

        ece += (n / total) * (abs(acc - conf) - var)

    return max(ece, 0.0)  
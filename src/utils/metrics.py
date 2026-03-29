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
def bootstrap_ci(metric_fn, y_true, y_score, B=300, alpha=0.05):
    n = len(y_true)
    vals = []
    for _ in range(B):
        idx = rng.integers(0, n, size=n)
        vals.append(metric_fn(y_true[idx], y_score[idx]))
    lo = np.quantile(vals, alpha/2)
    hi = np.quantile(vals, 1 - alpha/2)
    return float(lo), float(hi)

def log_eval(y_true, y_score, thr = None):
    if thr == None:
        rs_eval = evaluate(y_true, y_score)
        rs_best_thr, rs_best_cost = thr_min_cost(y_true, y_score)
        rs_ece_bias = debiased_ece(y_true, y_score)
        rs_ece_adap = adaptive_ece(y_true, y_score)
        return dict(
            threshold = rs_best_thr,
            Cost = rs_best_cost,
            ROC_AUC = rs_eval["roc_auc"],
            PR_AUC = rs_eval["auprc"],
            debiased_ece = rs_ece_bias,
            adaptive_ece = rs_ece_adap,
            Brier = rs_eval["brier"]
        )
    else:
        rs_eval = evaluate(y_true, y_score, thr)
        rs_cost = realized_cost(y_true, y_score, thr)
        rs_ece_bias = debiased_ece(y_true, y_score)
        rs_ece_adap = adaptive_ece(y_true, y_score)
        return dict(
            threshold = thr,
            Cost = rs_cost,
            Precision = rs_eval["precision"],
            Recall = rs_eval["recall"],
            F1 = rs_eval["f1"],
            ROC_AUC = rs_eval["roc_auc"],
            PR_AUC = rs_eval["auprc"],
            debiased_ece = rs_ece_bias,
            adaptive_ece = rs_ece_adap,
            Brier = rs_eval["brier"]
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

def summarise_model(name, y_true, y_prob, thr_p90, thr_cost):
    ap = average_precision_score(y_true, y_prob)
    roc = roc_auc_score(y_true, y_prob)
    brier = brier_score_loss(y_true, y_prob)
    ece = expected_calibration_error(y_true.values, y_prob, n_bins=15)
    cost_p90 = realized_cost(y_true, y_prob, thr_p90, FP, FN)
    cost_min = realized_cost(y_true, y_prob, thr_cost, FP, FN)
    ap_lo, ap_hi = bootstrap_ci(average_precision_score, y_true.values, y_prob)
    return {
        "Model": name, "AP(Test)": ap, "AP 95% CI": f"[{ap_lo:.3f}, {ap_hi:.3f}]",
        "ROC-AUC(Test)": roc, "Brier(Test)": brier, "ECE(15)": ece,
        "Thr@P90(val)": float(thr_p90), "Thr@MinCost(val)": float(thr_cost),
        "Cost@Test@P90": cost_p90, "Cost@Test@MinCost": cost_min,
    }
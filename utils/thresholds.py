import numpy as np
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix
from .config import COST_FP as FP, COST_FN as FN

def thr_for_precision(y_true, y_scores, target_prec=0.9):
    """Hàm tính ngưỡng threshold để đạt được độ chính xác (precision) mong muốn."""
    ps, rs, thrs = precision_recall_curve(y_true, y_scores)

    hits = np.where(ps[:-1] >= target_prec)[0]
    idx = hits[0] if hits.size else np.argmax(0.5*ps[:-1] + 0.5*rs[:-1])

    return float(thrs[idx]), float(ps[idx]), float(rs[idx])


def thr_min_cost(y_true, y_scores, cost_fp=FP, cost_fn=FN, grid = 1001):
    """Hàm tính ngưỡng threshold để đạt được chi phí thấp nhất."""
    best_cost, best_thr = float('inf'), 0.5
    for thr in np.linspace(0,1,grid):
        yhat = (y_scores >= thr).astype(int)
        tn, fp, fn, tp = confusion_matrix(y_true, yhat, labels=[0,1]).ravel()
        cost = fp*cost_fp + fn*cost_fn
        if cost < best_cost:
            best_cost, best_thr = float(cost), float(thr)
    return best_thr, best_cost


sweep_thresholds
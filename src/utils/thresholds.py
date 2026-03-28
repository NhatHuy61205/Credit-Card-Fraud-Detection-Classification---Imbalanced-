import numpy as np
from sklearn.metrics import precision_recall_curve,confusion_matrix,precision_score, recall_score, f1_score
import pandas as pd

from .config import COST_FP as FP, COST_FN as FN

def thr_for_precision(y_true, y_scores, target_prec=0.9):
    """Hàm tính ngưỡng threshold để đạt được độ chính xác (precision) mong muốn."""
    ps, rs, thrs = precision_recall_curve(y_true, y_scores)

    hits = np.where(ps[:-1] >= target_prec)[0]
    idx = hits[0] if hits.size else np.argmax(0.5*ps[:-1] + 0.5*rs[:-1])

    return dict(threshold=float(thrs[idx]), precision=float(ps[idx]), recall=float(rs[idx]))


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


def sweep_thresholds(y_true, y_prob, costs=(FP, FN)):
    ths = np.linspace(0, 1, 101)
    rows = []
    for t in ths:
        yhat = (y_prob >= t).astype(int)
        tn, fp, fn, tp = confusion_matrix(y_true, yhat, labels=[0,1]).ravel()
        prec = precision_score(y_true, yhat, zero_division=0)
        rec  = recall_score(y_true, yhat)
        f1   = f1_score(y_true, yhat, zero_division=0)
        cost = fp*costs[0] + fn*costs[1]
        rows.append([t, prec, rec, f1, tp, fp, fn, tn, cost])
    return pd.DataFrame(rows, columns=["thr","precision","recall","f1","tp","fp","fn","tn","cost"])

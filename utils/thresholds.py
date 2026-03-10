import numpy as np
from sklearn.metrics import precision_recall_curve

def thr_for_precision(y_true, y_scores, target_prec=0.9):
    """Hàm tính ngưỡng threshold để đạt được độ chính xác (precision) mong muốn."""
    ps, rs, thrs = precision_recall_curve(y_true, y_scores)

    hits = np.where(ps[:-1] >= target_prec)[0]
    idx = hits[0] if hits.size else np.argmax(0.5*ps[:-1] + 0.5*rs[:-1])

    return float(thrs[idx]), float(ps[idx]), float(rs[idx])


thr_min_cost
sweep_thresholds
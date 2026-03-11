from sklearn.metrics import brier_score_loss, precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, average_precision_score
from sklearn.calibration import calibration_curve
def plot_pr_roc(y_true, y_score, title):
    """Hàm vẽ Precision-Recall và ROC với baseline cho PR."""

    # ===== Precision-Recall Curve =====
    precision, recall, _ = precision_recall_curve(y_true, y_score)
    ap = average_precision_score(y_true, y_score)
    plt.figure(figsize=(6,5))
    plt.plot(recall, precision, label=f'Model (AP={ap:.2f})')
    plt.axhline(y_true.mean(), linestyle='--', label=f'Baseline={y_true.mean():.2f}')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f'Precision-Recall Curve - {title}')
    plt.legend()
    plt.show()

    # ===== ROC Curve =====
    fpr, tpr, _ = roc_curve(y_true, y_score)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(6,5))
    plt.plot(fpr, tpr, label=f'Model (AUC={roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve - {title}')
    plt.legend()
    plt.show()
    

def reliability_plot(y_true, y_score, title, bins=10):
    """Hàm vẽ biểu đồ so sánh xác suất giá trị dự đoán với giá trị thực tế."""
    prob_true, prod_pred = calibration_curve(y_true, y_score, n_bins=bins, strategy='quantile')
    plt.figure(figsize=(6,5))
    plt.plot(prod_pred, prob_true, marker='o', label='Model')
    plt.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Perfectly Calibrated')
    plt.xlabel('Predicted Probability')
    plt.ylabel('Empirical probability')
    plt.title(title + f" — Brier={brier_score_loss(y_true, y_score):.4f}")
    plt.legend()
    plt.show()

def plot_alerts_and_savings(alerts, savings, title):
    
# 💳 CREDIT CARD FRAUD DETECTION

### Phát hiện gian lận thẻ tín dụng với dữ liệu mất cân bằng mạnh

------------------------------------------------------------------------

## 📌 Tổng quan dự án

Gian lận thẻ tín dụng gây thiệt hại lớn cho ngân hàng và khách hàng.\
Tuy nhiên, giao dịch gian lận chỉ chiếm khoảng **0.1--0.2%** tổng số
giao dịch.

Đây là một bài toán:

**Phân loại nhị phân với dữ liệu mất cân bằng nghiêm trọng (Highly
Imbalanced Classification).**

### 🎯 Mục tiêu:

-   Phát hiện tối đa giao dịch gian lận (**ưu tiên Recall cao**)
-   Hạn chế bỏ sót fraud
-   Kiểm soát tỷ lệ báo động sai
-   Sử dụng metric phù hợp với dữ liệu imbalance (AUC-PR)

Hệ thống phân loại: - `1` -- Fraud\
- `0` -- Legitimate

------------------------------------------------------------------------

## 🧠 Phương pháp thực hiện

### 1️⃣ Đặc trưng sử dụng

-   Time
-   Amount
-   Các đặc trưng ẩn danh hóa (PCA features)

### 2️⃣ Xử lý mất cân bằng

-   SMOTE
-   Random Over-Sampling / Under-Sampling
-   Điều chỉnh class_weight
-   Threshold tuning

### 3️⃣ Đánh giá mô hình

-   Recall (ưu tiên chính)
-   Precision
-   F1-score
-   ROC-AUC
-   **AUC-PR (Primary Metric)**

AUC-PR phản ánh tốt hiệu suất trên lớp hiếm (fraud).

------------------------------------------------------------------------

## 👥 Thành viên nhóm

  MSSV         Họ tên           Vai trò
  ------------ ---------------- -------------
  2351050051   Bùi Nhật Huy     Trưởng nhóm
  2351050083   Trần Đăng Khoa   Thành viên
  2351050021   Phạm Hoàng Duy   Thành viên
  2351050136   Lê Hoàng Phúc    Thành viên

------------------------------------------------------------------------
## Công nghệ- ML: Python, sklearn, Jupyter - Frontend: ReactJS - Backend: Flask / FastAPI / Node (…) - Tracking: wandb 
## Cài đặt và chạy 
### Yêu câ ̀u- Python 3.x, Node.js (nê ́u dùng React) 
### Chạy Notebook 
jupyter notebook notebooks/project_analysis.ipynb 
### Chạy Backend 
cd api && pip install -r requirements.txt && python app.py 
### Chạy Frontend 
cd frontend && npm install && npm start 
### Truy cập- Frontend: http://localhost:3000 - API: http://localhost:5000 (hoặc port tương ứng) 
## Demo- wandb: [link] - Screenshot/video: [link hoặc mô tả] 
## Nộp bài- Báo cáo: report/report.pdf - wandb link: wandb_link.txt




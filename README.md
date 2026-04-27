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

| MSSV       | Họ tên            | Vai trò       |
|------------|------------------|--------------|
| 2351050051 | Bùi Nhật Huy     | Trưởng nhóm  |
| 2351050083 | Trần Đăng Khoa   | Thành viên   |
| 2351050021 | Phạm Hoàng Duy   | Thành viên   |
| 2351050136 | Lê Hoàng Phúc    | Thành viên   |


------------------------------------------------------------------------
# 📌 Fraud Detection System (Fullstack)

## 📖 Mô tả project

Đây là hệ thống **phát hiện gian lận giao dịch (Fraud Detection)** sử dụng Machine Learning, kết hợp giữa:

- **Backend (FastAPI)**: xử lý API, load model ML, nhận file CSV và dự đoán  
- **Frontend (Vite + JS)**: giao diện người dùng upload dữ liệu và hiển thị kết quả  
- **Notebook (EDA + Training)**: phân tích dữ liệu và huấn luyện model  

### Hệ thống cho phép:

- Upload file giao dịch (`.csv`)
- Phân tích và dự đoán gian lận
- Hiển thị các thống kê như:
  - Tổng giao dịch
  - Fraud / Non-fraud
  - Theo giờ, theo trạng thái

---

## ⚙️ Cấu trúc project
```bash
Credit-Card-Fraud-Detection-Classification
│
├── backend/
│ ├── app.py
│ ├── services/
│ ├── schema/
│ ├── model/
│ └── db/
│
├── frontend/
│ └── (Vite project)
│
├── data/
│ ├── test_1.csv
│ ├── test_2.csv
│ └── ...
│
├── notebooks/
│ ├── eda/
│ └── models/
│
└── artifacts/
└── model đã train
│
└── report/
└── báo cáo đề tài
│
└── screenshots/
└── nội dung hướng dẫn và hình ảnh demo web
│
└── weekly-report/
└── báo cáo mỗi tuần


---

## 🚀 Hướng dẫn chạy project
### Mở file sceenshots có hướng dẫn chi tiết cách chạy và video hướng dẫn cụ thể







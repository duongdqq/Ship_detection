# Các thư mục và mục đích sử dụng
* darknet.py: chạy file darknet dùng cho mục đích kiểm tra
* create_name.py: tạo tên đường dẫn của thư mục để đưa vào file train.txt, valid.txt và test.txt
* change_file_type.py: chuyển annotation của ảnh ( được gán nhãn bởi bài báo ) từ .xml sang .txt
* sample.xml: file xml mẫu
* coco.py: file được chỉnh sửa từ COCO, mục đích để lấy ảnh chứa class yêu cầu - Boat
# Kết quả và đánh giá 
---
25/2
* Dữ liệu

| Dataset                | Total         | Training set | Test set   |
| -----------------------|---------------|--------------|------------|
| Boat Types Recognition | 1362          | 1000         | 150        |
| Ship Detection         | 7000          | 1000         | 3000       |
| COCO                   | 8550          | 2000 + 4000  | 0 + 2550   |
| Project                | 19912         | 8000         | 5700       |
|                        |               | 4000 + 4000  | 3150 + 2550|
* 4000 + 4000 có nghĩa là trong 8000 ảnh của Training set chứa 4000 ảnh có tàu, 4000 ảnh không có tàu
* Kết quả

| Dataset      | detections_count | unique_truth_count | mAP   | TP    | FP    | FN    | IoU    |
| -------------|------------------|--------------------|-------|-------|-------|-------|--------|
| obj + noobj  | 11941            | 4603               | 69.15 | 2912  | 789   | 1691  | 59.66  |
| obj          | 5578             | 3802               | 87.68 | 2958  | 250   | 844   | 70.97  |
| noobj        | 5223             | 0                  | 0     | 0     | 492   | 0     | 0      |
* Nhận xét
* Tỉ lệ phát hiện thiếu (FN) = 1691/4603 = 0.37
* Tỉ lệ phát hiện sai (FP) = 492/11941 = 0.04
---
26/2
* Dữ liệu 

| Dataset                | Total         | Training set | Test set   |
| -----------------------|---------------|--------------|------------|
| Boat Types Recognition | 1362          | 1000         | 150        |
| Ship Detection         | 7000          | 1000         | 3000       |
| COCO                   | 9550          | **3000** + 4000  | 0 + 2550   |
| Project                | 17912         | **9000**         | 5700       |
|                        |               | **5000** + 4000  | 3150 + 2550|
* Kết quả

| Thresh | Dataset      | detections_count | unique_truth_count | mAP   | TP    | FP    | FN    | IoU    |
| -------| -------------|------------------|--------------------|-------|-------|-------|-------|--------| 
| 0.24   | obj + noobj  | 9277             | 4625               | 76.66 | 3262  | 629   | 1363  | 64.62  |
| 0.24   | obj          | 5021             | 3802               | 90.27 | 3139  | 193   | 663   | 73.75  |
| 0.24   | noobj        | 3194             | 22                 | 5     | 18    | 341   | 4     | 3.98   |
| 0.1    | obj + noobj  | 9277             | 4625               | 76.66 | 3236  | 1185  | 989   | 57.72  |

* Nhận xét
* Tỉ lệ phát hiện thiếu (FN) = 1363/4625 = 0.3
* Tỉ lệ phát hiện sai (FP) = 629/9277 = 0.07
---

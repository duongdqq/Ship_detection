# Các thư mục và mục đích sử dụng
* darknet.py: chạy file darknet dùng cho mục đích kiểm tra
* create_name.py: tạo tên đường dẫn của thư mục để đưa vào file train.txt, valid.txt và test.txt
* change_file_type.py: chuyển annotation của ảnh ( được gán nhãn bởi bài báo ) từ .xml sang .txt
* sample.xml: file xml mẫu
* coco.py: file được chỉnh sửa từ COCO, mục đích để lấy ảnh chứa class yêu cầu - Boat
# Quá trình hình thành đề tài
## T3 25/2/2020 
dataset
* training set 8000
* obj 1000 + 1000 + 2000
* noobj 4000 
* valid set 
* obj 3192
* noobj 2556
detects_count = 11941 
unuque_truth_count = 4603
ap = 69.15
TP 2912
FP 789
FN 1691
average IoU 59.66
---
dataset
* training set 8000
* obj 1000 + 1000 + 2000
* noobj 4000 
* valid set 
* obj 3192
detects_count = 5578
unuque_truth_count = 3802
ap = 87.68
TP 2958
FP 250
FN 844
average IoU 70.97
---
dataset
* training set 8000
* obj 1000 + 1000 + 2000
* noobj 4000 
* valid set 
* noobj 2556
detects_count = 5223 
unuque_truth_count = 0
ap = 0
TP 0
FP 492
FN 0
average IoU 0
---

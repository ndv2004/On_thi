import json
import random

# Đọc file dữ liệu (giả sử file là 'questions.json')
with open('lsd.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    options = item['options']
    # Xác định đáp án đúng
    if 'answerIndex' in item:
        correct_text = options[item['answerIndex']]
    elif 'answer' in item:
        correct_text = item['answer']
    else:
        continue

    # Xáo trộn options
    random.shuffle(options)
    # Tìm vị trí mới
    new_idx = options.index(correct_text)
    item['answerIndex'] = new_idx
    # Giữ lại answer (nội dung) để tham khảo
    item['answer'] = correct_text

# Ghi ra file mới
with open('lsd10.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Đã xáo trộn xong!")
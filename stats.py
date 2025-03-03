def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def char_count(text):
    char_cnt = {}
    for c in text:
        c = c.lower()
        if c.isalpha():
            if c in char_cnt:
                char_cnt[c] += 1
            else:
                char_cnt[c] = 1
    return char_cnt

def sorting_algo(char_cnt):
    char_list = [{"char": char, "count": count} for char, count in char_cnt.items()]
    sorted_list = sorted(char_list, reverse=True, key=lambda x: x["count"])
    return sorted_list


    
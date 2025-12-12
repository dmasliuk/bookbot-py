def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content

def count_book_words(content):
    return len(content.split())

def count_chars(content):
    content_dict = {}
    content = content.lower()
    for char in content:
      if char not in content_dict:
        content_dict[char] = 1
      else:
        content_dict[char] += 1
    return content_dict
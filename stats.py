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

def get_key(dict):
  return 

def sort_chars(chars):
  sorted_chars = []
  
  for k, v in chars.items():
    char_dict = {
    "char": k,
    "num": v
    }
    sorted_chars.append(char_dict)
  sorted_chars = sorted(sorted_chars, key = lambda x: (x["num"]),reverse = True)
  return sorted_chars
def int_func(text):
    upper = text.title()
    return upper


text = "super hero"
split_text = text.split(' ')
final_text = []
for i in split_text:
    final_text.append(int_func(i))
print(final_text)


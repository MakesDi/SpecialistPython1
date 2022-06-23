# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

import re

count = 0
no_punct = re.sub("[,|.|!|?|-]","", text)
only_words = no_punct.split()

for word in range(len(only_words)):
    if len(only_words[word]) > 7:
        count += 1
print("Число слов в тексте длиной больше 7 букв:", count)

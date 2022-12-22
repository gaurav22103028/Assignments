def char_count(str):
    all_freq = {}

    for i in str:
     if i in all_freq:
        all_freq[i] += 1
     else:
        all_freq[i] = 1
    return all_freq

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
     if word in counts:
        counts[word] += 1
     else:
        counts[word] = 1
    return counts
text = input("Enter a String: ")
if text.count(' ')>0:
    print(word_count(text))
else:
    print(char_count(text))
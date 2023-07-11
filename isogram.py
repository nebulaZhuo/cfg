
def is_isogram(word):
    word = word.lower()
    a = [0]*26
    for i in word:
        if i.isalpha()==False:
            return False
        else:
            a[ord(i) - ord('a')] += 1
    for j in a:
        if (j > 1):
            return False
    return True

# 汉函数的定义
def search4vowels(word):
    """找出文本中出现的元音字母"""
    return set("aeiou") & set(word)
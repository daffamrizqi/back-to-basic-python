def isAnagram(s: str, t: str) -> bool:
    # s_sort = sorted(s.strip())
    # t_sort = sorted(t.strip())

    # return s_sort == t_sort

    return sorted(s.strip()) == sorted(t.strip())


print(isAnagram("anagram", "nagaram"))
print(isAnagram("a", "ab"))
print(isAnagram("ab", "a"))
print(isAnagram("aacc", "ccac"))

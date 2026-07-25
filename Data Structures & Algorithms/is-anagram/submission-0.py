class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = {}
        for char in s:
            if char in hash_table_s:
                hash_table_s[char] += 1
            else:
                hash_table_s[char] = 1
        
        hash_table_t = {}
        for char in t:
            if char in hash_table_t:
                hash_table_t[char] += 1
            else:
                hash_table_t[char] = 1

        return hash_table_s == hash_table_t
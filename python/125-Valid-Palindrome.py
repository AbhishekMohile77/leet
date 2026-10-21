class Solution:
    def isPalindrome(self, s: str) -> bool:
        sfor = []
        for i in s:
            if i.isalnum():
                sfor.append(i.lower())
            continue
        sback = sfor[::-1]
        return "".join(sfor)=="".join(sback)
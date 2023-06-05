class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        count=0;n=len(s)
        max_count=0
        for i in range(k):
            count+=1 if s[i] in vowels else 0
        max_count=max(max_count,count)

        for i in range(k,n):
            count-=1 if s[i-k] in vowels else 0
            count+=1 if s[i] in vowels else 0
            max_count=max(max_count,count)
        max_count=max(max_count,count)
        return max_count
    
if __name__ == '__main__':
    so=Solution()
    print(so.maxVowels("abciiidef",3))



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        n=len(s2)
        count=0
        freq_count=[0]*26
        freq_count_s1=[0]*26
        for i in range(k):
            freq_count_s1[ord(s1[i])-ord('a')]+=1
        for i in range(k):
            if s2[i] in s1:
                freq_count[ord(s2[i])-ord('a')]+=1
        if freq_count_s1==freq_count: return True
        for i in range(k,n):
            freq_count[ord(s2[i-k])-ord('a')]-= 1 if s2[k-i] in s1 else 0
            freq_count[ord(s2[i])-ord('a')]+= 1 if s2[i] in s1 else 0
            if freq_count_s1==freq_count:
                return True
        return False
    
if __name__=='__main__':
    so=Solution()
    print(so.checkInclusion("ab","eidbaooo"))
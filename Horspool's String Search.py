# Horspool's String Search use extra space to store the shift step of each letter in order to reduce time
ALPHA_SIZE = 256
def FindShifts(P):
    m = len(P)
    Shift = [m] * ALPHA_SIZE
    for j in range(m-1):   # 0 to m-2
        Shift[ord(P[j])] = m - j - 1   # ord() return the Unicode of character, something like ASCII?
    return Shift

def Horspool(Pattern, Text):
    m = len(Pattern)
    n = len(Text)
    Shift = FindShifts(Pattern)
    i = m-1
    while i < n:
        k = 0
        while k < m and Pattern[m-k-1] == Text[i-k]:
            k+=1
        if k == m:
            return i - m + 1
        else:
            i = i + Shift[ord(Text[i])]
    return -1

def Test():
    print(Horspool("ABCD", "ACBBBIPABCDD"))
    print(Horspool("ABCD", "ACBBBIPABCCDD"))

if __name__=="__main__":
    Test()
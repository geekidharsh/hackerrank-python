# https://www.hackerrank.com/challenges/sherlock-and-anagrams
cases = int(input())
for caseNo in range(cases):
    n = len(s)
    word_counter = {}
    result = 0

    for l in range(1, n):
        for i in range(n-l+1):
            substring = list(s[i:i+l])
            substring = sorted(substring)
            substring = ''.join(substring) 
            if substring in word_counter:
                word_counter[substring] += 1
                result += 1
            else: 
                word_counter[substring] = 1
    print(result)

def LeftRotateString( s, n):
    # write code here
    s = list(s)
    def exchange(ss):
        temp = 0
        if len(ss)%2 == 0:
            for i in range(int(len(ss)/2)):
                temp = ss[i]
                ss[i] = ss[-(i+1)]
                ss[-(i+1)] = temp
        else:
            for i in range(int((len(ss)-1)/2)):
                temp = ss[i]
                ss[i] = ss[-(i+1)]
                ss[-(i+1)] = temp
        return ss
    s = exchange(s[:n]) + exchange(s[n:])
    exchange(s)
    res = ''
    for i in s:
        res=res+i
    return res

print(LeftRotateString('abcdefg',2))
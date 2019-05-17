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

# print(LeftRotateString('abcdefg',2))

def PrintMinNumber(numbers):
    # write code here
    if numbers = []:
        return ""
    string_num = [str(num) for num in numbers]
    for i in range(len(string_num)-1):
        for j in range(len(string_num)-1):
            AB = int(string_num[j]+string_num[j+1])
            BA = int(string_num[j+1]+string_num[j])
            if BA < AB:
                temp = string_num[j]
                string_num[j] = string_num[j+1]
                string_num[j+1] = temp
    res = ''
    for i in string_num:
        res = res + i
    return int(res)

print(PrintMinNumber([]))
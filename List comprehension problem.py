st = 'Create a list of the first letters of every word in this string'.split()
list = []
for i in st:
    list.append(i[0])
print list

string = 'Create a list of the first letters of every word in this string'
s = [word[0] for word in string.split()]
print s




def func(st):
    num = 0
    num2 = 0
    for i in st.split():
        for j in i:
            if j.isalpha() and j == j.upper():
                num += 1
            if j.isalpha() and j == j.lower():
                num2 += 1

    print "Upper case chars : %d" %num
    print "Lower case chars : %d" %num2
func("Hi, how are you this Tuesday?")


print [x for x in range(100) if x % 7 == 0]

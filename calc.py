class Calculator(object):
    def multdiv(self, s):
        s = s.split()
        i = 0
        while i < len(s):
            if s[i] == "*":
                res = float(s[i - 1]) * float(s[i + 1])
                del s[i + 1], s[i], s[i - 1]
                s.insert(i - 1, res)
                i = 0
            elif s[i] == "/":
                res = round(float(s[i - 1]) / float(s[i + 1]), 2)
                del s[i + 1], s[i], s[i - 1]
                s.insert(i - 1, res)
                i = 0
            else: i += 1
        return s


    def sum(self, s):
        i = 0
        while i <= len(s):
            if s[i] == "+":
                res = float(s[i - 1]) + float(s[i + 1])
                del s[i + 1], s[i], s[i - 1]
                s.insert(i - 1, res)
                i = 0
            elif s[i] == "-":
                res = float(s[i - 1]) - float(s[i + 1])
                del s[i + 1], s[i], s[i - 1]
                s.insert(i - 1, res)
                i = 0
            elif len(s) == 1:
                break
            else:
                i += 1
        num = s[0]
        if int(num)==num:
            num = int(num)
        print num
        return num

    def res(self, str):
        return Calculator.sum(a, Calculator.multdiv(a, str))
a = Calculator()



res("127")
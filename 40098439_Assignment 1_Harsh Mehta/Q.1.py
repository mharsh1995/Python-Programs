class statement:
    # Create constructor and initialize dictionary
    def __init__(s, pro, D):
        s.proposition = pro
        s.D = D
        s.stack = []
        s.ts = []
    # Use of dictionary to defined given functions
    def Dict(s, key, a, ar, k):
        b = k.get('b', None)
        solver = {
            '|': a or b,
            '&': a and b,
            '~': not a,
            '->': not a or b,
            'True': True,
            'False': False
        }
        return solver[key]
    def Exp(s, exp):
        if len(exp) == 3:
            x = s.D[str(exp[0])]
            y = s.D[str(exp[2])]
            output = s.Dict(exp[1], x, y)
            print(output)
        elif len(exp) == 1:
            print(exp[0])
        elif len(exp) == 2:
            return s.Dict('~', s.D[exp[1]])
    # This function when not is in the logical statement
    def snot(s, exp):
        tlist = []
        Returned = []
        for i in exp:
            if i != '~':
                Returned.append(i)
            elif i == '~':
                tlist.append('~')
                tlist.append(Returned.pop())
                Returned.append(str(s.Exp(tlist)))
                tlist = []
        print(Returned)
    # Use of stack to push and pop variables
    def stack(s):
        count = 0
        temp = 0
        val = []
        solution = []
        temp1 = []
        for i in s.proposition:
            if i == '(':
                count = count + 1
            if i != ')':
                s.stack.append(s.D[i])
            elif i == ')':
                count = count - 1
                while True:
                    pop = s.stack.pop()
                    if pop == '(':
                        break
                    val.append(pop)
                if '~ ' in val:
                    val = s.snot(val)
                # if Variables are more than 3 then using this function
                elif len(val) > 3:
                    while temp < len(val):
                        if temp != 0 and temp % 2 == 0:
                            solution.append(val[temp])
                            temp = s.Exp(solution)
                            del solution[:]
                            solution.append(str(temp))
                            temp = temp + 1
                        else:
                            solution.append(val[temp])
                            temp = temp + 1
                    val = solution
                # using append add all variables used in statement joined
                s.stack.append(str(s.Exp(list(reversed(val)))))
                del val[:]
        print(s.stack)
    def solF(s):
        print(s.stack[0])

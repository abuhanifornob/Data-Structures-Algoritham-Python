from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,item):
        self.container.append(item)
    def pop(self):
        return self.container.pop()
    def size(self):
        return len(self.container)
    def is_Empty(self):
        return len(self.container)==0
    def peek(self):
        return self.container[-1]
    def reverse_string(self):
        return self.container[::-1]
    def print(self):
        sl=""
        for item in self.container:
            sl+=str(item)+ "--> "
        print(sl)
def revice_string(s):
    stack=Stack()
    for c in s:
        stack.push(c)

    rvs=""
    while stack.size()!=0:
        rvs+=stack.pop()
    return rvs
#..................................()()() ....................................

def is_balance(input_str):
    s=list()
    for c in input_str:
        if c=='(':
            s.append()
        if c==')':
            if not s:
                return False
            s.pop()
    return not s

# Excersice  .... whien input is  (){}[] then result Balance . which input )((){}[] then result is not Balance

def is_all_balance(input_star):
    ps=list()
    cs=list()
    ss=list()
    for ch in input_star:
        if ch=='(':
            ps.append(ch)
        if ch=='{':
            cs.append(ch)
        if ch=='[':
            ss.append(ch)
        if ch==')':
            if not ps:
                return False
            ps.pop()
        if ch=='}':
            if not cs:
                return False
            cs.pop()

        if ch==']':
            if not ss:
                return False
            ss.pop()
    return not cs and not ps and not ss

# Excersise:
# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

def is_match(ch1,ch2):
    dic={
        ')':'(',
        '}':'{',
        ']':'['
    }
    return dic[ch1]==ch2
def code_is_balance(s):
    stack=Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch=="[":
            stack.push(ch)
        if ch==')' or ch=='}' or ch==']':
            if stack.size()== 0:
                return False
            if not is_match(ch,stack.pop()):
                return False
    return stack.size()==0

if __name__=="__main__":
    st=Stack()
    print(revice_string("We will conquere COVID-19"))

    input_str=input("Please input: ")
    if is_all_balance(input_str):
        print( input_str," Is Balance")
    else:
        print(input_str," is Not Balance")

    code_input=input("Please patten input ")
    if code_is_balance(code_input):
        print(code_input,' is Balance')
    else:
        print(code_input,'is not balance')


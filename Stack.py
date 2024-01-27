class Stack:
    stack = []
    pointer = -1
    print("stack created")
    
    def push(self, element):
        self.stack = self.stack + [element]
        self.pointer += 1
    def peek(self):
        return self.stack[-1]
    def pop(self):
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        print("removed value - ", val)
        self.pointer -= 1
        return val
    
    def displayStack(self):
        print(self.stack)
    
#-----------------------------------------------
        
def checkBrackets(string):
    stk = Stack()
    leftBrackets = ["(", "{", "["]
    rightBrackets = [")", "}", "]"]
    count = 1
    for i in string:
        if i in leftBrackets:
            stk.push(i)
        if i in rightBrackets:
            if stk.pointer == -1:
                print("This expression is NOT correct.")
                print(f"Error at character #{count}. '{i}'-not opened")
                return
            else:
                validity = False
                n = stk.pop()
                if n == "(" and i == ")":
                    validity  = True
                elif n == "{" and i == "}":
                    validity = True
                elif n == "[" and i == "]":
                    validity = True
                else:
                    validity = False
                    
                if validity != True:
                    print(f"Error at character #{count}. '{i}'-not opened.")
                    return
        count += 1   
        
    if stk.pointer == -1:
        print("This expression is correct")
        return
    else:
        print("This expression is not correct")
        while stk.pointer != -1:
            a = stk.pop()
            print(f"Error at #char. '{a}'- not closed.")
            print(count)
            stk.pointer -= 1
        return
    


st1 = Stack()
st1.displayStack()

st1.push(20)
st1.push(30)
st1.push(40)

st1.displayStack()

st1.pop()
st1.displayStack()

print(st1.peek())

checkBrackets('1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')
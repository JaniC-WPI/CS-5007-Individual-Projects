open_list = ["[","{","("]
close_list = ["]","}",")"]

def isBalanced(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        print("Balanced")
        return True
        
    else:
        print("Unbalanced")
        return False
    
def query(input):
    cont = True
    while cont == True:
        


def main():
    str = "{{[(12+9)/3]+7.2*[(6-4)/8]}"

    isBalanced(str)

if __name__== '__main__':
    main()
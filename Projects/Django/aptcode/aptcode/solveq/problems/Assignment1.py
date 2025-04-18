Title = "Valid Parentheses"
Question = '''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

    Input: s = "()"

    Output: true

Example 2:

    Input: s = "()[]{}"

    Output: true

Example 3:

    Input: s = "(]"

    Output: false

Example 4:

    Input: s = "([])"

    Output: true'''

Solutuoin = '''
def Solution(expression):
    print("Solution funciton is getting called with expression = ", expression)

if __name__ == "__main__":
    assert(Solution(expression = "()") == True)
    assert(Solution(expression = "()[]{}") == True)'''


keywords = '''stack, string'''

def Solution(expression):
    print("Solution funciton is getting called with expression = ", expression)

if __name__ == "__main__":
    assert(Solution(expression = "()") == True)
    assert(Solution(expression = "()[]{}") == True)
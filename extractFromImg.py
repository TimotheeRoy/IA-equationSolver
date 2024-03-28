from PIL import Image
import pytesseract 
from sympy import symbols, solve, sympify

num = ['2','3','4','5','6','7','8','9']

img = Image.open('test.jpg')
txt = pytesseract.image_to_string(img)

X = symbols('X')
eq = txt.split()[0]

new_eq = [eq[0]]
for i in range(1,len(eq)):
    if eq[i-1] in num and eq[i] == 'X':
        new_eq.extend(['*', eq[i]])
    else:
        new_eq.append(eq[i])

sympy_eq= ''.join(new_eq)
print(sympy_eq)

test = sympify(-4*X+7=15)
#solve(sympy_eq)
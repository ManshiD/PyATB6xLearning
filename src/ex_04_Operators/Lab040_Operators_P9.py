# divmod function - It will give you quotient and remainder both.
'''
@overload def divmod(__x: SupportsDivMod[_T_contra, _T_co],
           __y: _T_contra) -> _T_co
Return the tuple (x// y, x%y). Invariant: div*y + mod == x.
`divmod(__x, __y)` on docs. python. org
'''
q, r = divmod(5, 2)
print(q)  # quotient 2
print(r)  # remainder 1

# Assign multiple values in Python
a, b, c = 1, 2, 3
print(a)    #1
print(b)    #2
print(c)    #3

# Increment (++) / Decrement (--) Operators
# Python does not have ++, -- operator

x = 5
x += 1
print(x)    #6

x -= 1
print(x)    #6-1=5

x *= 3
print(x)    #x=x*3  so x=5*3=15





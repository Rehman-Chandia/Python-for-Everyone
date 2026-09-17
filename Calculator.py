x = input()

if '+' in x:
    a, b = x.split('+')
    print(int(a) + int(b))

elif '-' in x:
    a, b = x.split('-')
    print(int(a) - int(b))

elif '*' in x:
    a, b = x.split('*')
    print(int(a) * int(b))

elif '/' in x:
    a, b = x.split('/')
    print(int(a) // int(b))

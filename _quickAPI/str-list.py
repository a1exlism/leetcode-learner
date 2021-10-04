# str to list
s1 = '1234'
l1 = list(s1)  # ['1', '2', '3', '4']

s2 = '1 2 3 4'
l2 = s2.split(' ')  # ['1', '2', '3', '4']

# list to str
s3 = ''.join(l1)  # '1234'

l4 = [int(i) for i in '1234']  # [1, 2, 3, 4]
s4 = ''.join(str(e) for e in l4)  # '1234'

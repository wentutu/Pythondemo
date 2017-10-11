#dict
d={'tutu':100,'Bob':99,'qq':50}
s=d['tutu']
print s
d['jack']=60
j=d['jack']
print j

if 'tutu' in d:
    print d['tutu']
d.pop('tutu')
print d['tutu']
name = str(input('What is your name?'))
if name == 'Cristian':
   print('Your name is beautiful!')
else:
    print('Your name ugly')
print('Good morning, {}!!'.format(name))



n1 = float(input('Type your first grade: '))
n2 = float(input('Type your second grade: '))
m = (n1 + n2)/2
print('Your final grade is {:.1f}'.format(m))
if m >= 6.0:
    print('your final grade is really good')
else:
    print('You need study more!!')

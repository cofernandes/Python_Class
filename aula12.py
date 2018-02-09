name = str(input("What is your name?"))
if name == 'Gustavo':
    print('Is a beautiful name')
elif name == 'Peter' or name == 'Paul' or name == 'Anne':
    print('Your name is popular in Brazil')
elif name in 'Claudia Jessica Juliana':
    print('it is a beautiful female name!!')
else:
    print('Your name is Normal.')
print('Have a nice day {}'.format(name))


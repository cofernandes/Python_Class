#name = input('what is your name')
#print ('nice to meet you{:=^20}!'.format(name))

n1 = int(input('type um valor'))
n2 = int(input('type other number'))

s = n1+n2
m = n1*n2
d = n1 /n2
di = n1//n2
e = n1**n2
print('the sun is {}, the product is {} devisao is {:.3f}'.format(s,m,d), end=' ')
print('Divisao inteira {} and potencia {}'.format(di,e))
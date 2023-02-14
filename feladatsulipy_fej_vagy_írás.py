import random

dobás=random.randint(1,2)

print(dobás)
válasz=input('Találd ki mit dobok! Fej vagy írás(f/í)? ')

if dobás == 1 and válasz == 'f' or válasz== 'F' or válasz=='fej' or válasz=='Fej':
    print('Eltaláltad! Fejjet dobtam.')
    
elif dobás == 2 and válasz == 'í' or válasz== 'Í' or válasz=='írás' or válasz=='Írás':
    print('Eltaláltad! Írást dobtam.')
    
else:
    print('Nem Talált')
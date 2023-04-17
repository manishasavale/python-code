import string
import UserString

st = string.Template('warninggoccuedinwhen')


s = st.substitute({'warning': 'Lack of electricity', 'when': 'April 3, 2002'})

print(s)

s = UserString.MutableString('Python')
s[0] = 'P'

print (s)

u = u'Husker Du'

s = u.encode('latin1')

print(s, '=>', type(s))




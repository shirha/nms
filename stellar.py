key = 'B'
dict_ = {"F":"yl","G":"yl","K":"rd","M":"rd","B":"bl","O":"bl","G":"gr"}
func = lambda x: x[0] == key
color = list(filter(lambda x: x[0] == key, 
  {"F":"yl","G":"yl","K":"rd","M":"rd","B":"bl","O":"bl","G":"gr"}.items()))[0][1]
print(color)
print('Stellar Classification: B1pf'[24])
def fun1(name='sasi'):
   print("inside function fun1")
   def fun2():
       return "\t this is inside fun2"
   def fun3():
       return "\t this is inside fun3"
   if name == 'Sasi':
       return fun2
   else:
       return fun3
   print(" end of the fun ")

   return(name)

x = fun1()
print(x())


'''def hello():
   return "Hi Sasi"
def other(fun):
   print("other code go here")
   print(fun())

other(hello)
'''
def new_decorator(unc):
   def wrap_fun():
       print("Before executing func")
       unc()
       print("after executing func")
   return wrap_fun

@new_decorator
def fun_need_decorator():
    print("this function needed decorator")

fun_need_decorator()

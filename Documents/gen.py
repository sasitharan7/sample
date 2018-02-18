def generator_fun():
   for i in range(3):
       yield i

gen = generator_fun()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

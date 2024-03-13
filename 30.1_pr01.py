class Programmer:
	def __init__ (oo,name,age, wpm):
		oo.name=name
		oo.age=age
		oo.wpm=wpm

pp=Programmer("Pranjal",18,30)
pp.age=pp.age+23
print(pp.age)
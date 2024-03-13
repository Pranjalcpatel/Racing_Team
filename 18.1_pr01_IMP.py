s=set()
s.add(12)
s.add(12.0)
s.add("12")
#since 12=12.0 only adds 12 to the set
print(s)
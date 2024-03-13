oxford={
    "gift":"present",
    "this":"A keyword in c++",
    "mylist": [1,2,3]
}
print(oxford.items()) #gives a tuple of key value pairs
#o/p-> dict_items([('gift', 'present'), ('this', 'A keyword in c++'), ('mylist', [1, 2, 3])])
# for key in oxford.keys():
#     print(key)
oxford.update({"gift":"uphaar","mylist":[12,12,12]})
# #if some key is updated which is not in dict. then that key is added at the end of dict
# for a,b in oxford.items():
#     print(a,":",b)

print(oxford.get("this"))

#difference between oxford.get("this") and oxford["this"]
#if I put a keyword not in dict instead of this then .get returns None and doesn't terminate the program whereas the other one throws an error 
# print(oxford.get("notthis"))
# print(oxford["notthis"])

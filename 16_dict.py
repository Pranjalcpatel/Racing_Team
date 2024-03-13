oxford={
    "gift":"present",
    "this":"A keyword in c++",
    "mylist": [1,2,3]
}
#gift is key, present is value
#[1,2,3]="mylist" is not a valid element in this list
print(oxford)
print(oxford["gift"])
# It is unordered in versions below 3.7(if you print dictionary itmay be printed differently each time), in mine(3.11) they are ordered
# It is mutable
# if you duplicate any key like this:
# oxford={
#     "gift":"present",
#     "this":"A keyword in c++",
#     "mylist": [1,2,3],
#     "this":"that"
# }
# print(oxford)
# o/p={'gift': 'present', 'this': 'that', 'mylist': [1, 2, 3]}
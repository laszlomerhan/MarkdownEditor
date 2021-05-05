# use the function blackbox(lst) that is already defined
my_lst = []
new = blackbox(my_lst) 

if id(new) == id(my_lst):
    print("modifies")
else:
    print("new")

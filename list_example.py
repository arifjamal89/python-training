list_a = [1,2,3,4]
list_b = list()

#print(len(list_a)) # untuk tengok berapa nombor yang ada dalam list
#print(len(list_b))

list_c = [1,2,3,4,5]
list_d = [i*2 for i in list_c] # List Comprehension. looping value dalam list untuk darab 2.
list_e = [i*i for i in list_c] # List Comprehension. looping value dalam list untuk darab diri sendiri.

print(list_d)
list_a.extend(list_c) #empty_list function extend gabung list a dan list c
print(list_a)

#LIST OPERATION
empty_list=[]
empty_list.append('a')
empty_list.append('b') #append tambah di belakang value sebelum
print(empty_list)


#Tuple is immutable. kalau dah create xboleh berubah. lebih laju dari list

tuple_a=('a','a','b','c','a')
tuple_b = tuple()
#print(bool(tuple_a))
#print(bool(tuple_b))

tuple_c =(1,2,3)
tuple_d = 1,
#print(bool(tuple_c))
#print(bool(tuple_d))

#TUPLE OPERATIONS

print(tuple_a.count('a')) #count berapa value a ada dalam tuple
print(tuple_c.index(1)) #dia cari value 1 dalam tuple berada di kedudukan mana
print(tuple_a[0])
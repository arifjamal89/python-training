dict_a= dict() #if dict_a -> False
dict_b={} #empty dictionary


dict_a['hello'] = 'world'
dict_a['mohd'] = 'arif'

print(dict_a)
print(dict_a['hello']) #macam translate tunjuk value hello sama dengan world

print(dict_a.get('error','Not Found.')) #untuk check kalau error xdak dalam dict akan keluar not found


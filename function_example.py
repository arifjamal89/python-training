# Function definition

# def function_name(a,b,c):
#     <body of function>
#     return <return value>


def add_number(a, b):
    total = a+b
    return total

def total(*args):
    pass            # mesti letak sama ada pass atau ...

add_a = add(1, 2)
add_b = add('hello', 'world')
add_c = add(1.0, 3)

print (add_a, add_b, add_c)
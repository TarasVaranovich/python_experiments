tuple = (1, 2, 'hi')
print(len(tuple))  ## 3
print(tuple[2])    ## hi
#tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works

tuple = ('hi',)   ## size-1 tuple

(x, y, z) = (42, 13, "hike")
print(z)  ## hike
#(err_string, err_code) = Foo()  ## Foo() returns a length-2 tuple
str = "label"
int_arr = [] 
xor_arr = []
enc = ''
for c in str:
    tmp = ord(c)
    int_arr.append(tmp)
    tmp ^= 13
    xor_arr.append(tmp)
    enc +=  chr(tmp)


print(int_arr)
print(xor_arr)
print(enc)



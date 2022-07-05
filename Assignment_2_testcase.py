import numpy as np

a = np.random.randint(1, 10, size =(1024, 900),dtype='int64')
print(a)
np.savetxt('C:/Users/ashwina/Downloads/a.txt', a , fmt='%d')

b = np.random.randint(1, 10, size =(1024, 900),dtype='int64')
print(b)
np.savetxt('C:/Users/ashwina/Downloads/b.txt', b , fmt='%d')

c = np.random.randint(1, 10, size =(800, 1024),dtype='int64')
print(c)
np.savetxt('C:/Users/ashwina/Downloads/c.txt', c , fmt='%d')

d = np.random.randint(1, 10, size =(800, 990),dtype='int64')
print(d)
np.savetxt('C:/Users/ashwina/Downloads/d.txt', d , fmt='%d')

temp1 = np.transpose(a)
temp2 = np.transpose(b)
add1 = np.add(temp1,temp2)
temp3 = np.transpose(c)
mul = np.matmul(add1, temp3)

out = np.matmul(mul , d)
print(out)
np.savetxt('C:/Users/ashwina/Downloads/out.txt', out , fmt='%d')

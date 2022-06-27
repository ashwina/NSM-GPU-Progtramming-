import numpy as np

a = np.random.randint(1, 1000, size =(1000, 900),dtype='int64')
print(a)
np.savetxt('C:/Users/ashwina/Downloads/a.txt', a , fmt='%d')

b = np.random.randint(1, 1000, size =(1000, 900),dtype='int64')
print(b)
np.savetxt('C:/Users/ashwina/Downloads/b.txt', b , fmt='%d')

temp1 = np.add(a, b)
temp2 = np.transpose(temp1)

sub1 = np.subtract(b,a)
trans = np.transpose(sub1)

out = np.subtract(temp2 , trans)
print(out)
np.savetxt('C:/Users/ashwina/Downloads/out.txt', out , fmt='%d')

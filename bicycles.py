bicycles= ['trek','cannodale', 'redline', 'specialized']
print(bicycles[-1].upper())
#bicycles[1]= 'firecracker'
#print(bicycles)
bicycles.append('firecracker ')
#print(bicycles)

bicycles.insert(2, 'no bike')
print(bicycles)

del bicycles[2]
print(bicycles)
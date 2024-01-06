import time

timestamp=time.strftime("%H:%M:%S")
print(timestamp)
print(type(timestamp))

init=time.time()
for i in range(0,5000):
    print(i)

print(time.time()-init)
time.sleep(5)
print('after sleep')

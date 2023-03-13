import time

n = 100000
x = 0
while_total_sum = 0
for_total_sum = 0

#While function start
print("While Loop performance:")
time_start = time.time()

while x <= n:
    while_total_sum = while_total_sum + x
    x = x+1

print(while_total_sum)
time_end = time.time()
time_total = time_end - time_start
print(time_total)

#For function start
print("\nFor Loop performance:")
time_start = time.time()

for y in range(n+1):
    for_total_sum = for_total_sum + y

print(for_total_sum)
time_end = time.time()
time_total = time_end - time_start
print(time_total)
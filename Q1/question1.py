# Q1    

#storage
n = int(input())
storage_size = input().split()
storage_size()
# customer requst
m = int(input())
request_size = input().split()

fulfilled = [False] * m

for i, j in enumerate(request_size):
    for s in storage_size:
        if s >= j:
            fulfilled[i] = True
            break

for f in fulfilled:
    if not f:
        print("No")
print("Yes")

    
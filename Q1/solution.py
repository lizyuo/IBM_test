# Q1    

with open("input.txt", "r") as f:
    
    #storage
    n = int(f.readline())
    storage_size = f.readline().split()
    
    # customer requst
    m = int(f.readline())
    request_size = f.readline().split()


fulfilled = 0

for i, j in enumerate(request_size):
    for s in storage_size:
        if s >= j:
            fulfilled += 1 # fulfilled
            break

# all fulfilled
if fulfilled == m:
    print("Yes")
else: 
    print("No")

    
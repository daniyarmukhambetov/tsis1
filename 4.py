ans = int(0)
for i in range(1,18,4):
    # print(i,end=' ')
    ans+=4/i
for i in range(3,20,4):
    # print(i,end=' ')
    ans-=4/i
print(ans)
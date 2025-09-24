#a=list(map(int,input().split()))
# for i in a:
    # value=a.count(i)
    # if(value == 1):
        # print(i)
        # break

# m,n=list(map(int,input().split()))
# sum = 0
# for i in range(m,n+1):
    # sum = sum+i
# print(sum)/


# S=input()
# l=[]
# c=""
# for i in S:
    # if i.isdigit():
        # l.append(int(i))
    # elif i.isalpha():
        # c=c+i
# print(min(l))
# print(max(l))
# print(sum(l))
# print(c)


x =input()
y =""
for i in x:
    if not i.isalnum():
        y=y+i
print(y)


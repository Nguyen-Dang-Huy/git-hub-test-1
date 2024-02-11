def Jump_Search(a,k):
    step=3
    for i in range(0,len(a),step):
        if a[i]==k:
            return i
        elif (i+step<=len(a)-1)and(a[i]<k)and(k<=a[i+step]):
            for j in range(i+1,i+step+1):
                if a[j]==k:
                    return j
        elif (i+step>len(a)-1)and a[i]<k:
            for j in range(i+1,len(a)):
                if a[j]==k:
                    return j
    return -1
def jumsearch(a,k):
    i=0
    j=i+3
    while (j<n)and(a[j]<k):
        i+=3
        j+=3
    if j>n-1:
        j=n-1
    while (i<n)and(a[i]!=k):
        i+=1
    if i<n:
        return i
    else:
        return -1
if __name__=='__main__':
    # n=int(input('Nhập N: '))
    # # arr=list(map(int, input()))
    # arr=[]
    # for i in range(n):
    #     h=int(input())
    #     arr.append(h)
    # k=int(input('Nhập K: '))
    # arr.sort()
    arr=[1,2,3,4,5,6,7,8,9,10,11]
    n=10
    k=int(input())
    i=0
    print(Jump_Search(arr,k))
    # bl=False
    # while i<=n-1:
    #     if arr[i]<k:
    #         i+=3
    #     elif arr[i]>k:
    #         for j in range(i-3,i):
    #             if arr[j]==k:
    #                 locate=j
    #                 bl=True
    #                 break
    #         break
    #     elif arr[i]==k:
    #         locate=i
    #         bl=True
    #         break
    # if bl==False:
    #     print(-1)
    # else:
    #     if i<=n-1:
    #         print(locate)
    #     else:
    #         for j in range(i-3,n):
    #             if arr[j]==k:
    #                 print(j)
    #                 break
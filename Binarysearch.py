# THUẬT TOÁN TÌM KIẾM NHỊ PHÂN
def Binarysearch(a,k):
    left=0
    right=len(a)-1
    while left<=right:
        mid=round((left+right)/2)
        if a[mid]==k:
            return mid
        elif a[mid]<k:
            left+=1
        else:
            right-=1
    return -1
def vitri(a,k):
    n=len(a)
    i=round(n/2)
    count=0
    bl=False
    while (bl==False)and(count<n):
        if a[round(n/2)]>k:
            a=a[:round(n/2)]
            n=len(a)
            i=round(n/2)
        elif a[round(n/2)]<k:
            a=a[round(n/2)+1:]
            count=count+round(n/2)+1
            n=len(a)
            i=round(n/2)
        else:
            a=a[:round(n/2)]
            n=len(a)
            count=count+n
            bl=True
    if count<n:
        return count
    else:
        return-1
def BS_dequi(a,k,l,r):
    if l==r:
        if a[l]==k:
            return l
        else:
            return -1
    else:
        mid=(l+r)//2
        if a[mid]==k:
            return mid
        else:
            if a[mid]>k:
                return BS_dequi(a,k,l,mid-1)
            else:
                return BS_dequi(a,k,mid+1,r)
if __name__=='__main__':
    # n=int(input('Nhập N: '))
    # a=[]
    # for i in range(n):
    #     a.append(int(input()))
    k=int(input('Nhập K: '))
    a=[0,1,2,3,4,5,6,7,8,9,10]
    print('vị trí của',k,'là:',BS_dequi(a,k,0,len(a)-1))

#implementation of merge sort

def mergesort(arr): 
    if len(arr)>1:
        r=len(arr)//2                     # r is the point where array is divided in 2 subarrays
                                                     
        L=arr[:r]                         #left subarray
        M=arr[r:]                         #right subarray

        #sorting two subarrays 
        mergesort(L)
        mergesort(M)

        i=j=k=0
        
        #Comparing L and M and placing the smallest element in the correct position of auxiliary array
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=M[j]
                j+=1
            k+=1

        #When we run out of elements in L or M, pick up the remaining elements and put in auxiliary array
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(M):
            arr[k]=M[j]
            j+=1
            k+=1
#Test Case
if __name__ == '__main__':
    #user input array
    a=[]
    a=[int(itms) for itms in input("Enter the elements: ").split()] 
    print("Array: ",a)
    mergesort(a)
    print("Sorted array: ",a)
N1 = int(input())
arr1 = set(input().split())
B1= int(input())
arr2 = set(input().split())
arr3 = arr2.intersection(arr1)
print(len(arr3))
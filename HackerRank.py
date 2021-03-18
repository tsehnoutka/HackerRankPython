if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    
    i = len(arr)-1
    max = arr[i]
    found = False
    while i >=0 and not found:
        if max > arr[i]:
            found =True
        else:
            i -= 1
    print (arr[i])
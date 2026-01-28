class Algorithm:
    def binary_search(self, low:int, high:int, target:int, arr:list[int])->int:
        if low > high:
            return -1

        mid = low + (high - low)//2
        if (target == arr[mid]):
            return mid
        if target > arr[mid]:
            return self.binary_search(mid + 1, high, target, arr)
        if target < arr[mid]:
            return self.binary_search(low , mid - 1, target, arr)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    target = 5
    obj = Algorithm()
    print(obj.binary_search(0, len(arr), target, arr))

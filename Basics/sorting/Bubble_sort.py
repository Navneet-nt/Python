class Algorithm:
    def bubble_sort(self, nums:list[int])->list[int]:
        n = len(nums)
        for i in range(n):
            swapped = True
            for j in range(0,n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = False
            if swapped:
                break

        return nums

if __name__ == "__main__":
    nums = [3, 5, 2, 7, 1]
    ob = Algorithm()
    print(ob.bubble_sort(nums))

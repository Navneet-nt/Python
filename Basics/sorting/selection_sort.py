class Algorithm:
    def selection_sort(self, nums:list[int]):
        for i in range(len(nums)-1):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[min_index]>nums[j]:
                    nums[min_index], nums[j] = nums[j], nums[min_index]

if __name__ == "__main__":
    nums = [3, 4, 1, 5, 2]
    obj = Algorithm()
    obj.selection_sort(nums)
    print(nums)
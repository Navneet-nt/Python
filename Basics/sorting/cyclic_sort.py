class Algorithm:
    @staticmethod
    def cyclic_sort(nums:list[int]):
        i = 0
        while (i < len(nums)):
            correct_index = nums[i]
            if (nums[correct_index] != nums[i]):
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1

if __name__ == "__main__":
    nums = [2, 4, 1, 3, 0, 5]
    Algorithm.cyclic_sort(nums)
    print(nums)
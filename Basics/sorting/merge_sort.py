class Algorithm:
    def merge_sort(self, nums:list[int]) -> list[int]:
        if (len(nums) <= 1):
            return nums
        mid = len(nums) // 2
        left = nums[0:mid:1]
        right = nums[mid:len(nums):1]
        left_sorted = self.merge_sort(left)
        right_sorted = self.merge_sort(right)
        return self.merge(left_sorted, right_sorted)

    def merge(self, left:list[int], right:list[int]) -> list[int]:
        i = 0
        j = 0
        answer = []
        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                answer.append(left[i])
                i += 1
            else:
                answer.append(right[j])
                j += 1
        answer.extend(left[i:len(left)])
        answer.extend(right[j:len(right)])
        return answer

if __name__ == "__main__":
    nums = [2, 4, 1, 5, 3, 6]
    obj = Algorithm()
    nums = obj.merge_sort(nums)
    print(nums)
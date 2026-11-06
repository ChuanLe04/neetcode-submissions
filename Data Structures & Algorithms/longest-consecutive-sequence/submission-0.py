class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_s = 0

        for n in num_set:
            if (n-1) not in num_set:
                current_num = n
                current_s = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_s += 1
                
                if current_s > longest_s:
                    longest_s = current_s
        
        return longest_s
    
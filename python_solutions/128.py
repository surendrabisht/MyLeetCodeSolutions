class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        dictionary={}
        longest_chain_length=0
        for no in nums:
            if dictionary.get(no) is None:
                before_no=dictionary.get(no-1,0)
                after_no=dictionary.get(no+1,0)
                chain_length=before_no+after_no+1
                dictionary[no]=chain_length
                dictionary[no-before_no] =chain_length
                dictionary[no+after_no] = chain_length
                longest_chain_length = max(longest_chain_length,chain_length)
        
        return longest_chain_length


if __name__ == '__main__':
    print(Solution().longestConsecutive([1,2,0,1]))


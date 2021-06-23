class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        dictionary={}
        for i in range(len(s)):
            if dictionary.get(s[i]) is None:
                dictionary[s[i]]=[i]
            else:
                 dictionary[s[i]].append(i)
        
        count=0
        for word in words:
            last_index=-1
            count +=1
            char_reached_index = {ch:-1 for ch in 'abcdefghijklmnopqrstuvwxyz'}
            for character in word:
                char_indices_list=dictionary.get(character)
                next_reach_index=char_reached_index[character]+1
                if char_indices_list is not None and len(char_indices_list)>next_reach_index:
                    new_index=char_indices_list[next_reach_index]
                    while last_index>new_index and len(char_indices_list)>next_reach_index+1:
                        next_reach_index=next_reach_index+1
                        new_index=char_indices_list[next_reach_index]

                    char_reached_index[character] = next_reach_index

                    if last_index> new_index:
                        count -=1
                        break
                    else:
                        last_index=new_index
                else:
                    count -=1
                    break
                
        return count
            


if __name__ == '__main__':
    print(Solution().numMatchingSubseq("dsahjpjauf",
["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))
           
            
        
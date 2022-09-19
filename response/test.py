#User function Template for python3

class Solution:
    def powerSet(self, s, temp, index):
        # base case 
        if len(s)==index:           
            print(temp, end=" ")
            return
        
        # take
        self.powerSet(s, temp+s[index], index+1)
        
        # not take
        self.powerSet(s, temp, index+1)
        return
    
    
	def AllPossibleStrings(self, s):
		self.powerSet(s, "", 0)
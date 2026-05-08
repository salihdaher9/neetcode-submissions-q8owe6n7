class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
                res = []
                if not digits:
                    return res
                digitToChar = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "qprs",
                    "8": "tuv",
                    "9": "wxyz",
                }


                def backtrack(digits,curr):
                    if not digits:
                        res.append(curr[:])
                        return
                    
                    for i in digitToChar[digits[0]]:  
                        curr+=i                         
                        backtrack(digits[1:],curr)
                        curr=curr[:-1]
                
                backtrack(digits,"")
                
                return res
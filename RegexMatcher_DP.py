


class Solution:
    def isMatchDP(self, regex, str):
            """
                bottom up DP formulation is:
                    d[i,j] = d[i+1,j+1] || d[i+1,j] || d[i+1,j+2]
            """


            #initialize dp matrix
            #i is string index,
            #j is regex pattern index
            dp = [[False for _ in range(0,len(regex)+1)] for _ in range(0,len(str)+1)]

            dp[-1][-1] = True
            #bottom-up construction of the dp matrix
            for i in range(len(str),-1,-1):
                for j in range(len(regex)-1,-1,-1):

                #duplicate the boolean logic of the recursive function
                #A. check the first match
                    first_match = (i < len(str)) and (regex[j] == str[i])

                #B.Kleene star case
                # check to see if previous j index value was a Kleene star
                # in this implementation, one is evaluating both inputs in reverse order
                # so one is checking j+1 and basing the current dp value on the regex chomp j+2
                    if j+1 < len(regex) and regex[j+1] == "*":
                        dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])

                #C. nominal case, chomp along by 1 on both str and regex
                    else:
                        dp[i][j] = first_match  and dp[i+1][j+1]
        

            return dp[0][0]









####################################TEST###########################
regex = "a*b"
str1 = "ab"
str2 = "aab"
str3  ="kb"
regex2 = "a*"
str4= "a"

t =  Solution()

print("Dynamic programming implementation results:")
print(t.isMatchDP(regex,str1))
print(t.isMatchDP(regex,str2))
print(t.isMatchDP(regex,str3))
print(t.isMatchDP(regex2,str4))









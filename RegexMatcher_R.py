class Solution:
    def isMatchRecursive(self,regex,str):
        
        
        #A.
        #null case
        if not regex:
            return not str
        
        #see if this level of recursion holds true
        first_match = False
        if str and (str[0] == regex[0]):
            first_match = True
        #B.
        # Kleene star case:
        #if len(regex) >=2 and regex[1]=="*",
        #     i. see if str matches regex beyond the "*" (chomp regex by 2, keep string) or
        #     ii. see if repeating (keep regex, chomp string)
        if (len(regex) >= 2) and regex[1] == "*":
            return (self.isMatchRecursive(regex[2:], str)) or (first_match and self.isMatchRecursive(regex,str[1:]))
        
        #C.
        # nominal recursive case, chomp both str and regex
        else:
            return first_match and self.isMatchRecursive(regex[1:], str[1:])
        
        return False


####################################TEST##################
regex = "a*b"
str1 = "ab"
str2 = "aab"
str3  ="kb"
regex2 = "a*"
str4= "a"

t =  Solution()

print("Recursive implementation results:")
print(t.isMatchRecursive(regex,str1))
print(t.isMatchRecursive(regex,str2))
print(t.isMatchRecursive(regex,str3))
print(t.isMatchRecursive(regex2,str4))

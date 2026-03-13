# You have a string s composed only of the characters (, ), {, }, [ and ]. 
# Determine if the bracket arrangement in this string is valid. 
# Specifically, a valid string must meet the following criteria:

# Each opening bracket has a corresponding closing bracket of the same type.
# Brackets are closed in the correct order.
# Every closing bracket matches an earlier opening bracket of the same type.
# Examples:

# Input: s = "()" Output: true
# Input: s = "()[]{}" Output: true
# Input: s = "(]" Output: false
# Input: s = "([])" Output: true



# Schau dir den ersten/nächsten Character an
# Schau dir die Art an von der Klammer
# such nach der Art von Klammer
# ENTWEDER es muss mit dem letzten oder den nächsten Character matchen.

s = "()"


def parenthesis(s):
    s_list = list(s)
    for char in s_list:
        if char == s_list[-1]:
            s_list.remove(s_list[0])
            s_list.remove(s_list[-1])
        elif char == s_list[1]:
            s_list.remove(s_list[0])
            s_list.remove(s_list[1])
        else:
            print("False")
            return False
    print("True")
    return True

parenthesis(s)
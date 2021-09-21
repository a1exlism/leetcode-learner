import re

"""
re.*
- findall	Return list
- search	Return Match `object`
- split 	Return list where the string has been split at each match
- sub	    Replaces one or many matches with a string
"""

if __name__ == "__main__":
    s = 'sjdkfsdkf'
    pattern = r'.*'
    res = re.findall(pattern, s, flags=0)
    print(res)


"""
.span()     returns a tuple containing the start-, and end positions of the match.
.string     returns the string passed into the function
.group()    returns the part of the string where there was a match
"""

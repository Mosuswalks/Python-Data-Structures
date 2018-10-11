import re

# Question: 1.3 
# Write a method to replace all spaces with "%20".
#       
# For this question, we can utilize Python's built in Regex module.
# We'll use the re.sub fucntion and the regular expression for white spaces to replace them with our required characters.
#
#
def urlify(string: str) -> str:
    string = re.sub(r'\s+', '%20', string)
    return string

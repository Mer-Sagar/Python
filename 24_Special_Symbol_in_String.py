#  Input : "wlecome @@32jhadb wjg sud &*$"
#  Output : String Contains Special Symbols

#  Input : "wlecome to India"
#  Output : String not Contains Special Symbols

import re

str = "wlecome @@32jhadb wjg sud &*$"
str1 = "wlecome to India"

regex= re.compile('[!@#$%^*?/\|~`]')

if(regex.search(str1) == None):
    print("No special Characters present in a string")
else:
    print("special Characters present in a string")

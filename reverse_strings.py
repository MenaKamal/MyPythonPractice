# reverse strings @Mena Kamal
myStr = ("this is a very nice challenge").split()
Str = ""
# Method one usign [:]
for x in myStr:Str = Str + x[::-1] + " "
print Str

# Method two using reversed function 
Str = ""
for x in myStr:Str = Str + "".join(reversed(x)) + " "
print Str

# Method three you con reverse the order of string and the words
myStr = ("this is a very nice challenge") 
print "".join(reversed(myStr))

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
header =  list()
email = list()
for line in fh:
  if "From " not in line: continue
  words = line.split()
  email = words[1]
  print email
  count += 1
   
#print email
print "There were", count, "lines in the file with From as the first word"



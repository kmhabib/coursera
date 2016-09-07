
fname = raw_input("Enter file name: ")
fh = open(fname)
result= []
for line in fh:
  words = line.split()
  for word in words:
    if word not in result:
      result.append(word)

result.sort()      

print result

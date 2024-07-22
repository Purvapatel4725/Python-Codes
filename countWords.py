def countWords(arg):
  words = arg.split(" ")
  Totalrepetation = {}
  for i in words:
    if i in Totalrepetation:
      Totalrepetation[i] += 1
    else:
      Totalrepetation[i] = 1
  return Totalrepetation

print(countWords("Apple Mango Orange Mango Guava Guava Mango"))
print(countWords("Train Bus Bus Train Taxi Aeroplane Taxi Bus"))
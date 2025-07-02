fileName = input("Enter the name of the file: ")

words = {}
alphabeticOrderWords = {}

# Here, we store the count of each word appeared in file as dictionary
# key being word and value being count 

with open(fileName,'r') as file:
  for line in file:
    for word in line.split():
      if word in words:
        words[word] += 1
      else:
        words[word] = 1
        
# Normal Order printing as it appears in file
# for word in words.items():
#   print(f"{word[0]} : {word[1]}")
  
listAlphabeticWiseWords = sorted(list(words.keys()))

for word in listAlphabeticWiseWords:
  alphabeticOrderWords[word] = words[word]

for word in alphabeticOrderWords.items():
  print(f"{word[0]} : {word[1]}")

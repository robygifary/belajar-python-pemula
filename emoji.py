pesan = input(">>> ")

emoji_map = {
  ":)" : "😊",
  ":D" : "😃",
  ":p" : "😋",
  ":*" : "😉",
  ":'(" : "🥲",
  ":(" : "😞",
  "O:)" : "😇"
}

words = pesan.split(" ")

output = ""

for w in words:
  output = output + emoji_map.get(w, w) + " "

print(output)
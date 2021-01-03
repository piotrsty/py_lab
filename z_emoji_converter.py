# Emoji Converter
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "buzka wesola",
    ":(": "buzka smutna"
}
output = ""
#print(words)
#print(message)

for word in words:
    output += emojis.get(word, word ) + " " 
print(output)

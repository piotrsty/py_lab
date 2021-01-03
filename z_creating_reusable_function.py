# Emoji Converter

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "buzka wesola",
        ":(": "buzka smutna"
    }
    output = ""
# print(words)
# print(message)

    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
result = emoji_converter(message)
print(result)
# print(moji_converter(message))

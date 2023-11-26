def text_to_emoji_converter(text):
    emoji_dict = {
        'a': '😃', 'b': '😎', 'c': '🤖', 'd': '🚀', 'e': '🌈', 'f': '🌟',
        'g': '🍀', 'h': '🎉', 'i': '💡', 'j': '🎸', 'k': '🔑', 'l': '📚',
        'm': '🔍', 'n': '🌙', 'o': '🍊', 'p': '🎨', 'q': '🎭', 'r': '🚗',
        's': '🌊', 't': '🌄', 'u': '👾', 'v': '✌️', 'w': '🌳', 'x': '❌',
        'y': '💛', 'z': '🦓',

        'A': '😄', 'B': '😲', 'C': '😇', 'D': '😍', 'E': '😂', 'F': '🎩',
        'G': '🐸', 'H': '🏰', 'I': '🍦', 'J': '🎷', 'K': '🔪', 'L': '💡',
        'M': '🌟', 'N': '🌈', 'O': '🍭', 'P': '🎨', 'Q': '🎹', 'R': '🚀',
        'S': '🌊', 'T': '🌄', 'U': '🌈', 'V': '✌️', 'W': '🌅', 'X': '❌',
        'Y': '💛', 'Z': '🦄',

        '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
        '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣'
    }

    emoji_text = ''

    for char in text.lower():
        # Use the emoji from the dictionary if available, else keep the original character
        emoji_text += emoji_dict.get(char, char)

    return emoji_text

if __name__ == "__main__":
    user_input = input("Enter text to convert to emojis: ")
    emoji_result = text_to_emoji_converter(user_input)
    print("Converted text:")
    print(emoji_result)


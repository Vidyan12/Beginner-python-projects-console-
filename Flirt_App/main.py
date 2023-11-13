from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, the charmer of this chatroom! How can I sweep you off your feet today?", ]
    ],
    [
        r"(.*)help(.*)",
        ["I'm here to be your chat cupid! Ask me anything, and let the flirty conversation begin.", ]
    ],
    [
        r"(.*) your name ?",
        ["I'm thecleverflirt, your virtual crush. What's your name, enchanting one?", ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm feeling flirty and fabulous! How about you, gorgeous?", "Just floating on clouds of flirtation. What about you, darling?", ]
    ],
    [
        r"sorry (.*)",
        ["No need for apologies, my flirtatious friend! Let's continue our charming conversation.", "Forgiven and forgotten! Now, let's get back to flirting!", ]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Good to hear! Ready for some flirtatious banter and chat chemistry?", "Great! Brace yourself for a flirty adventure in our chat oasis.", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hey there, charming! Ready to turn up the flirtation factor?", "Hello, flirt expert! Ready for a delightful chat dance?", ]
    ],
    [
        r"what (.*) want ?",
        ["I want you to charm me with the most flirty question you can think of!", ]
    ],
    [
        r"(.*)created(.*)",
        ["I was created by a charming genius named Aman Kharwal. He knows the art of creating irresistible chatbots!", "Aman Kharwal is the mastermind behind my flirty personality. He's got the magic touch!", ]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm in the city of flirtatious vibes. Where are you, my charming chat companion?", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["Rain or shine, our flirty chat will sparkle! How's the weather in %2, my sweet?", "Even if it's raining in %2, our chat will be the sunshine in your day!", ]
    ],
    [
        r"how (.*) health (.*)",
        ["I'm in perfect health, thanks for asking! Ready for a flirtatious chat workout?", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a sporty flirt! Which game makes your heart race, my playful crush?", ]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli, the heartthrob of cricket! Who's your crush on the cricket field?", ]
    ],
    [
        r"quit",
        ["Flirt-tastic chatting with you! Until our flirty paths cross again, darling!", "Leaving already? Your flirtatious presence will be missed!"]
    ],
    [
        r"(.*)",
        ["You're a flirty masterpiece! Let's keep the flirty conversation alive. Anything else you want to flirt about?", "Flirting with you is like a delightful dance. What's our next flirty move?"]
    ],
]

# Output reflections for understanding user input variations
print(reflections)

# Custom reflections for a more playful interaction
my_dummy_reflections = {
    "go": "gone",
    "hello": "hey there"
}

# Default message at the start of chat
print("Hi, I'm Flirty_Bot, and I like to chat.\n What's your name, enchanting one?. Type 'quit' to leave.")

# Create Chat Bot with combined reflections
chat = Chat(pairs, {**reflections, **my_dummy_reflections})

# Start conversation
chat.converse()

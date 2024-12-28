import re

text = "The quick brown fox jumps over the lazy brown dog"

dog = r"brown"

dogColour = "white"

newtext = re.sub(dog, dogColour, text)

print("The old string:{}\nThe new string:{}".format(text, newtext))


phrase = """
Beneath the twilight's fading light,
Dreams awaken in the soft light.
The stars whisper their endless light,
Guiding lost souls toward the light.
Winds carry tales of shimmering light,
Through the trees that glow with light.
Time moves gently, bathed in light,
Moments fleeting, but filled with light.
In the darkness, hearts find light,
Chasing forever the radiant light.
"""

lastword = r"light"
newlastword = "dark"

newPhrase = re.sub(lastword, newlastword, phrase)

print("The new phrase is : {}".format(newPhrase))

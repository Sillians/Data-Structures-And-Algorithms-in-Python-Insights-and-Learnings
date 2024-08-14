import re

def removePunctuationRegexVersion(string: str) -> str:
    return re.sub("[^a-zA-Z0-9 ]", "", string)


print(removePunctuationRegexVersion("This isn't a test about life and death."))
print(removePunctuationRegexVersion(
    "But, it is a test about whether you have a chance to succeed in your life!"))
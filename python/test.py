# string is empty
pattern = ""
text = "abc"
if not pattern:
    print(True);
else:
    print(False);

# fancy value
# if string is empty then it's False
true_or_not = bool(pattern)
print(true_or_not)

first_match = bool(text) and pattern[0] in {text[0], '.'}
print(first_match)


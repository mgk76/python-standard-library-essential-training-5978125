# Use standard library functions to search strings for content


sampleStr = "The quick brown fox jumps over the lazy dog"

# TODO: startsWith and endsWith functions
print(sampleStr.startswith("The"))
print(sampleStr.endswith("dog"))

# TODO: the find and rfind functions
print()
print(sampleStr.find("the"))
print(sampleStr.rfind("the"))
print("the" in sampleStr)


# TODO: using replace
print()
newstr = sampleStr.replace("lazy", "tired")
print(newstr)

# TODO: counting instances of substrings
print()
print(sampleStr.count("over"))

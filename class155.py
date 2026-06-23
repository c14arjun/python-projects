word=input("Enter a word: ")
for ch in word:
    if ch in "aeiouAEIOU":
        print("First vowel found:",ch)
        break
    else:
        print("Not a vowel:",ch)
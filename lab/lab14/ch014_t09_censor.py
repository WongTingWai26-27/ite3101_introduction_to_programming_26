def censor(text, word):
    words = text.split()
    result = []
    stars = "*" * len(word)
    
    for w in words:
        if w == word:
            result.append(stars)
        else:
            result.append(w)
            
    return " ".join(result)

# Example test
print(censor("this hack is wack hack", "hack"))

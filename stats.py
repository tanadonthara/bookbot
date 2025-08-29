def count_words(text):
    return len(text.split())

def get_char_counts(text):
    counts = {}
    for ch in text.lower():
        if ch in counts:
    	    counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def get_sorted_char_counts(counts):
    items = []
    for ch in counts:
        if ch.isalpha():              # skip non-letters
            items.append({"char": ch, "num": counts[ch]})

    def sort_on(d):
        return d["num"]

    items.sort(key=sort_on, reverse=True)  # greatest to least
    return items

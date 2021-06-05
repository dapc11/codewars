def to_jaden_case(string):
    results = []
    for word in string.split(' '):
        word = word[0].upper() + word[1:]
        results.append(word)

    return ' '.join(results)


QUOTE = "How can mirrors be real if our eyes aren't real"
assert (
    to_jaden_case(QUOTE) == "How Can MIrrors Be Real If Our Eyes Aren't Real")

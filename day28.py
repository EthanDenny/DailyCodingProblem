"""

Given:
- A list of words
- The start index (inclusive) of the line in the list
- The end index (inclusive) of the line in the list
- The number of spaces to be distributed

Spreads the spaces evenly between words, and adds a
bonus space to the first N words where
N = number of spaces % number of gaps between words

Concatenates all the words & spaces and returns the
result

"""
def convert_to_line(words, start, end, spaces):
    seps = end - start

    i = 0
    line = ""
    while i < seps:
        line += words[start + i]
        line += ' ' * (spaces // seps)
        if i < spaces % seps: line += ' '
        i += 1
    
    return line + words[end]


def f(words, line_len):
    lines = []
    count = 0 # Length of current line
    i = 0 # End of slice index
    j = 0 # Start of slice index

    def add_line():
        spaces = line_len - count + i - j # Spaces to be distributed
        line = convert_to_line(words, start=j, end=i-1, spaces=spaces)
        lines.append(line)

    while i < len(words):
        if count + len(words[i]) > line_len:
            add_line()
            count = 0
            j = i
        else:
            count += len(words[i]) + 1
            i += 1

    add_line()

    return lines


if __name__ == '__main__':
    words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    assert f(words, 16) == ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']

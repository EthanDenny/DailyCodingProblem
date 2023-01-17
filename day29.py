def encode(string):
    count = 1
    ch = string[0]
    output = ''

    for i in range(1, len(string)):
        if string[i] == ch:
            count += 1
        else:
            output += str(count) + ch
            ch = string[i]
            count = 1
    output += str(count) + ch
    
    return output


def decode(string):
    output = ''

    for i in range(0, len(string), 2):
        output += string[i+1] * int(string[i])
    
    return output


if __name__ == '__main__':
    assert encode('AAAABBBCCDAA') == '4A3B2C1D2A'
    assert decode('4A3B2C1D2A') == 'AAAABBBCCDAA'

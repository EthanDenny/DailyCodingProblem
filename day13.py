def f(k, s):
    if k <= 1:
        return k
    else:
        long_cand_len = 0

        cand = ''
        char_counts = {}

        for c in s:
            cand += c
            if not c in char_counts:
                char_counts[c] = 1
            if len(char_counts) > k:
                if len(cand) - 1 > long_cand_len:
                    long_cand_len = len(cand) - 1
                while len(char_counts) > k:
                    ch = cand[0]
                    char_counts[ch] -= 1
                    cand = cand[1:]
                    if char_counts[ch] == 0:
                        char_counts.pop(ch)
        
        return long_cand_len


if __name__ == "__main__":
    assert f(2, 'abcba') == 3

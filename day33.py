def f(seq):
    sort_seq = []

    for elem in seq:
        # Insert the given element in the sorted list

        i = 0

        while i < len(sort_seq) and elem > sort_seq[i]:
            i += 1

        sort_seq.insert(i, elem)
        
        # Find the median

        count = len(sort_seq)
        
        median = sort_seq[count // 2]
        
        if count % 2 == 0:
            median += sort_seq[count // 2 - 1]

            # Pretty division; removes unnecessary floats
            if median % 2 == 0: median //= 2
            else: median /= 2
        
        print(median)
            

if __name__ == '__main__':
    """
    Should print:
    2
    1.5
    2
    3.5
    2
    2
    2
    """
    f([2, 1, 5, 7, 2, 0, 5])

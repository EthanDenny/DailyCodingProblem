def longest_path(f):
    # Strip parent directory
    parent_dir_len = f.find('\n')+1
    f = f[parent_dir_len:]
    
    start = 0
    end = 1
    max_sub_len = 0

    def handle(start, end):
        dir = f[start:end]
        dir = dir.replace('\n\t', '\n')
        if '\n' in dir:
            return longest_path(dir)
        elif '.' in dir:
            return len(dir)
        else:
            return 0

    while end < len(f):
        if f[end-1] == '\n' and f[end+1] != '\t':
            subdir_len = handle(start+1, end-1)
            max_sub_len = max(subdir_len, max_sub_len)
            start = end
        end += 1
        if end == len(f):
            subdir_len = handle(start+1, end)
            max_sub_len = max(subdir_len, max_sub_len)
    
    return parent_dir_len + max_sub_len


if __name__ == "__main__":
    file_system = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    assert longest_path(file_system) == 32

def flatten(tall_dict: dict) -> dict:
    flat_dict: dict = {}

    for k, v in tall_dict.items():
        if type(v) is dict:
            for sub_k, sub_v in flatten(v).items():
                flat_dict[k + '.' + sub_k] = sub_v
        else:
            flat_dict[k] = v
    
    return flat_dict

if __name__ == '__main__':
    test_dict: dict = {
        'key': 3,
        'foo': {
            'a': 5,
            'bar': {
                'baz': 8
            }
        }
    }
    
    flat_dict: dict = flatten(test_dict)
    
    assert(flat_dict['key'] == 3)
    assert(flat_dict['foo.a'] == 5)
    assert(flat_dict['foo.bar.baz'] == 8)

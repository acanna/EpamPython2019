import inspect


def letters_range(*args, **kwargs):
    if not args:
        raise TypeError('letters_range expected at least 1 agruments, got 0')
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    indexes = dict([(x, i) for i, x in enumerate(letters)])
    result = None
    if len(args) == 1:
        result = letters[:indexes[args[0]]]
    elif len(args) == 2:
        result = letters[indexes[args[0]]:indexes[args[1]]]
    elif len(args) == 3:
        result = letters[indexes[args[0]]:indexes[args[1]]:args[2]]
    if kwargs:
        for i, x in enumerate(result):
            if x in kwargs:
                result[i] = str(kwargs[x])
    return result


assert letters_range('b', 'w', 2) == ['b', 'd', 'f', 'h', 'j', 'l',
                                      'n', 'p', 'r', 't', 'v']
assert letters_range('g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert letters_range('g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert letters_range('g', 'p', **{'l': 7, 'o': 0}) == ['g', 'h', 'i', 'j', 'k',
                                                       '7', 'm', 'n', '0']
assert letters_range('p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
assert letters_range('a') == []


def atom(value=None):
    def get_value():
        return value

    def set_value(new_value):
        nonlocal value
        value = new_value
        return value

    def process_value(*funcs):
        nonlocal value
        for func in funcs:
            value = func(value)
        return value

    def delete_value():
        nonlocal value
        value = None

    return get_value, set_value, process_value, delete_value


def make_it_count(func, counter_name):
    def inner(*args, **kwargs):
        globals()[counter_name] += 1
        return func(*args, **kwargs)

    return inner


def modified_func(func, *fixated_args, **fixated_kwargs):
    def inner(*args, **kwargs):
        nonlocal fixated_args
        fixated_args_ = fixated_args + args
        fixated_kwargs_ = fixated_kwargs.copy()
        fixated_kwargs_.update(kwargs)
        print(fixated_args_, fixated_kwargs_)
        return func(*fixated_args_, **fixated_kwargs_)

    inner.__name__ = f'func_{func.__name__}'
    doc = f'\nA func implementation of {func.__name__}\n' \
        f'with pre-applied arguments being:\n'
    doc += f'{", ".join(map(str, fixated_args))},\n' if fixated_args else ''
    doc += f'{str(fixated_kwargs)[1:-1]}\n' if fixated_kwargs else ''
    doc += f'source_code:\n{inspect.getsource(func)}'
    inner.__doc__ = doc
    return inner

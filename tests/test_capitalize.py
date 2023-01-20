from pack_funk.capitalize import capitalize


if capitalize('hello!') != 'Hello!':
    raise Exception('The function does not work properly.')

if capitalize('') != '':
    raise Exception('The function does not work properly.')

print('All tests passed successfully.')
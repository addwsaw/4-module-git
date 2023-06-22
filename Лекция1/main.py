def func(str):
    revstr = str[::-1]
    if str != revstr:
        return False
    else:
        return True


print(func('tenet'))
print(func('helloworld'))
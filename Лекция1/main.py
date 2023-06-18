def func(str):
    liststr = list(str)
    revstr = liststr[::-1]
    if liststr != revstr:
        return False
    else:
        return True


print(func('tenet'))
print(func('helloworld'))
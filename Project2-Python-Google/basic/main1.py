
list1 = ['aa', 'ee', 'xx', 'zz']
list2 = ['bb', 'cc', 'yy']


def process(list_a, list_b):
    list_a = sorted(list_a, reverse=False)
    list_b = sorted(list_b, reverse=False)
    result = []
    while len(list_a) and len(list_b):

        if list_a[0] < list_b[0]:
            result.append(list_a.pop(0))
        else:
            result.append(list_b.pop(0))

    result.extend(list_a)
    result.extend(list_b)
    return result


def main():
    print process(list1,list2)






if __name__ == '__main__':
    main()


list1 = ['aa', 'xx', 'zz']
list2 = ['bb', 'cc']


def process(list_a, list_b):
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

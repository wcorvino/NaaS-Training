
def swap(x, y, n):
    z = x[n]
    x = y[n]
    y = z[0]


def main():
    list1 = ['aa', 'xx', 'zz']
    list2 = ['bb', 'cc']
    list_a = list1+list2
    list_n = []

    swap(list_n, list_a, 0)


if __name__ == '__main__':
    main()

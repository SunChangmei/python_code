def get_height(route):
    start = route[0]
    res = 0
    for i in range(len(route)):
        if i == len(route)-1 or route[i+1] < route[i]:
            height = route[i]-start
            res = res if res > height else height
            start = route[i+1] if i != (len(route)-1) else start
    return res


def main():
    while True:
        try:
            num = input()
            if not (num and 1 <= int(num) <= 1000):
                return
            num = int(num)
            route = input().split()
            if len(route) != num:
                return
            route = [int(item) for item in route]
            res = get_height(route)
            print(res)
        except EOFError:
            break


if __name__ == '__main__':
    main()
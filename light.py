def add_light(front, next):
    pass


def main():
    street = int(input())
    light_num = int(input())
    light_limit = int(input())
    if not (1 <= street <= 1000 and 1 <= light_num <= street and 0 <= light_limit <= street):
        return
    light_list = []
    for i in range(light_num):
        light = int(input())
        if len(light_list) != 0 and light <= light_list[i - 1]:
            return
        light_list.append(light)

    for i in range(len(light_list)):
        if i == 0 and light_list[0] - light_limit <= 0:
            continue
        elif i < len(light_list) - 1:
            if light_list[i] - light_limit <= light_list[i - 1] + light_limit:
                if light_list[i] + light_limit <= light_list[i + 1] - light_limit:
                    add_light(light_list[i], light_list[i + 1])
            add_light(light_list[i - 1], light_list[i])
        else:
            if light_list[i] - light_limit <= light_list[i - 1] + light_limit:
                return 0


if __name__ == '__main__':
    res = main()
    print(res)

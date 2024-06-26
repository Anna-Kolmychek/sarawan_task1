import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', type=int)
    return parser


def request_num():
    num = ''
    while not is_correct_num(num):
        num = input('Введите целое положительное число: ')
    return num


def is_correct_num(num):
    if not num.isdigit():
        return False
    if int(num) <= 0:
        return False
    return True


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    if not args.num:
        num = request_num()
    elif args.num <= 0:
        num = request_num()
    else:
        num = args.num

    print('Искомая последовательность:')
    print(''.join([str(n) * n for n in range(1, int(num) + 1)]))

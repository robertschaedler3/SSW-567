import sys

if __name__ == '__main__':
    if 1 == len(sys.argv):
        print('Hello, world!')
    else:
        print(f'Hello, {" ".join(sys.argv[1:])}!')

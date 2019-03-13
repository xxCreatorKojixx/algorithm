#スタック & キュー

#デバッガで動かしながらxの様子をみてください

def main():
    stack()
    queue()

def stack():

    x = ["a","b","c"]

    print(x)
    print("pop:",x.pop())
    print("pop:",x.pop())
    print("pop:",x.pop())


def queue():

    x = ["a","b","c"]

    print(x)
    print("pop:",x.pop(0))
    print("pop:",x.pop(0))
    print("pop:",x.pop(0))

if __name__ == "__main__":
    main()
#クイックソート

#https://qiita.com/muiscript/items/257e8b9b49d891137d56


def main():

    data = [7,1,5,9,6,2,3,4,8]

    print(quick(data))


def quick(data):

    if len(data) in (0,1):
        return data

    pivot = data[-1]
    
    #この記述方法を「リスト内包表記」と言います
    left = [x for x in data[:-1] if x <= pivot]
    right = [x for x in data[:-1] if x > pivot]

    return quick(left) + [pivot] + quick(right)


if __name__ == "__main__":
    main()
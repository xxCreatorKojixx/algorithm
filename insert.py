#挿入ソート

#https://qiita.com/muiscript/items/257e8b9b49d891137d56

def main():

    data = [7,1,2,6,4,8,5,9,3]

    print(insert(data))


def insert(data):

    for i in range(1,len(data)):
        for j in range(i,0,-1):
            if data[j] >= data[j-1]:
                break
            else:
                #変数内の入れ替え
                data[j],data[j-1] = data[j-1],data[j]

    return data


if __name__ == "__main__":
    main()
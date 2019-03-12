
#セレクトソート

#参考URL
#https://qiita.com/muiscript/items/257e8b9b49d891137d56

def main():
    
    data = [5,3,9,1,7,4,2,6,8]

    print(selection(data))

    return


def selection(data):
    
    for i in range(len(data) -1):

        #並べられていない範囲のリストの
        #最小値のインデックス番号をとってくる
        minindex = data[i:].index(min(data[i:]))

        #data[i]と#data[i+minindex]を入れかえる
        data[i] , data[i+minindex] = data[i+minindex] , data[i]

    return data

if __name__ =="__main__":
    main()
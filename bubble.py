



def main():
    data = [3,5,2,1,4,6,8,9,7]

    print("デバッグが動きます")
    x = range(len(data))
    print("デバッグ")

    result = bubble(data)

    print(result)
    return 

def bubble(data):

    for i in range(len(data)):#0~9
        for j in range(len(data)-1,i,-1):
            if data[j] < data[j-1]:
                data[j],data[j-1] = data[j-1], data[j]
                
    return data


if __name__ == "__main__":
    main()
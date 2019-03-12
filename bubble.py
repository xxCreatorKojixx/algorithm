#
#写経用バブルソートアルゴリズムです
#

def main():

    data = [3,5,2,1,4,6,8,9,7]

    result = bubble(data)

    print(result)

    return 

def bubble(data):
    #昇順に数字を並べ替えます
    
    for i in range(len(data)):#0~9
        for j in range(len(data)-1,i,-1):
            if data[j] < data[j-1]:
                data[j],data[j-1] = data[j-1], data[j]
                
    return data


if __name__ == "__main__":
    main()
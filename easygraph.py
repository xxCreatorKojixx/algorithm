#easy graph

# 参考URL
# https://qiita.com/y__sama/items/a2c458de97c4aa5a98e7

def main():

    data = [4,2,8,6,3]
    graph = easygraph(data)

    for i in range(len(data)):
        print(str(data[i])+":"+graph[i])

    return


def easygraph(data):

    graph = ["*" * data[i] for i in range(len(data))]

    return graph


if __name__ == "__main__":
    main()

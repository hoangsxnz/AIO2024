def find_max(num_list: list, k: int) -> list[int]:
    res = []
    for i in range(len(num_list)-k+1):
        print(num_list[i:i+k])
        res.append(max(num_list[i:i+k]))

    return res


if __name__ == "__main__":
    num_list = [6, 5, 4, 3, 2, 1]
    k = 3
    print(find_max(num_list, k))

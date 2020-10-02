if __name__ == '__main__':
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in records:
            records[score].append(name)
        else:
            records[score] = [name]
    new = sorted(records.keys())
    print(*sorted(records[new[1]]), sep='\n')

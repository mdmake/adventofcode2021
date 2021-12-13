def foldVertical(coordinates, x):
    for i, item in enumerate(coordinates):
        if item[0] > x:
            coordinates[i] = [x - abs(x - item[0]), item[1]]
    return coordinates

def foldHorisontal(coordinates, y):
    for i, item in enumerate(coordinates):
        if item[1] > y:
            coordinates[i] = [item[0], y - abs(y-item[1])]
    return coordinates


def readData(filename):
    coordinates = []
    folds = []
    beginFolds = False
    with open(filename) as file:
        for row in file:
            if row.strip() == "":
                beginFolds = True
                continue
            if not beginFolds:
                coordinates.append([int(item) for item in row.strip().split(',')])
            else:
                fold = row.strip().replace('fold along ','').split('=')
                folds.append([fold[0], int(fold[1])])


    return coordinates, folds

if __name__ == "__main__":
    data, folds = readData('day13data.txt')

    for axe, fold in folds:
        if axe == 'x':
            data = foldVertical(data, fold)
        else:
            data = foldHorisontal(data, fold)

    newData = {tuple(item) for item in data}
    x_max = max(newData, key=lambda d: d[0])[0]
    y_max = max(newData, key=lambda d: d[1])[1]

    for y in range(y_max+1):
        for x in range(x_max+1):
            if (x, y) in newData:
                print('#', end='')
            else:
                print(' ', end='')
        print()



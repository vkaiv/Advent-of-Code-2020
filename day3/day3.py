def checkForTrees(lines, xSpeed, ySpeed):
    treeEncounters = 0
    x = 0
    y = 0
    while y < len(lines):
        if x + 3 > len(lines[y]):
            x -= len(lines[y])
        if lines[y][x] == '#': treeEncounters += 1
        x += xSpeed
        y += ySpeed
    return treeEncounters

def main():
    with open('input.txt', 'r') as fh:
        lines =  fh.readlines()

    lines = [i.strip() for i in lines]
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    product = 1 
    for i in slopes:
        trees = checkForTrees(lines, *i)
        product *= trees
        print(f'The number of tree encounters is: {trees}')

    print(f'The tree encounters multiplied together is: {product}')
    
if __name__ == '__main__':
    main()
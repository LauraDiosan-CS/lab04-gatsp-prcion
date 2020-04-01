from GA import GA

def read_file(file):
    all = {}
    f = open(file, "r")
    n = int(f.readline())
    all['noNodes'] = n
    matrix = []
    for _ in range(n):
        line = f.readline()
        lineValues = line.split(',')
        lineList = []
        for value in lineValues:
            lineList.append(int(value))
        matrix.append(lineList)
    all['matrix'] = matrix
    return all

def function(matrix, chr):
    val = 0
    for i in range(0, len(chr) - 1):
        val = val + matrix[chr[i] - 1][chr[i + 1] - 1]
    val = val + matrix[chr[len(chr) - 1] - 1][chr[0] - 1]
    return val

def main():
    net = read_file("easy_03_tsp.txt")
    # net = read_file("medium_01_tsp.txt")
    # net = read_file("hard_01_tsp.txt")

    gaParam = {'popSize':100, 'noGen' : 500, 'pc' : 1.8, 'pm' : 1.1}
    problParam = {'net': net, 'function': function, 'noNodes':net['noNodes']}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    for i in range(0, gaParam['noGen']):
        ga.oneGenerationElitism()
        print(ga.bestChromosome())

main()

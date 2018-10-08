import csv

data = []
nombreArchivo = "clientes"

def getCombinations():
    numerico = "numeric"
    booleano = "{'0', '1'}"

    return [numerico, booleano, numerico, booleano, booleano, booleano, booleano, booleano, booleano,
            numerico, booleano, booleano, booleano, booleano, booleano, booleano, booleano, booleano]

def convertArff():
    with open( nombreArchivo + '.csv', 'r', encoding="utf8") as csvfile:
        fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in fileReader:
            data.append(row)

    with open( nombreArchivo + '.arff', 'w') as file:
        attributes = data[0]
        file.write("@relation " + nombreArchivo + "\n")
        combinaciones = getCombinations()
        i = 0
        for attribute in attributes:
            file.write("@attribute '" + attribute + "' " + combinaciones[i] + "\n")
            i = i + 1
        file.write("@data\n")
        for row in data[1:]:
            for dato in row:
                file.write(dato + ",")
            file.write("\n")
        file.close()

convertArff()

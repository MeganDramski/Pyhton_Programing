import sys
import csv


def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        sales = sys.argv[1]
        master = sys.argv[2]
        output = sys.argv[3]
        price = []
        lotSize = []
        quantity = []
        productId = []
        name = []
        TotalUnits = []
        GrossRevenue = []

          
        with open(master) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                name.append(row[1])
                price.append(float(row[2]))
                lotSize.append(float(row[3]))

        with open(sales) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                sales = list(map(int, row))
                productId.append(int(sales[2]))
                quantity.append(int(sales[3]))


        for i in range(len(lotSize)):
            TotalUnits.append(lotSize[i] * quantity[i])

        for i in range(len(TotalUnits)):
            GrossRevenue.append(price[i] * TotalUnits[i])

        with open(output, mode='w') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(TotalUnits)):
                writer.writerow([name[i], TotalUnits[i], GrossRevenue[i]])

        return name, TotalUnits, GrossRevenue


if __name__ == '__main__':
    print('Main: ', main())

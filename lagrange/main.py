# print sqrt
# add data input

from polynomials import Polynomials
from getData import GetData

def main():
    data_raw = GetData.getData(GetData)
    p = Polynomials(data_raw)
    best = p.find_best()
    print(best)
    best.report.save()

if __name__ == "__main__":
    main()

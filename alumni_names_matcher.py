import xlrd

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def loadFromExcel(excelFile):
    allRows = []
    book = xlrd.open_workbook(excelFile)
    for sheet in book.sheets():
        for row in range(sheet.nrows):
            allRows.append(sheet.row(row))

    return allRows

def nameMatch(alumniNames, muslimNames):
    matches = []
    for row in alumniNames:
        if (binarySearch(muslimNames, row[1].value.split(' ')[0])):
            matches.append(row)
        """for colidx, cell in enumerate(row):
            if colidx == 1:
                for name in muslimNames:
                    firstName = cell.value.split(" ")[0]
                    if(firstName == name):
                        #print row
                        matches.append(row)"""

    return matches

with open('names.txt') as f:
    content = f.readlines()

muslimNames = sorted([x.strip('\n') for x in content])

alumniNames = loadFromExcel('ubisoc 2010_2016_Final.xlsx')
matches = nameMatch(alumniNames, muslimNames)
print matches
print len(matches)

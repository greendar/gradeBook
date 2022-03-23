class Course:
    def __init__(self, name):
        self.name = name
        self.oe = self.getOEs()

    def __str__(self):
        stringOut = f'{self.name}\n\n'
        for item in self.oe:
            stringOut += item
            stringOut += '\n'
        return stringOut

    def fileOut(self):
        stringOut = f'{self.name},'
        for item in self.oe:
            stringOut += item
            stringOut += ','
        return stringOut

    def getOEs(self):
        oes = []
        d = 0
        e = 0
        a = int(input('How many in strand A?\n: '))
        b = int(input('How many in strand B?\n: '))
        c = int(input('How many in strand C?\n: '))
        d = int(input('How many in strand D?\n: '))
        if d != 0:
            e = int(input('How many in strand E?\n: '))
            if e != 0:
                f = int(input('How many in strand F?\n: '))
        for i in range(a):
            oes.append('A' + str(i + 1))
        for i in range(b):
            oes.append('B' + str(i + 1))
        for i in range(c):
            oes.append('C' + str(i + 1))
        for i in range(d):
            oes.append('D' + str(i + 1))
        if d != 0:
            for i in range(e):
                oes.append('E' + str(i + 1))
        if e != 0:
            for i in range(f):
                oes.append('F' + str(i + 1))
        return oes

class Assessment:
    def __init__(self, oe, maxMark, course, mark=None):
        self.oe = oe
        self.maxMark = maxMark
        self.course = course
        self.mark = mark

    def __str__(self):
        return f'{self.oe} {self.mark}'

class Student:
    def __init__(self, fName, lName = ''):
        self.fName = fName
        self.lName = lName
        self.course = []
        self.evals = []

class SchoolClass:
    def __init__(self, courseCode, year):
        self.courseCode = courseCode
        self.year = year
        self.longestName = 0
        self.classList = self.getClassList()

    def createEval(self):
        print(f'Create Evaluation: {self.courseCode} - {self.year}')
        print('Enter Overall Expectation')
        getOE = input(': ')
        print('Enter the maximum number of marks')
        getMax = int(input(': '))
        for student in self.classList:
            student.evals.append(Assessment(getOE, getMax, self.courseCode))

    def getClassList(self):
        listOut = []
        fileInName = input('Please enter the filename to use.\n: ')
        f = open(fileInName, 'r')
        for name in f:
            a = Student(name.strip('\n'), self.courseCode)
            if len(a.fName) > self.longestName:
                self.longestName = len(a.fName)
            listOut.append(a)
        return listOut

    def sortClassList(self):
        tempList = []
        for student in self.classList:
            tempList.append(student.fName)
        tempList.sort()
        for name in tempList:
            print(name)

    def numberList(self):
        i = 1
        for name in self.classList:
            print(f'{(2 - len(str(i))) * " "}{i}.  {name.fName}')
            i += 1

    def __str__(self):
        stringOut = self.courseCode + '  ' + str(self.year) + '\n\n'
        for name in self.classList:
            stringOut += name.fName
        return stringOut

if __name__ == '__main__':
    a = SchoolClass('MCV4U', 2122)
    a.createEval()
    for student in a.classList:
        print(f'{student.fName}{(a.longestName + 2 - len(student.fName)) * " "}', end='')
        for assessment in  student.evals:
            print(assessment)

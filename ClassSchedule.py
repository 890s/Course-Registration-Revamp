class ClassSchedule:
    def __init__(self, math, sci, engl, ss, elec1, elec2):
        self.math = math
        self.sci = sci
        self.engl = engl
        self.ss = ss
        self.elec1 = elec1
        self.elec2 = elec2

    def setSchedule(self, math=None, sci=None, engl=None, ss=None, elec1=None, elec2=None):
        if math != None:
            self.math = math
        if sci != None:
            self.sci = sci
        if engl != None:
            self.engl = engl
        if ss != None:
            self.ss = ss
        if elec1 != None:
            self.elec1 = elec1
        if elec2 != None:
            self.elec2 = elec2

    def __str__(self):
        return f"Math: {self.math[0]} \nScience: {self.sci[0]}\nELA: {self.engl[0]}\nSocial Studies: {self.ss[0]}\nElective 1: {self.elec1[0]}\nElective 2: {self.elec2[0]}"

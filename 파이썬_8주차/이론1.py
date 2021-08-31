students = [
    {"이름": '송강호', 'korean':97, "math":91, "english": 96, "science":82},
    {"이름": '아이유', 'korean':95, "math":90, "english": 92, "science":86},
    {"이름": '송중기', 'korean':100, "math":88, "english": 94, "science":90},
    {"이름": '김태리', 'korean':93, "math":87, "english": 98, "science":94},
    {"이름": '송강', 'korean':87, "math":82, "english": 96, "science":98},
]

class Student :
    def __init__(self,name, korean, math, english, science ):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    
student = [
    Student("송강호", 98, 97, 96, 99),
    Student("아이유", 96, 100, 91, 95),
    Student("송중기", 95, 77, 66, 92),
    Student("김태리", 92, 87, 96, 95),
    Student("송강", 95, 97, 91, 93),
]

def getsum(self):
        return self.korean + self.math + self.english + self.science

def average(self):
        return "{:2f}".format(self.get_sum() / 4)

print(f"{student.name} 총점: {student.get_sum()} 평균: {student.average()}")

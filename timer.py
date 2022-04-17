from typing import List

class ZTime:
    def __init__(self, h: int=0, m: int=0, s: int=0):
        self.set(h, m, s)

    def set(self, h, m, s):
        self._hours = h
        self._minutes = m
        self._seconds = s

    def __str__(self) -> str:
        return '{:02d}:{:02d}:{:02d}'.format(self._hours, self._minutes, self._seconds)

    def get_full_sec(self) -> int:
        return self._seconds + self._minutes * 60 + self._hours * 3600
        
    # getters

    @property
    def hours(self) -> int: return self._hours
    
    @property
    def minutes(self) -> int: return self._minutes

    @property
    def seconds(self) -> int: return self._seconds

    # setters

    @hours.setter
    def hours(self, value: int) -> None:
        self._hours = value

    @minutes.setter
    def minutes(self, value: int) -> None: 
        if 0 < value > 60:
            self.hours += value//60
        self._minutes = value%60

    @seconds.setter
    def seconds(self, value: int) -> None: 
        if 0 < value > 60:
            self.minutes += value//60
        self.seconds =  value%60


class Student:
    def __init__(self, time: ZTime='', name: str=''):
        self._time = time
        self._name = name

    # getters

    @property
    def time(self) -> ZTime: return self._time
    
    @property
    def name(self) -> str: return self._name

    # setters

    @time.setter
    def time(self, value: ZTime) -> None: self._time = value

    @name.setter
    def name(self, value: str) -> None: self._name = value


def print_times(students: List[Student]):
    students = sorted(students, key=lambda student: student.time.get_full_sec())
    print('Место\tВремя     \tИмя')
    for i,student in enumerate(students):
        print('{}\t{}\t{}'.format(i+1, student.time, student.name))

times = [ 
    Student(ZTime(23, 12, 1), 'heisenberg'),
    Student(ZTime(5, 30, 1), 'sosig'),
    Student(ZTime(7, 46, 1), 'sos'),
    Student(ZTime(34, 10, 1), 'sis'),
]
print_times(times)
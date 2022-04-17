from typing import List

class ZDate:
    def __init__(self, d: int=1, m: int=1, y: int=0):
        self.set(d, m, y)

    def set(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def __str__(self) -> str:
        return '{:02d}.{:02d}.{}'.format(self._day, self._month, self._year)
        
    # getters

    @property
    def day(self) -> int: return self._day
    
    @property
    def month(self) -> int: return self._month

    @property
    def year(self) -> int: return self._year

    # setters

    @day.setter
    def day(self, value: int) -> None:
        if 1 < value > 31:
            raise Exception('bad day number')
        self._day = value

    @month.setter
    def month(self, value: int) -> None: 
        if 1 < value > 12:
            raise Exception('bad month number')
        self._month = value

    @year.setter
    def year(self, value: int) -> None: 
        self._year = value

class Session:
    def __init__(self, date: ZDate='', teacher: str='', group: str='', discipline: str=''):
        self._date = date
        self._teacher = teacher
        self._group = group
        self._discipline = discipline

    # getters

    @property
    def date(self) -> ZDate: return self._date
    
    @property
    def teacher(self) -> str: return self._teacher

    @property
    def group(self) -> str: return self._group

    @property
    def discipline(self) -> str: return self._discipline

    # setters

    @date.setter
    def date(self, value: ZDate) -> None: self._date = value

    @teacher.setter
    def teacher(self, value: str) -> None: self._teacher = value

    @group.setter
    def group(self, value: str) -> None: self._group = value

    @discipline.setter
    def discipline(self, value: str) -> None: self._discipline = value


def print_shedule(shedule: List[Session]):
    print('Дата\tПреподаватель\tГруппа\tДисциплина')
    for session in shedule:
        print('{}\t{}\t{}\t{}'.format(session.date, session.teacher, session.group, session.discipline))

shedule = [ 
    Session(ZDate(1, 12, 2022), 'sosok', 'G1-2', 'Прога'),
    Session(ZDate(1, 12, 2022), 'sosig', 'Р1-2', 'Дизайн'),
    Session(ZDate(1, 12, 2022), 'sos', 'П1-2', 'Жрок'),
    Session(ZDate(1, 12, 2022), 'sis', 'T1-2', 'Прога'),
]
print_shedule(shedule)
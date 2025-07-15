from dataclasses import dataclass
from enum import Enum
import random

class ScheduleType(Enum):
    TWO_BY_TWO = "2/2"
    FIVE_BY_TWO = "5/2"

class FunctionalType(Enum):
    SUPPORT = "Поддержка"
    REQUESTS = "Обработка заявок"
    MAIL = "Почта и документы"

def str_to_minutes(time_str: str) -> int:
    hh, mm = map(int, time_str.split(":"))
    return hh * 60 + mm

def minutes_to_str(minutes: int) -> str:
    return f"{minutes // 60:02d}:{minutes % 60:02d}"

@dataclass
class Break:
    start: str
    end: str
    duration: int
    is_lunch: bool

@dataclass
class FunctionalAssignment:
    hour: str
    functional: FunctionalType

class Employee:
    def __init__(self, name: str, schedule_type: ScheduleType):
        self.name = name
        self.schedule_type = schedule_type
        self.breaks: list[Break] = []
        self.assignments: list[FunctionalAssignment] = []
        self.start_hour = random.randint(6, 10)
        self.work_duration = random.choice([9, 12])
        self.generate_breaks()

    def generate_breaks(self):
        start_minute = self.start_hour * 60
        end_minute = start_minute + self.work_duration * 60
        total_breaks = []

        if self.schedule_type == ScheduleType.TWO_BY_TWO:
            durations = [20, 30, 20, 30]
        else:
            durations = [10, 40, 10, 10, 10]

        placed_times = []
        for duration in durations:
            attempts = 0
            while attempts < 100:
                candidate = random.randint(start_minute + 60, end_minute - duration - 60)
                if all(abs(candidate - pt) >= 60 for pt in placed_times):
                    placed_times.append(candidate)
                    total_breaks.append(Break(
                        minutes_to_str(candidate),
                        minutes_to_str(candidate + duration),
                        duration,
                        duration >= 30
                    ))
                    break
                attempts += 1

        self.breaks = sorted(total_breaks, key=lambda b: str_to_minutes(b.start))

    def is_on_break(self, hour: str) -> bool:
        current_min = str_to_minutes(hour)
        for br in self.breaks:
            if str_to_minutes(br.start) <= current_min < str_to_minutes(br.end):
                return True
        return False

    def is_available(self, hour: str) -> bool:
        current_hour_min = str_to_minutes(hour)
        work_start_min = self.start_hour * 60
        work_end_min = work_start_min + self.work_duration * 60
        return work_start_min <= current_hour_min < work_end_min and not self.is_on_break(hour)

    def can_switch_functional(self, current_hour: str) -> bool:
        if not self.assignments:
            return True

        last_assignment = self.assignments[-1]
        current_min = str_to_minutes(current_hour)
        last_min = str_to_minutes(last_assignment.hour)
        min_interval = 180 if self.schedule_type == ScheduleType.TWO_BY_TWO else 120
        return (current_min - last_min) >= min_interval

    def assign_functional(self, hour: str, functional: FunctionalType):
        self.assignments.append(FunctionalAssignment(hour, functional))

class Functional:
    def __init__(self, functional_type: FunctionalType, min_employees: int):
        self.type = functional_type
        self.min_employees = min_employees
        self.assignments: dict[str, list[Employee]] = {}

    def add_assignment(self, hour: str, employee: Employee):
        if hour not in self.assignments:
            self.assignments[hour] = []
        self.assignments[hour].append(employee)

    def is_requirement_met(self, hour: str) -> bool:
        return len(self.assignments.get(hour, [])) >= self.min_employees

class Schedule:
    def __init__(self):
        self.hours = [f"{h:02d}:00" for h in range(6, 22)]
        self.functionals = {
            FunctionalType.SUPPORT: Functional(FunctionalType.SUPPORT, 2),
            FunctionalType.REQUESTS: Functional(FunctionalType.REQUESTS, 1),
            FunctionalType.MAIL: Functional(FunctionalType.MAIL, 1)
        }
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_available_employees(self, hour: str) -> list[Employee]:
        return [emp for emp in self.employees if emp.is_available(hour)]

    def print_schedule(self):
        for hour in self.hours:
            print(f"\n{hour}-{int(hour[:2]) + 1:02d}:00")
            on_break = [emp.name for emp in self.employees if emp.is_on_break(hour)]
            for functional in self.functionals.values():
                emps = functional.assignments.get(hour, [])
                if emps:
                    names = ', '.join(e.name for e in emps)
                    print(f"  {functional.type.value}: {names}")
            if on_break:
                print(f"  Перерывы: {', '.join(on_break)}")

class Distributor:
    def __init__(self, schedule: Schedule):
        self.schedule = schedule

    def distribute(self):
        for hour in self.schedule.hours:
            available_employees = self.schedule.get_available_employees(hour)
            random.shuffle(available_employees)
            for functional in self.schedule.functionals.values():
                needed = functional.min_employees - len(functional.assignments.get(hour, []))
                if needed <= 0:
                    continue
                for emp in available_employees[:]:
                    if emp.assignments and emp.assignments[-1].functional != functional.type:
                        if not emp.can_switch_functional(hour):
                            continue
                    functional.add_assignment(hour, emp)
                    emp.assign_functional(hour, functional.type)
                    available_employees.remove(emp)
                    needed -= 1
                    if needed <= 0:
                        break

def create_sample_schedule() -> Schedule:
    schedule = Schedule()
    employees_data = [
        ("Иванов", ScheduleType.TWO_BY_TWO),
        ("Петров", ScheduleType.TWO_BY_TWO),
        ("Смирнова", ScheduleType.FIVE_BY_TWO),
        ("Козлова", ScheduleType.FIVE_BY_TWO),
        ("Никитина", ScheduleType.FIVE_BY_TWO),
        ("Сидоров", ScheduleType.TWO_BY_TWO),
        ("Васильева", ScheduleType.FIVE_BY_TWO),
        ("Попов", ScheduleType.TWO_BY_TWO)
    ]
    for name, schedule_type in employees_data:
        schedule.add_employee(Employee(name, schedule_type))
    return schedule

def main():
    schedule = create_sample_schedule()
    distributor = Distributor(schedule)
    distributor.distribute()
    schedule.print_schedule()

if __name__ == "__main__":
    main()


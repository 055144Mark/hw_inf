class DaySchedule:
    def __init__(self):
        self.lessons = []

    def add_lesson(self, lesson_name):
        self.lessons.append(lesson_name)

    def __str__(self):
        return "\n".join(f"- {lesson}" for lesson in self.lessons) if self.lessons else "Уроков нет"

    def get_lessons(self):
        return self.lessons

class WeeklySchedule:
    def __init__(self):
        self.week_days = [DaySchedule() for _ in range(7)]

    def schedule_lesson(self, day_number, lesson_name):
        if 0 <= day_number < len(self.week_days):
            self.week_days[day_number].add_lesson(lesson_name)
        else:
            raise ValueError("Неправильный номер дня: допустимый диапазон 0-6")

    def get_day_schedule(self, day_number):
        if 0 <= day_number < len(self.week_days):
            return self.week_days[day_number]
        else:
            raise ValueError("Неправильный номер дня")

    def __iter__(self):
        return iter(self.week_days)

weekly_schedule = WeeklySchedule()
weekly_schedule.schedule_lesson(0, "Математика")
weekly_schedule.schedule_lesson(0, "Физика")
weekly_schedule.schedule_lesson(1, "Литература")

for day_num, day_schedule in enumerate(weekly_schedule, start=1):
    print(f"День {day_num}:")
    print(day_schedule)

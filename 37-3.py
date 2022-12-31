from datetime import datetime


class Meeting:
    def __init__(self, date: datetime, title: str):
        self.date = date
        self.title = title


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, date: datetime):
            return date not in self.meetings

    def add_meeting(self, meeting: Meeting):
        if self.is_available(meeting.date):
            self.meetings[meeting.date] = meeting

    def next_available_slot(self, date: datetime):
        meeting_date = date
        while not self.is_available(meeting_date):
            meeting_date =
        # stworznie zmiennej potencjalnej godzieny spotakania
        # while - dopoki potencjalana godzina nie jest wolna
        # dodawaj po jendaj godzienie do potencjalnej godzieny spotkania (timedelta)


def test_add_meeting():
    #given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), "Urodziny mam!")
    birthday2 = Meeting(datetime(2020, 11, 9, 12, 0), "Urodziny mam!")
    calendar = Calendar()
    #when
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)
    #then
    assert len(calendar.meetings) == 1

def test_add_two_meeting():
    #given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), "Urodziny mam!")
    birthday2 = Meeting(datetime(2021, 11, 9, 12, 0), "Urodziny mam!")
    calendar = Calendar()
    #when
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)
    #then
    assert len(calendar.meetings) == 2
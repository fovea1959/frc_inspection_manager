import jsonpickle

import json
import random
import uuid
from enum import Enum, auto


class InspectionReason(Enum):
    Weighin = auto()
    Initial = auto()
    Reinspect = auto()
    Final = auto()


class Inspection:
    def __init__(self):
        self.when = None
        self.inspector_id: uuid = None
        self.robot_weight = None
        self.red_bumper_weight = None
        self.blue_bumper_weight = None
        self.robot_weight_with_red = None
        self.robot_weight_with_blue = None
        self.inspection_reason: InspectionReason = None
        self.comments = None
        self.passed = None


class TeamStatus(Enum):
    Absent = auto()
    Checked_In = auto()
    Weighed = auto()
    Partial = auto()
    Inspected = auto()
    Final_Incomplete = auto()
    Final_Completed = auto()


class Team:
    def __init__(self):
        self.number = None
        self.name = None
        self.checked_in = False
        self.inspections = []
        self.inspector_in_pit = None        # inspector.id

    def __str__(self):
        return "Team " + str(self.number)

    @property
    def status_s(self):
        return str(self.status).rpartition('.')[2].replace('_', ' ')

    @property
    def status(self):
        possible_status = {TeamStatus.Absent}
        if self.checked_in:
            possible_status.add(TeamStatus.Checked_In)
        for inspection in self.inspections:
            if inspection.robot_weight is not None:
                possible_status.add(TeamStatus.Weighed)
            if inspection.passed:
                possible_status.add(TeamStatus.Inspected)
            if inspection.inspection_reason == InspectionReason.Final:
                if inspection.passed:
                    possible_status.add(TeamStatus.Final_Completed)
                else:
                    possible_status.add(TeamStatus.Final_Incomplete)
        # print('1: ', possible_status)
        most_positive_status = sorted(possible_status, reverse=True, key=lambda r: r.value)[0]
        # print('2: ', most_positive_status)
        return most_positive_status


class InspectorStatus(Enum):
    Off = auto()
    Available = auto()
    In_Pit = auto()
    Break = auto()
    Field = auto()


class Inspector:
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = None
        self.status = InspectorStatus.Off
        self.inspection_team_number = None  # team number
        self.time_away_started = None

    def __str__(self):
        return self.name

    @property
    def status_s(self):
        s = str(self.status).rpartition('.')[2].replace('_', ' ')
        if self.inspection_team_number is not None:
            s += f" {self.inspection_team_number}"
        return s


class SaveData:
    pass


class Database:
    def __init__(self):
        self.teams = []
        self.inspectors = []
        self.team_map = {}
        self.inspector_map = {}
        self.dirty = False

    def __str__(self):
        return f"Database, {len(self.teams)} teams, {len(self.inspectors)} inspectors"

    @property
    def is_dirty(self):
        return self.dirty

    def mark_dirty(self):
        self.dirty = True

    def make_indices(self):
        self.team_map.clear()
        for t in self.teams:
            self.team_map[t.number] = t
        self.inspector_map.clear()
        for i in self.inspectors:
            self.inspector_map[i.id] = i

    def fetch_team(self, team_number):
        return self.team_map[team_number]

    def fetch_inspector(self, inspector_id):
        return self.inspector_map[inspector_id]

    def as_json(self):
        save_data = SaveData()
        save_data.teams = self.teams
        save_data.inspectors = self.inspectors
        return jsonpickle.encode(save_data, keys=True, indent=1)

    def from_json(self, json_string):
        save_data = jsonpickle.decode(json_string)
        self.teams = sorted(save_data.teams, key=lambda t: t.number)
        self.inspectors = save_data.inspectors
        self.make_indices()
        self.dirty = False


def dummy_team_list():
    teams = []
    for i in range(1, 41):
        team = Team()
        team.number = (i * 100) + random.randint(1, 99)
        team.name = "Team " + str(team.number)
        teams.append(team)
    return teams


def dummy_inspector_list():
    inspectors = []

    for i in range(0, 8):
        inspector = Inspector()
        inspector.name = "Inspector " + str(i)
        inspector.status = InspectorStatus.Available
        inspectors.append(inspector)

    return inspectors


def dummy_database():
    database = Database()
    database.teams = dummy_team_list()
    database.inspectors = dummy_inspector_list()
    database.make_indices()
    return database


def database_from_tba(fn):
    database = Database()
    with open(fn) as tba_fp:
        tba = json.load(tba_fp)
    for tba1 in tba:
        team = Team()
        team.number = tba1['team_number']
        team.name = tba1['nickname']
        database.teams.append(team)
    database.make_indices()
    return database


if __name__ == '__main__':
    d = database_from_tba('2022misjo_teams.json')
    i1 = Inspector()
    i1.name = "Doug Wegscheid"
    d.inspectors.append(i1)

    print(d)
    j = d.as_json()
    with open('misjo.imd', 'w') as fp:
        fp.write(j)

    with open('misjo.imd', 'r') as fp:
        j = fp.read()
        dd = Database()
        dd.from_json(j)
        print(dd)

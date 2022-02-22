import jsonpickle

import json
import random
import uuid
import enum


InspectionReason = enum.Enum('InspectionReason', 'Initial Reinspect Final')


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
        self.success = False


TeamStatus = enum.Enum('TeamStatus', 'Absent Present Weighed Partial Inspected Final_completed')


class Team:
    def __init__(self):
        self.team_number = None
        self.team_name = None
        self.team_status = None
        self.inspections = []

    def __str__(self):
        return "Team " + str(self.team_number)

    def team_status_s(self):
        return str(self.team_status).rpartition('.')[2]


InspectorStatus = enum.Enum('InspectorStatus', 'Off Available Pit Break Field')


class Inspector:
    def __init__(self):
        self.id: uuid = None
        self.name = None
        self.status = None
        self.inspection_team = None
        self.inspection_started = None
        self.break_started = None

    def __str__(self):
        return self.name

    def status_s(self):
        return str(self.status).rpartition('.')[2]


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

    def is_dirty(self):
        return self.dirty

    def mark_dirty(self):
        self.dirty = True

    def make_indices(self):
        self.team_map.clear()
        for t in self.teams:
            self.team_map[t.team_number] = t
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

    def from_json(self, j):
        save_data = jsonpickle.decode(j)
        self.teams = save_data.teams
        self.inspectors = save_data.inspectors
        self.make_indices()
        self.dirty = False

def dummy_team_list():
    teams = []
    for i in range(1, 41):
        team = Team()
        team.team_number = (i * 100) + random.randint(1, 99)
        team.team_name = "Team " + str(team.team_number)
        team.team_status = TeamStatus.Absent
        teams.append(team)
    return teams


def dummy_inspector_list():
    inspectors = []

    for i in range(0, 8):
        inspector = Inspector()
        inspector.name = "Inspector " + str(i)
        inspector.id = uuid.uuid4()
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
    with open(fn) as fp:
        tba = json.load(fp)
    for tba1 in tba:
        team = Team()
        team.team_number = tba1['team_number']
        team.team_name = tba1['nickname']
        database.teams.append(team)
    database.make_indices()
    return database



if __name__ == '__main__':
    d = database_from_tba('2022misjo_teams.json')
    print(d)
    j = d.as_json()
    with open('misjo.imd', 'w') as fp:
        fp.write(j)

    with open('misjo.imd', 'r') as fp:
        j = fp.read()
        dd = Database()
        dd.from_json(j)
        print(dd)

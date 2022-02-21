import jsonpickle
import random
from frc_inspection_manager import *

def team_list():
    teams = []
    for i in range(1, 41):
        team = Team()
        team.team_number = (i * 100) + random.randint(1, 99)
        team.team_name = "Team " + str(team.team_number)
        team.team_status = TeamStatus.Absent
        teams.append(team)
    return teams


def inspector_list():
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
    database.teams = team_list()
    database.inspectors = inspector_list()
    return database


if __name__ == '__main__':
    j = jsonpickle.dumps(dummy_database(), indent=1)

    print(j)

    db = jsonpickle.loads(j)
    print(db)


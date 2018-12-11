"""
BORIS
Behavioral Observation Research Interactive Software
Copyright 2012-2018 Olivier Friard


  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.

"""

import sqlite3
import os
from config import *
import project_functions

import time


def load_events_in_db(pj, selectedSubjects, selectedObservations, selectedBehaviors):
    """
    populate a memory sqlite database with events from selectedObservations,
    selectedSubjects and selectedBehaviors

    Args:
        pj (dict): project dictionary
        selectedObservations (list):
        selectedSubjects (list):
        selectedBehaviors (list):

    Returns:
        database cursor:

    """

    # # selected behaviors defined as state event
    # state_behaviors_codes = [pj[ETHOGRAM][x]["category"] for x in pj[ETHOGRAM]
    #                              if pj[ETHOGRAM][x]["category"] in selectedBehaviors]
    #
    # # selected behaviors defined as point event
    # point_behaviors_codes = [pj[ETHOGRAM][x]["category"] for x in pj[ETHOGRAM]
    #                              if POINT in pj[ETHOGRAM][x][TYPE].upper()
    #                                 and pj[ETHOGRAM][x]["category"] in selectedBehaviors]

    db = sqlite3.connect(":memory:", isolation_level=None)
    #db = sqlite3.connect("/tmp/1.sqlite", isolation_level=None)

    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE events (observation TEXT,
                                           subject TEXT,
                                           key TEXT,
                                           type TEXT,
                                           category TEXT,
                                           modifiers TEXT,
                                           occurence FLOAT)""")
    cursor.execute("CREATE INDEX observation_idx ON events(observation)")
    cursor.execute("CREATE INDEX subject_idx ON events(subject)")
    cursor.execute("CREATE INDEX key_idx ON events(key)")
    cursor.execute("CREATE INDEX modifiers_idx ON events(modifiers)")

    for subject_to_analyze in selectedSubjects:
        for obsId in selectedObservations:
            for event in pj[OBSERVATIONS][obsId][EVENTS]:
                if event[3] in selectedBehaviors:
                    # extract time, code, modifier and comment (time:0, subject:1, key:2, type: 3, category: 4 ,modifier:5)
                    if ((subject_to_analyze == NO_FOCAL_SUBJECT and event[EVENT_SUBJECT_FIELD_IDX] == "") or (event[EVENT_SUBJECT_FIELD_IDX] == subject_to_analyze)):
                        r = cursor.execute("""INSERT INTO events (observation, subject, key, type, category, modifiers, occurence) VALUES (?,?,?,?,?,?,?)""",
                        (obsId,
                         NO_FOCAL_SUBJECT if event[EVENT_SUBJECT_FIELD_IDX] == "" else event[EVENT_SUBJECT_FIELD_IDX],
                         event[EVENT_BEHAVIOR_FIELD_IDX],
                         event[3],
                         event[5],
                         event[4],
                         str(event[EVENT_TIME_FIELD_IDX])))

    db.commit()
    return cursor

def load_aggregated_events_in_db(pj, selectedSubjects, selectedObservations, selectedBehaviors):
    """
    populate a memory sqlite database with aggregated events from selectedObservations, selectedSubjects and selectedBehaviors

    Args:
        pj (dict): project dictionary
        selectedObservations (list):
        selectedSubjects (list):
        selectedBehaviors (list):

    Returns:
        bool: True if OK else False
        str: error message
        database connector: db connector if bool True else None

    """

    # if no observation selected select all
    if not selectedObservations:
        selectedObservations = sorted([x for x in pj[OBSERVATIONS]])

    # if no subject selected select all
    if not selectedSubjects:
        selectedSubjects = sorted([pj[SUBJECTS][x]["name"] for x in pj[SUBJECTS]] + [NO_FOCAL_SUBJECT])

    # if no behavior selected select all
    if not selectedBehaviors:
        selectedBehaviors = sorted([pj[ETHOGRAM][x][BEHAVIOR_CODE] for x in pj[ETHOGRAM]])

    # check if state events are paired
    out = ""
    for obsId in selectedObservations:
        r, msg = project_functions.check_state_events_obs(obsId, pj[ETHOGRAM],
                                                          pj[OBSERVATIONS][obsId],
                                                          HHMMSS)
        if not r:
            out += "Observation: <strong>{obsId}</strong><br>{msg}<br>".format(obsId=obsId, msg=msg)
    if out:
        return False, out, None

    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    cursor2 = db.cursor()
    cursor2.execute("""CREATE TABLE aggregated_events
                              (id INTEGER PRIMARY KEY ASC,
                               observation TEXT,
                               subject TEXT,
                               behavior TEXT,
                               type TEXT,
                               modifiers TEXT,
                               start FLOAT,
                               stop FLOAT,
                               comment TEXT,
                               comment_stop TEXT)""")


    cursor2.execute("CREATE INDEX observation_idx ON aggregated_events(observation)")
    cursor2.execute("CREATE INDEX subject_idx ON aggregated_events(subject)")
    cursor2.execute("CREATE INDEX behavior_idx ON aggregated_events(behavior)")
    cursor2.execute("CREATE INDEX modifiers_idx ON aggregated_events(modifiers)")


    for obsId in selectedObservations:
        cursor1 = load_events_in_db(pj, selectedSubjects, [obsId], selectedBehaviors)

        for subject in selectedSubjects:
            for behavior in selectedBehaviors:
                print(behavior)
                cursor1.execute("SELECT DISTINCT modifiers FROM events WHERE observation=? AND subject=? AND key=? ORDER BY modifiers",
                                (obsId, subject, behavior,))
                rows_distinct_modifiers = list(x[0].strip() for x in cursor1.fetchall())
                print(rows_distinct_modifiers)
                for distinct_modifiers in rows_distinct_modifiers:

                    cursor1.execute(("SELECT occurence, comment FROM events "
                                    "WHERE observation = ? AND subject = ? AND key = ? AND modifiers = ? ORDER by occurence"),
                                    (obsId, subject, behavior, distinct_modifiers))
                    rows = list(cursor1.fetchall())

                    # for idx, row in enumerate(rows):
                    #
                    #     if behavior in behaviors_key:
                    #         cursor2.execute(("INSERT INTO aggregated_events (observation, subject, behavior, type, modifiers, "
                    #                          "                               start, stop, comment, comment_stop) "
                    #                         "VALUES (?,?,?,?,?,?,?,?,?)"),
                    #                         (obsId, subject, behavior, "", distinct_modifiers,
                    #                          row["occurence"], row["occurence"], row["comment"], "",))


    db.commit()

    return True, "", db

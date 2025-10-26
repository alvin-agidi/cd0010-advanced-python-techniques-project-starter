"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""

import csv
import json
from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        "datetime_utc",
        "distance_au",
        "velocity_km_s",
        "designation",
        "name",
        "diameter_km",
        "potentially_hazardous",
    )
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, "w") as file:
        wr = csv.writer(file, delimiter=",")
        wr.writerow(list(fieldnames))
        for a in results:
            wr.writerow(
                (
                    a.time,
                    a.distance,
                    a.velocity,
                    a._designation,
                    a.neo.name,
                    a.neo.diameter,
                    a.neo.hazardous,
                )
            )


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    with open(filename, "w") as file:
        json_list = []
        for approach in results:
            a = approach.__dict__
            a["neo"] = approach.neo.__dict__
            del a["neo"]["approaches"]
            a["datetime_utc"] = datetime_to_str(a["time"])
            del a["time"]
            a["distance_au"] = float(a["distance"])
            del a["distance"]
            a["velocity_km_s"] = float(a["velocity"])
            del a["velocity"]
            a["neo"]["diameter_km"] = float(a["neo"]["diameter"])
            del a["neo"]["diameter"]
            a["neo"]["potentially_hazardous"] = a["neo"]["hazardous"]
            del a["neo"]["hazardous"]
            json_list.append(a)
        json.dump(json_list, file)

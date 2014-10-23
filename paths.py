from __future__ import print_function

import os
from os.path import join, exists
from os import mkdir

USER_DIR_NAME = os.path.expanduser("~")
TT_DIR_NAME = ".timetracker"

TT_DIR = join(USER_DIR_NAME, TT_DIR_NAME)

TT_LOG = join(TT_DIR, "log")
TT_STATUS = join(TT_DIR, "status")


def normalize(name):
    """
    Normalize the given name to a path-compatible string.
    :param name: The string to convert.
    :return: The normalized version of name.
    """
    # TODO implement
    return name


def get_group_info_file(group):
    """
    Calculate the location of the info file for the given task group.
    :param group: A string representing the task group's name.
    :return: The location of the info file.
    """
    group = normalize(group)
    join(TT_DIR, group, "info")


def get_task_info_file(group, task):
    """
    Calculate the location of the info file for the given task group.
    :param group: A string representing the task group's name.
    :param task: A string representing the task's name.
    :return: The location of the task's info file.
    """
    group = normalize(group)
    task = normalize(task)
    dir = join(TT_DIR, group, task)
    file = join(dir, "info")

    if not exists(dir):
        mkdir(dir)

    if not exists(file):
        f = open(file, "w")


    return file
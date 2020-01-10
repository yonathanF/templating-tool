"""
File generator based on the Mustache syntax
"""

import pystache
from document_models import LectureNotes
import argparse


def command_line():
    """ Lets the user interact with the tool from the 
    command line
    :returns: A string

    """
    parser = argparse.ArgumentParser(
        description='A simple template tool to help you get started with files you use repeatedly.')

    parser.add_argument('type', metavar='TYPE', choices=[
                        "lecture", "essay"], help='The type of latex document')

    parser.add_argument('--title', metavar='TITLE',
                        help='The title of the document')

    parser.add_argument('--lecturer', metavar='PROF',
                        help='The name of the lecturer')

    parser.add_argument('--lecture_number', metavar='N',
                         help='The lecture number')

    args = parser.parse_args()
    process_input(args)


def process_input(args):
    """ Creates to object depending on the 
    args passed in
    """
    renderer = pystache.Renderer(
        search_dirs=["/home/yonathan/Documents/templates/", "."], file_extension="tex")

    if args.type == "lecture":
        lecture = LectureNotes(args.title, "Yonathan Fisseha",
                               args.lecturer, args.lecture_number)
        print(renderer.render(lecture))


if __name__ == "__main__":
    command_line()

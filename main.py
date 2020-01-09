"""
File generator based on the Mustache syntax
"""

import pystache
from datetime import datetime

renderer = pystache.Renderer(search_dirs=["/home/yonathan/Documents/templates/", "."], file_extension="tex")

class LectureNotes(object):
    def date(self):
        return datetime.today() 
    def title(self):
        return "test"

lecture = LectureNotes()
print(renderer.render(lecture))

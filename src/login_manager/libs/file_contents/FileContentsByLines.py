import os
from login_manager.libs.file_contents.FileContents import FileContents
from login_manager.libs.file_contents.FileContentsByRawValue import FileContentsByRawValue


class FileContentsByLines(FileContents):

    def __init__(self, file_contents_by_raw_value):
        assert isinstance(file_contents_by_raw_value, FileContentsByRawValue)
        self.__file_contents_by_raw_value = file_contents_by_raw_value
        self.__lines = self.__file_contents_by_raw_value.get_contents().splitlines()

    def get_path(self):
        return self.__file_contents_by_raw_value.get_path()

    def get_contents(self):
        return self.__lines.copy()

    def update(self, line_index, new_line):
        assert isinstance(line_index, int)
        assert isinstance(new_line, str)
        self.__lines[line_index] = new_line
        self.__file_contents_by_raw_value.update(os.linesep.join(self.get_contents()))

    @classmethod
    def get_instance(cls, path):
        return cls(FileContentsByRawValue.get_instance(path))
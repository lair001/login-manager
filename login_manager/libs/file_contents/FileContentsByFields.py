import os
import re
from login_manager.libs.file_contents.FileContents import FileContents
from login_manager.libs.file_contents.FileContentsByLines import FileContentsByLines


class FileContentsByFields(FileContents):

    def __init__(self, file_contents_by_lines):
        assert isinstance(file_contents_by_lines, FileContentsByLines)
        self.__fields = {}
        self.__file_contents_by_lines = file_contents_by_lines
        for index, line in enumerate(self.__file_contents_by_lines.get_contents()):
            if self.__class__.__has_field(line):
                field_name = self.__class__.__parse_field_name(line)
                field_value = self.__class__.__parse_field_value(line)
                self.__fields[field_name] = { 'line_index': index, 'value': field_value }

    def get_path(self):
        return self.__file_contents_by_lines.get_path

    def get_contents(self):
        return self.__fields.copy()

    def update(self, field_name, field_value):
        self.fields[field_name]['value'] = field_value
        self.__file_contents_by_lines.update(self.fields[field_name]['line_index'], f'{field_name}={field_value}')

    __line_with_field_regex = re.compile("\A[a-zA-Z_]\w*=[^=]+\Z")
    __field_name_regex = re.compile("\A[a-zA-Z_]\w*(?==)")
    __field_value_regex = re.compile("(?<==)[^=]+\Z")

    @classmethod
    def __has_field(cls, line):
        return cls.__line_with_field_regex.search(line) is not None

    @classmethod
    def __parse_field_name(cls, line):
        return re.search(cls.__field_name_regex, line).group(0)

    @classmethod
    def __parse_field_value(cls, line):
        return os.path.expanduser(re.search(cls.__field_value_regex, line).group(0))

    @classmethod
    def get_instance(cls, path):
        return cls(FileContentsByLines.get_instance(path))

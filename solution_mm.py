from os import path
import tempfile


class File:
    """Class for working with files"""

    def __init__(self, path_to_file):
        self.path = path_to_file
        self.current = 0
        self.end = 0
        if not path.exists(path_to_file):
            with open(path_to_file, 'w') as f:
                f.write("")

    def read(self):
        with open(self.path, "r") as f:
            return f.read()

    def write(self, text):
        with open(self.path, "w+") as f:
            f.write(text)
            f.seek(0)
            self.end = len(f.readlines())
            f.seek(0)

    def __str__(self):
        return self.path

    def __iter__(self):
        result = None

        with open(self.path, "r") as file:
            result = file.readlines()
        return iter(result)

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        with open(self.path, "r") as file:
            result = file.readlines()[self.current]
            self.current += 1
            return result.strip("\n")

    def __add__(self, obj):
        storage_path = path.join(tempfile.gettempdir(), 'new.data')
        new_file = File(storage_path)
        content_1 = self.read()
        content_2 = obj.read()
        if content_1.strip() and content_2.strip():
            if content_1[-1] != '\n' and content_2[0] != '\n':
                content_1 += '\n'
        new_file.write(content_1 + content_2)
        return new_file
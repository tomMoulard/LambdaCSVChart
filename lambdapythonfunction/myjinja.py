import re

class template():

    """Templates"""

    def __init__(self, path):
        """Create a new template

        :path: TODO

        """
        self._path = path
        print(self._path)
        self._file = open(self._path).read()

    def get(self):
        return self

    def render(self, *args, **kwargs):
        for key, value in kwargs.items():
            self._file = self._file.replace("{{ " + str(key) +" }}", str(value))
        return self._file

class jinja():

    """Local version of jinja"""

    def __init__(self, path):
        """Create a new object to store templates

        :path: TODO

        """
        self._path = path

    def get_template(self, path):
        return template(self._path+"/"+path).get()

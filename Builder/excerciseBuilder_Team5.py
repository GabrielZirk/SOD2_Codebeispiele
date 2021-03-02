# Sie werden aufgefordert, das Builder-Entwurfsmuster zum Rendern
# einfacher Codestücke zu implementieren


#  Hier ist ein einfaches Beispeil wie man den code verwenden sollte
#     cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
#     print(cb)

from unittest import TestCase

class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'Name: {self.name}, Value: {self.value}'

class Class:
    indent_size = 2

    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str(self):
        if len(self.fields) == 0:
            return f"class {self.name}:\n  pass"
        else:
            code = []
            code.append(f"class {self.name}:")
            code.append(f'{" " * self.indent_size}def __init__(self):')

            for e in self.fields:
                code.append(f'{" " * self.indent_size * 2}self.{e.name} = {e.value}')
            return "\n".join(code)

    def __str__(self):
        return self.__str()

class CodeBuilder:
    def __init__(self, root_name):
        self.root = Class(root_name)

    def add_field(self, type, name):
        self.root.fields.append(Field(type, name))
        return self

    def __str__(self):
        return str(self.root)

if __name__ == '__main__':
    cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
    print(cb)


class Evaluate(TestCase):
    @staticmethod
    def preprocess(s=''):
        return s.strip().replace('\r\n', '\n')

    def test_empty(self):
        cb = CodeBuilder('Foo')
        self.assertEqual(
            self.preprocess(str(cb)),
            'class Foo:\n  pass'
        )

    def test_person(self):
        cb = CodeBuilder('Person').add_field('name', '""') \
            .add_field('age', 0)
        self.assertEqual(self.preprocess(str(cb)),
                         """class Person:
  def __init__(self):
    self.name = \"\"
    self.age = 0""")

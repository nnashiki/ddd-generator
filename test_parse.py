from ast import ClassDef

import ast
from dataclasses import dataclass
from ast import ClassDef
from typing import Iterable

text = """
class LoginApp:
    @inject
    def __init__(self, repo: LoginRepositoryInterface):
        self.repo = repo

    def login(self, username: str, password: str):
        return LoginCruds(self.repo).login(username, password)
        
class Foo:
    
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(self.name)
        
TARGET = 'foo'
"""


@dataclass
class ModuleClassDada:
    module_name: str
    has_classes: Iterable[str]

    def __str__(self):
        tmp = ""
        for the_class in self.has_classes:
            tmp += "\n    class " + the_class


        template = """
@startuml
package "foo" #DDDDDD {
        """ + tmp + """
}
@enduml
        """

        return template


ast_result = ast.parse(text)
classes = [ast_obj.name for ast_obj in ast_result.body if isinstance(ast_obj, ClassDef)]
module_class_dada = ModuleClassDada(module_name='foo', has_classes=classes)
print(module_class_dada)

import os
TARGET_DIR = "./"



import glob
import re
import codecs

import ast
from dataclasses import dataclass
from ast import ClassDef
from typing import Iterable


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
package """ + self.module_name + """ #DDDDDD {
        """ + tmp + """
}
@enduml
        """

        return template


modules = [p for p in glob.glob('./src/**', recursive=True) if os.path.isfile(p) and re.search('.*\.py',str(p))]
for module in modules:
    with codecs.open(module, "r", "utf_8", "ignore") as file:
        ast_result = ast.parse(file.read())
        classes = [ast_obj.name for ast_obj in ast_result.body if isinstance(ast_obj, ClassDef)]
        if len(classes) > 0:
            module_class_dada = ModuleClassDada(module_name=str(module), has_classes=classes)
            print(module_class_dada)

from dataclasses import dataclass

@dataclass
class ParsedDocs:
    items: list
    resources: list
    buildables: list
    production_recipes: list
    buildable_recipes: list
    customizer_recipes: list
    schematics: list
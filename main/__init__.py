import pathlib

import strictyaml

from .models import Recipe
from .templates import recipe_template


root = pathlib.Path(__file__).parent.parent


def define_env(env):
    @env.macro
    def recipe(recipe_path: str) -> str:
        full_path = f"{root.absolute()}/recipes/{recipe_path}.yml"
        with open(full_path) as f:
            recipe_data = strictyaml.load(f.read()).data
        recipe_obj = Recipe.parse_obj(recipe_data)
        return recipe_template.render(recipe=recipe_obj)

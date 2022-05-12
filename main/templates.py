from jinja2 import Environment, FileSystemLoader, select_autoescape

jinja2_env = Environment(
    loader=FileSystemLoader("templates"), autoescape=select_autoescape()
)

recipe_template = jinja2_env.get_template("recipe.md.jinja2")

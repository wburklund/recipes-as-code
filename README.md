# Recipes As Code

Recipe management system built with YAML, Markdown, and Python.

## Description

Recipes As Code is a recipe management system that allows you to create and modify recipes as YAML. It formats recipes as Markdown and publishes them as a website with the help of [MkDocs](https://www.mkdocs.org/). Once a recipe has been published, you can refer to it on any device with a web browser. That way, you don't have to lug your laptop into the kitchen just to read a recipe!

## Getting Started

As mentioned, this project publishes a website.
The below instructions will walk you through adding a recipe and publishing it.

### Dependencies

* Python 3.9

### Installing

Create a virtual environment:

(Windows)
```
python -m venv .venv
.venv/scripts/activate
```

(Mac/Linux)
```
python -m venv .venv
source .venv/bin/activate  # Use the appropriate `activate` script if you're running an alternative shell
```

Install Python packages:
```
pip install -r requirements.txt
```

### Executing program

* Run `mkdocs serve` to begin serving content locally
  * server will update when changes are made in the doc and recipe files

* Run `mkdocs build` to publish content as a static website

### Adding a Recipe

* Run `mkdocs serve` and open the website in your web browser
* Navigate to the "Lunch" page
* Add text to the end of `docs/recipes/lunch.md`:
```
---

{{recipe("lunch/pb_and_j")}}
```
* An error shows up on the page because this recipe doesn't exist yet. Let's fix that.
* Create a file `pb_and_j.yml` under `recipes/lunch/`. Leave it blank for now.
* A different error will show up. Look at the last few lines:
```
pydantic.error_wrappers.ValidationError: 4 validation errors for Recipe
name
  field required (type=value_error.missing)
description
  field required (type=value_error.missing)
ingredients
  field required (type=value_error.missing)
produces
  field required (type=value_error.missing)
```
* These errors are telling us our recipe is missing required information. Paste the following recipe in `pb_and_j.yml`:
```
name: Peanut Butter and Jelly
description: A traditional recipe for a peanut butter and jelly sandwich.
ingredients:
  - name: Sandwich bread
    amount: 2 slices
  - name: Peanut butter
    amount: 2 tbsp
  - name: Grape jelly or strawberry jam
    amount: 2 tsp
steps:
  - step: Spread the peanut butter on one slice of bread.
  - step: Spread the jelly on the other side.
  - step: Put the two pieces of bread together to form a sandwich.
produces: 1 peanut butter and jelly sandwich.
source: https://www.food.com/recipe/traditional-peanut-butter-and-jelly-243965
```
* Save the file.
* You should now see the new recipe at the bottom of the page. Try clicking the checkboxes and source link!

### Adding a New Page

* Run `mkdocs serve` and open the website in your web browser
* Create a file `my_recipes.md` under `docs/recipes/`: 
```
# My Recipes
```
* Open `mkdocs.yml` and add a navigation entry for your new page:
```
nav:
  - index.md
  - Recipes:
    ...
    - recipes/my_recipes.md
  ...
```
* You should see your new page listed as "My Recipes".

## Help

If you get a "command not found" error running `mkdocs`, make sure you've activated your virtual environment.

## Authors

William Burklund <waburklund@gmail.com>

## License

This project is licensed under the GNU Affero General Public License Version 3 - see the LICENSE file for details

## Acknowledgements

* [MkDocs](https://www.mkdocs.org/) for the super-slick documentation site generator
* [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for the theme
* [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) for demonstrating how to build a code generator with Pydantic and Jinja
* [DomPizzie](https://gist.githubusercontent.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc/raw/d59043abbb123089ad6602aba571121b71d91d7f/README-Template.md) for the README template
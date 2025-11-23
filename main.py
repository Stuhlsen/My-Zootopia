import json


def load_data(file_path):
    """Loads a JSON file and returns the parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts a single animal object into an HTML <li> block."""
    name = animal_obj.get("name", "Unknown")
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations") or []

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'

    # Diet
    if "diet" in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    # Location
    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    # Type
    if "type" in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n\n'

    return output



def build_animals_html(data):
    """Builds the HTML for all animals by delegating each one to serialize_animal()."""
    output = ""
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output



def main():
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_html = template_file.read()

    animals_text = build_animals_html(animals_data)

    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_text)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html)

    print("animals.html wurde erzeugt.")


if __name__ == "__main__":
    main()

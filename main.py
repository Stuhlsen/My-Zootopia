import json


def load_data(file_path):
    """Loads a JSON file and returns the parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def build_animals_html(data):
    """Builds an HTML <li> block for each animal using the card design."""
    output = ""

    for animal in data:
        name = animal.get("name", "Unknown")
        characteristics = animal.get("characteristics", {})
        locations = animal.get("locations") or []

        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{name}</div>\n'
        output += '  <p class="card__text">\n'

        # Diet (optional)
        if "diet" in characteristics:
            output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

        # Location (optional, first entry)
        if locations:
            output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

        # Type (optional)
        if "type" in characteristics:
            output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

        output += "  </p>\n</li>\n\n"

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

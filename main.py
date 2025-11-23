import json


def load_data(file_path):
    """Loads a JSON file and returns the parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def build_animals_html(data):
    """Builds an HTML <li> block for each animal."""
    output = ""

    for animal in data:
        output += '<li class="cards__item">\n'

        # Name
        if "name" in animal:
            output += f"Name: {animal['name']}<br/>\n"

        # Characteristics (diet, type)
        characteristics = animal.get("characteristics", {})

        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}<br/>\n"

        # First location
        locations = animal.get("locations")
        if locations:
            output += f"Location: {locations[0]}<br/>\n"

        # Type
        if "type" in characteristics:
            output += f"Type: {characteristics['type']}<br/>\n"

        output += "</li>\n\n"

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

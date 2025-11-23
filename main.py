import json


def load_data(file_path):
    """Loads a JSON file and returns the parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def build_animals_text(data):
    """Build a plain text block with animal information."""
    output = ""

    for animal in data:
        # Name
        if "name" in animal:
            output += f"Name: {animal['name']}\n"

        # Diet
        characteristics = animal.get("characteristics", {})
        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}\n"

        # First location
        locations = animal.get("locations")
        if locations:
            output += f"Location: {locations[0]}\n"

        # Type (optional)
        if "type" in characteristics:
            output += f"Type: {characteristics['type']}\n"

        # Leerzeile zwischen Tieren
        output += "\n"

    return output


def main():
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_html = template_file.read()

    animals_text = build_animals_text(animals_data)

    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_text)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html)

    print("animals.html wurde erzeugt.")


if __name__ == "__main__":
    main()

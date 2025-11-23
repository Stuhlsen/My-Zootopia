import json

def load_data(file_path):
    """Loads a JSON file and returns the parsed data."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info(animal):
    """Prints selected information about a single animal."""

    # Name
    if "name" in animal:
        print(f"Name: {animal['name']}")

    # Diet
    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        print(f"Diet: {characteristics['diet']}")

    # First Location
    locations = animal.get("locations")
    if locations and len(locations) > 0:
        print(f"Location: {locations[0]}")

    # Type
    if "type" in characteristics:
        print(f"Type: {characteristics['type']}")

    print()  # Empty line after each animal


def main():
    animals_data = load_data("animals_data.json")

    for animal in animals_data:
        print_animal_info(animal)


if __name__ == "__main__":
    main()

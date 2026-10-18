# What is for dinner
# My first Python program
# This will collect dinners we have had and offer suggestions on what to have.

# October 17, 2026 Copilot generated:

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import random
@dataclass
class Entree:
    name: str
    protein: str
    origin: str
    recipe: str = ""
class DinnerLibrary:
    def __init__(self, filename: str = "dinners.json") -> None:
        self.path = Path(filename)
        self.entrees = self.load()
    def load(self) -> list[Entree]:
        if not self.path.exists():
            return []
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ValueError(f"{self.path} contains invalid JSON: {error}") from error
        if not isinstance(data, list):
            raise ValueError(f"{self.path} must contain a JSON list.")
        entrees = []
        for number, item in enumerate(data, start=1):
            if not isinstance(item, dict):
                raise ValueError(f"Dinner record {number} must be a JSON object.")
            try:
                entrees.append(Entree(**item))
            except TypeError as error:
                raise ValueError(f"Dinner record {number} has missing or unexpected fields: {error}") from error
        return entrees
    def save(self) -> None:
        self.path.write_text(
            json.dumps([asdict(entree) for entree in self.entrees], indent=2),
            encoding="utf-8",
        )
    def add(self, entree: Entree) -> None:
        self.entrees.append(entree)
        self.save()
class DinnerApp:
    FIELD_NAMES = {
        "name": "name",
        "entree": "name",
        "entree name": "name",
        "protein": "protein",
        "origin": "origin",
        "ethnic origin": "origin",
        "cuisine": "origin",
        "recipe": "recipe",
        "recipe link": "recipe",
        "recipe url": "recipe",
    }
    def __init__(self, library: DinnerLibrary) -> None:
        self.library = library
    @staticmethod
    def ask_required(prompt: str) -> str:
        while True:
            answer = input(prompt).strip()
            if answer:
                return answer
            print("This field is required. Please try again.")
    @staticmethod
    def describe(entree: Entree) -> None:
        print(f"Entree: {entree.name}. Protein: {entree.protein}. Cuisine or origin: {entree.origin}.")
        if entree.recipe:
            print(f"Recipe reference: {entree.recipe}")
    def add_entree(self) -> None:
        print("Add a dinner. You can press Ctrl+C to stop the program.")
        entree = Entree(
            name=self.ask_required("Entree name: "),
            protein=self.ask_required("Protein: "),
            origin=self.ask_required("Cuisine or ethnic origin: "),
            recipe=input("Recipe URL or file path (optional): ").strip(),
        )
        self.library.add(entree)
        print(f"Saved {entree.name} to {self.library.path}.")
    def suggest(self) -> None:
        if not self.library.entrees:
            print("No dinners are saved yet. Choose Add a dinner first.")
            return
        protein_filter = input("Protein filter, or press Enter for any protein: ").strip().casefold()
        origin_filter = input("Cuisine or origin filter, or press Enter for any: ").strip().casefold()
        matches = [
            entree for entree in self.library.entrees
            if (not protein_filter or protein_filter in entree.protein.casefold())
            and (not origin_filter or origin_filter in entree.origin.casefold())
        ]
        if not matches:
            print("No saved dinners match those filters.")
            return
        suggestion = random.choice(matches)
        print("Dinner suggestion:")
        self.describe(suggestion)
    def list_entrees(self) -> None:
        if not self.library.entrees:
            print("No dinners are saved yet.")
            return
        for number, entree in enumerate(self.library.entrees, start=1):
            print(f"Dinner {number}.")
            self.describe(entree)
    def import_recipe(self) -> None:
        file_name = Path(self.ask_required("Path to a .txt or .md recipe file: "))
        if file_name.suffix.casefold() not in {".txt", ".md"}:
            print("That file type is not supported. Choose a .txt or .md file.")
            return
        try:
            text = file_name.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            print(f"Could not read the recipe file: {error}")
            return
        values: dict[str, str] = {}
        for line in text.splitlines():
            cleaned = line.strip().lstrip("# -*\t").strip()
            if ":" not in cleaned:
                continue
            label, value = cleaned.split(":", 1)
            field = self.FIELD_NAMES.get(label.strip().casefold())
            if field and value.strip():
                values[field] = value.strip()
        print("Review the recipe details. Enter any missing information.")
        name = values.get("name") or input("Entree name: ").strip()
        protein = values.get("protein") or input("Protein: ").strip()
        origin = values.get("origin") or input("Cuisine or ethnic origin: ").strip()
        recipe = values.get("recipe", str(file_name))
        if not name or not protein or not origin:
            print("Import cancelled. Entree name, protein, and origin are required.")
            return
        entree = Entree(name=name, protein=protein, origin=origin, recipe=recipe)
        print("Please review this dinner before saving:")
        self.describe(entree)
        confirmation = input("Type yes to save this dinner; anything else cancels: ").strip().casefold()
        if confirmation == "yes":
            self.library.add(entree)
            print(f"Saved {entree.name} to {self.library.path}.")
        else:
            print("Import cancelled; nothing was saved.")
    def run(self) -> None:
        print("Dinner planner. The menu is shown as text; enter the name of an action.")
        while True:
            print("Actions: add, suggest, import, list, quit.")
            action = input("Action: ").strip().casefold()
            if action == "add":
                self.add_entree()
            elif action == "suggest":
                self.suggest()
            elif action == "import":
                self.import_recipe()
            elif action == "list":
                self.list_entrees()
            elif action == "quit":
                print("Goodbye.")
                return
            else:
                print("Unrecognized action. Type add, suggest, import, list, or quit.")
def main() -> None:
    try:
        app = DinnerApp(DinnerLibrary())
        app.run()
    except (OSError, ValueError) as error:
        print(f"Dinner planner could not continue: {error}")
if __name__ == "__main__":
    main()
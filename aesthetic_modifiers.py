import logging

logger = logging.getLogger(__name__)


aesthetic_keywords = {
    "Dark Cinematic": 1.2,
    "Old Money": 1.1,
    "High Fidelity": 1.0,
    "Neon Dreams": 0.8,
    "Retro Arcade": 0.7,
    "Vintage Film": 0.9,
}


def calculate_modifier(aesthetic_name):
    return aesthetic_keywords.get(aesthetic_name, 1.0)


def add_new_aesthetic(aesthetic_name, value):
    aesthetic_keywords[aesthetic_name] = value
    # Optional: persist to database/file system for long-term storage
    # logger.info(f"Added new aesthetic: {aesthetic_name}")


def calculate_aesthetic_overrides(aesthetic_name1, aesthetic_name2):
    return 1.0 / (
        calculate_modifier(aesthetic_name1) / calculate_modifier(aesthetic_name2)
    )


def load_aesthetic_overrides(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            override_map = {}
            for line in data.splitlines():
                if line.startswith("#"):
                    continue
                key, value = line.split("=")
                key = key.strip()
                value = float(value.strip())
                override_map[key] = value
            return override_map
    except FileNotFoundError:
        print("File not found. Using default aesthetic overrides.")
        return {}


def save_aesthetic_overrides(filename, override_map):
    try:
        with open(filename, "w") as file:
            for key, value in override_map.items():
                file.write(f"{key}={value}\n")
    except Exception as e:
        print(f"Error saving aesthetic overrides: {str(e)}")

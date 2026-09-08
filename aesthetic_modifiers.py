import os
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


def save_default_overrides(filename):
    default_map = {"plot_size": 8.0, "point_color": 1.0, "label_size": 12.0}
    save_aesthetic_overrides(filename, default_map)


def load_default_overrides(filename):
    try:
        with open(filename, "r") as file:
            default_map = {}
            for line in file.read().splitlines():
                if line.startswith("#"):
                    continue
                key, value = line.split("=")
                key = key.strip()
                value = float(value.strip())
                default_map[key] = value
            return default_map
    except FileNotFoundError:
        print("Default file not found. Using default aesthetic overrides.")
        save_default_overrides(filename)
        return load_default_overrides(filename)
    except Exception as e:
        print(f"Error loading default aesthetic overrides: {str(e)}")


def save_custom_overrides(filename, custom_map):
    try:
        with open(filename, "w") as file:
            for key, value in custom_map.items():
                file.write(f"{key} = {value}\n")
    except Exception as e:
        print(f"Error saving custom aesthetic overrides: {str(e)}")


def load_custom_overrides(filename):
    try:
        with open(filename, "r") as file:
            custom_map = {}
            for line in file.read().splitlines():
                if line.startswith("#"):
                    continue
                key, value = line.split("=")
                key = key.strip()
                value = float(value.strip())
                custom_map[key] = value
            return custom_map
    except FileNotFoundError:
        print("Custom file not found. Using default aesthetic overrides.")
        return load_default_overrides(filename)


def save_default_overrides(filename, default_map):
    try:
        with open(filename, "w") as file:
            for key, value in default_map.items():
                file.write(f"{key} = {value}\n")
    except Exception as e:
        print(f"Error saving default aesthetic overrides: {str(e)}")


def load_default_overrides(filename):
    try:
        with open(filename, "r") as file:
            default_map = {}
            for line in file.read().splitlines():
                if line.startswith("#"):
                    continue
                key, value = line.split("=")
                key = key.strip()
                value = float(value.strip())
                default_map[key] = value
            return default_map
    except FileNotFoundError:
        default_default_map = {"map1": 1.0, "map2": 2.0}  # example default map
        return default_default_map


def load_specific_override(filename, key):
    try:
        with open(filename, "r") as file:
            for line in file.read().splitlines():
                if line.startswith("#"):
                    continue
                curr_key, value = line.split("=")
                curr_key = curr_key.strip()
                if curr_key == key:
                    return float(value.strip())
    except FileNotFoundError:
        return None


def load_specific_defaults_from_file(filename, defaults):
    try:
        override_found = False
        with open(filename, "r") as file:
            for line in file.read().splitlines():
                if line.startswith("#"):
                    continue
                key, value = line.split("=")
                key = key.strip()
                if key in defaults:
                    defaults[key] = float(value.strip())
                    override_found = True
            if not override_found:
                return defaults
    except FileNotFoundError:
        return defaults


def write_specific_defaults_to_file(filename, defaults):
    with open(filename, "w") as file:
        file.write("\n# Aesthetic modifier defaults\n")
        for key, value in defaults.items():
            file.write(f"{key}={value}\n")


def load_specific_defaults_from_environment(defaults):
    for key in defaults:
        if key in os.environ:
            try:
                value = float(os.environ[key])
                defaults[key] = value
            except ValueError:
                pass


def load_specific_defaults_from_file(filename, defaults):
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                key, value = line.split("=")
                if key in defaults:
                    try:
                        defaults[key] = float(value)
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass

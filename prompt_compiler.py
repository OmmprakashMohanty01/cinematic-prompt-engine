import logging
from typing import List, Dict

logger = logging.getLogger(__name__)


def inject_lighting_camera_rendering_base(
    base_subject, lighting=None, camera_angles=None, rendering=None
):
    injected_base = base_subject
    if lighting:
        injections = {
            "l": "lighting = {}",
            "l_": f'{{"type": "spotlight", "intensity": {lighting["spotlights"][0]["intensity"]}, "fov": {lighting["spotlights"][0]["field_of_view"]}}}',
            "c": "camera_angles = {}",
            "c_": f'{{"elevation": {camera_angles["elevation"]}, "azimuth": {camera_angles["azimuth"]}}}',
            "r": "rendering = {}",
            "r_": f'{{"render_quality": "{rendering["render_quality"]}", "resolution": ({rendering["resolution"][0]}, {rendering["resolution"][1]})}}',
        }
        for key, value in injections.items():
            if key != "l_":
                inject = "{" + key + "} = {}"
            else:
                inject = key + "=" + value
            if key in lighting:
                injected_base += "\n" + inject.format(lighting[key])
        if "l_" in lighting:
            injected_base += "\n" + injected_base[8]
    return injected_base


lighting = {
    "spotlights": [
        {"type": "spotlight", "intensity": 0.5, "fov": 0.8, "color": (1.0, 1.0, 1.0)},
        {
            "type": "directional_light",
            "intensity": 0.2,
            "color": (1.0, 1.0, 1.0),
            "direction": (0.5, 0.5, 0.5),
        },
    ]
}
camera_angles = {"elevation": 0.785, "azimuth": 0}
rendering = {"render_quality": "high", "resolution": [2560, 1400]}

subject = (
    "A scene with 2 spotlights, 1 directional light,"
    + " 90 degree camera angle, with high rendering quality and 2560x1400 resolution."
)
print(
    inject_lighting_camera_rendering_base(subject, lighting, camera_angles, rendering)
)


def inject_animation(base_subject: str, animation: Dict) -> str:
    if not animation:
        return base_subject

    injected_base = base_subject
    injections = {
        "a": "animation = {}",
        "a_": f'{{"duration": {animation["duration"]}, "frames_per_second": {animation["frames_per_second"]}}}',
    }
    for key, value in injections.items():
        if key != "a_":
            inject = "{" + key + "} = {}"
        else:
            inject = key + "=" + value
        injected_base += "\n" + inject.format(animation[key])
    return injected_base


def inject_sound(
    base_subject: str, sound: Dict, sound_effects=None, volume=None
) -> str:
    injected_base = base_subject
    injections = {
        "s": "sound = {}",
        "s_": f'{{"source": "{sound["source"]}", "type": "{sound["type"]}"}},',
        "sf": "sound_effects = {}",
        "sf_": f'{{"type": "{sound_effects["type"]["sf"]}", "duration": {sound_effects["duration"]}}}',
        "v": "volume = {}",
        "v_": f'{{"master_volume": {volume["master_volume"]}, "sound_volume": {volume["sound_volume"]}}}',
    }
    for key, value in injections.items():
        if key != "s_":
            inject = "{" + key + "} = {}"
        elif key != "sf_":
            inject = "{" + key + "}" + value
        else:
            inject = f"  {injections[key]}"
            if "sf" in sound_effects:
                injected_base += inject.format(injections["sf_"])
        if key in sound:
            injected_base += "\n" + inject.format(sound[key])
    return injected_base


sound = {
    "source": "engine",
    "type": "dynamic",
    "pitch": 1.2,
    "volume": 0.8,
    "frequency": 500,
}
sound_effects = {
    "type": {"sf": "explosion"},
    "duration": 2,
    "volume": 1.0,
    "pitch": 2.0,
}
volume = {
    "master_volume": 0.7,
    "sound_volume": 0.9,
}
subject = (
    "A game with engine sound, dynamic type, "
    "pitch: 1.2, volume: 0.8, frequency: 500 Hz, "
    "with explosion sound effect, duration: 2 seconds, "
    "pitch: 2.0, volume: 1.0, and with master volume: 0.7 and sound volume: 0.9."
)
print(inject_sound(subject, sound, sound_effects, volume))


def inject_terrain(
    base_subject: str, terrain: Dict, elevation: Dict = None, grass=None
) -> str:
    injected_base = base_subject
    injections = {
        "t": "terrain = {}",
        "t_": f'{{"height": {terrain["height"]}, "material": "{terrain["material"]}"}},',
        "e": "elevation = {}",
        "e_": f'{{"min": {elevation["min"]}, "max": {elevation["max"]}}}',
        "g": "grass = {}",
        "g_": f'{{"color": "{grass["color"]}", "length": {grass["length"]}}}',
    }
    for key, value in injections.items():
        if key != "t_":
            inject = "{" + key + "} = {}"
        else:
            inject = key + "=" + value
        if key in terrain:
            injected_base += "\n" + inject.format(terrain[key])
    if "e_" in elevation:
        injected_base += "\n" + injections["e_"]
    if "g_" in grass:
        injected_base += "\n" + injections["g_"]
    return injected_base


terrain = {
    "height": 0.8,
    "material": "dirt",
}
elevation = {"min": -0.5, "max": 0.2}
grass = {"color": "green", "length": 0.5}
subject = (
    "A game with terrain height of 0.8, material of dirt, "
    "elevation min: -0.5 and max: 0.2, and with grass color of green and length of 0.5."
)
print(inject_terrain(subject, terrain, elevation, grass))


import logging
from typing import Dict

logger = logging.getLogger(__name__)


def inject_weather(base_subject: str, weather: Dict) -> str:
    injected_base = base_subject
    injections = {
        "w": "weather = {}",
        "w_": f'{{"type": "{weather["type"]}", "temperature": {weather["temperature"]}, "humidity": {weather["humidity"]}, "wind_speed": {weather["wind_speed"]}}}',
    }
    for key, value in injections.items():
        if key != "w_":
            inject = "{" + key + "} = {}"
        else:
            inject = key + "=" + value
        injected_base += "\n" + inject.format(weather[key])
    return injected_base


weather = {
    "type": "rainy",
    "temperature": 15,
    "humidity": 0.8,
    "wind_speed": 10,
}
subject = (
    "A game with rainy weather, temperature of 15, "
    "humidity of 0.8 and wind speed of 10."
)
print(inject_weather(subject, weather))


import logging
from typing import Dict


logger = logging.getLogger(__name__)


def inject_water(base_subject: str, water: Dict) -> str:
    injected_base = base_subject
    injections = {
        "wa": "water = {}",
        "wa_": f'{{"level": {water["level"]}, "texture": "{water["texture"]}", "flow_rate": {water["flow_rate"]}}}',
    }
    for key, value in injections.items():
        if key != "wa_":
            inject = "{" + key + "} = {}"
        else:
            inject = key + "=" + value
        if key in water:
            injected_base += "\n" + inject.format(water[key])
    return injected_base


water = {
    "level": 0.5,
    "texture": "wavy",
    "flow_rate": 2,
}
subject = "A game with water level of 0.5, texture of wavy, and flow rate of 2."
print(inject_water(subject, water))


from typing import Dict


def extract_wood(base_subject: str, wood: Dict) -> str:
    extracted_base = base_subject
    extractions = {
        "wh": "wood = {}",
        "wh_": f'{{"density": {wood["density"]}, "grain": "{wood["grain"]}", "stability": {wood["stability"]}}}',
    }
    for key, value in extractions.items():
        if key != "wh_":
            extract = "{" + key + "} = {}"
        else:
            extract = key + "=" + value
        if key in wood:
            extracted_base += "\n" + extract.format(wood[key])
    return extracted_base


wood = {
    "density": 0.7,
    "grain": "smooth",
    "stability": 3,
}
subject = "A game with wood density of 0.7 and grain of smooth, also stability of 3."
print(extract_wood(subject, wood))

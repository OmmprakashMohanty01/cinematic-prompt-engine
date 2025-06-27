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

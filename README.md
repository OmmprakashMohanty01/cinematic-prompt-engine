# Cinematic Prompt Engine 🎬✨

An advanced prompt compilation tool designed for generative AI models. It programmatically injects complex lighting, camera angles, and rendering constraints into base subjects to generate highly detailed and cinematic outputs.

## 🚀 Features

- **Prompt Compilation (`prompt_compiler.py`)**: Dynamically merges base subjects with environmental variables to create structured AI prompts.
- **Aesthetic Modifiers (`aesthetic_modifiers.py`)**: Applies predefined visual styles, cinematic lighting rigs (e.g., spotlights, FOV), and rendering parameters.
- **API Integration (`api_client.py`)**: Robust API client implementation to send compiled prompts directly to generative AI endpoints.

## 🛠 Tech Stack

- **Language:** Python 3.x
- **Key Concepts:** String manipulation, API integration, JSON structuring, typing & logging.

## 💻 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OmmprakashMohanty01/cinematic-prompt-engine.git
   cd cinematic-prompt-engine
   ```
2. **Configure your environment:**
   Ensure you have the required API keys configured (check the `api_client.py` for specific environment variables).
3. **Run the compiler:**
   ```bash
   python3 prompt_compiler.py
   ```
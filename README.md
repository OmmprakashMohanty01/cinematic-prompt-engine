<div align="center">
  
# Cinematic Prompt Engine 🎬✨

**An advanced prompt compilation tool designed for generative AI models, engineered to transform flat concepts into visually striking masterpieces.**

[![CI/CD](https://github.com/OmmprakashMohanty01/cinematic-prompt-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/OmmprakashMohanty01/cinematic-prompt-engine/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 🌟 Executive Summary

The **Cinematic Prompt Engine** is a robust, modular pipeline that programmatically injects complex lighting, camera angles, and rendering constraints into base subjects. By leveraging a structured compiler and aesthetic modifiers, it guarantees that generative AI outputs maintain a high degree of fidelity, artistic direction, and photorealism. 

Whether you need volumetric fog in a cyberpunk cityscape or anamorphic lens flares on a dark portrait, the engine systematically builds prompts that guide AI models to perfection.

### Visual Outputs

Here is a glimpse of what the engine can produce when its aesthetic modifiers and atmospheric lighting rules are applied:

![Cyberpunk Cityscape](assets/cyberpunk_cityscape.jpg)
*Figure 1: "Cyberpunk neon city street scene" generated with injected atmospheric lighting, volumetric fog, and photorealistic 8k modifiers.*

![Rogue AI Portrait](assets/cinematic_portrait.jpg)
*Figure 2: "Rogue AI android" generated with custom bokeh, anamorphic lens flare, and dramatic chiaroscuro lighting modifiers.*

---

## 🚀 Core Features

- **Prompt Compilation (`prompt_compiler.py`)**: Dynamically merges base subjects with environmental variables to create highly structured AI prompts.
- **Aesthetic Modifiers (`aesthetic_modifiers.py`)**: Applies predefined visual styles, cinematic lighting rigs (e.g., spotlights, FOV, chiaroscuro), and rendering parameters to guarantee a premium look.
- **API Integration (`api_client.py`)**: A robust API client implementation to send compiled prompts directly to generative AI endpoints with proper error handling and exponential backoff.

## 🛠 Tech Stack & Architecture

- **Language:** Python 3.10+
- **Key Concepts:** Abstract Syntax Trees (AST) for prompt structuring, Asynchronous API integration, JSON data validation, typing & logging.
- **CI/CD:** Automated testing and flake8 linting via GitHub Actions.

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
   python3 prompt_compiler.py --subject "A futuristic city" --style "cyberpunk"
   ```

## 🤝 Contributing

Contributions are welcome! Please check out the [Issues](https://github.com/OmmprakashMohanty01/cinematic-prompt-engine/issues) tab for `good first issue` tags if you'd like to get started.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
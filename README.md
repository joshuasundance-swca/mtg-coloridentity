---
title: mtg-coloridentity
emoji: 🧙
colorFrom: blue
colorTo: red
sdk: streamlit
sdk_version: 1.30.0
app_file: app.py
pinned: true
license: mit
---

# mtg-coloridentity

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

[![Push to HuggingFace Space](https://github.com/joshuasundance-swca/mtg-coloridentity/actions/workflows/hf-space.yml/badge.svg)](https://github.com/joshuasundance-swca/mtg-coloridentity/actions/workflows/hf-space.yml)
[![Open HuggingFace Space](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/joshuasundance/mtg-coloridentity)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)


# mtg-coloridentity

🤖 This README was written by GPT-4. 🤖

## Overview
This Streamlit app is designed for the multi-label classification of Magic: The Gathering (MTG) cards,
specifically focusing on their color identity.
It utilizes a pre-trained model hosted on Hugging Face, `joshuasundance/mtg-coloridentity-multilabel-classification`,
to predict the color identity of MTG cards based on their names and descriptions.

## Features
- Interactive UI: Users can input the name and text of any MTG card to get predictions on its color identity.
- Color Probabilities: The app displays the probability of each color identity (Black, Green, Red, Blue, White) for the given card.
- Random Card Selection: With a "Roll the Dice" feature, users can load the text of a random MTG card from the dataset.

## How It Works
The app fetches a pre-trained `SetFit` model from Hugging Face and uses it to
predict the color identities of MTG cards.
The model's predictions are displayed as a bar chart,
showing the probability of each color identity.

## Getting Started
To run this app locally, clone the repository and ensure you have the following prerequisites installed:

- Python 3.x
- `streamlit`
- `pandas`
- `seaborn`
- `matplotlib`
- `datasets` and `setfit` from Hugging Face

## Contributions, Support, and Contact

Contributions to this project are welcome! Please feel free to submit issues and pull requests.

For support, please raise an issue on GitHub or in the HuggingFace space.

## License

This project is under the [MIT License](LICENSE.md).

## Acknowledgments

Thanks to HuggingFace and `setfit`!

## TODO
- [ ] make a todo list ;)
- [ ] improve READMEs
- [ ] make better model(s)
- [x] learn in public

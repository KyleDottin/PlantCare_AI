# PlantCare_AI

*"An AI-powered solution for plant health monitoring and pest detection, conceived for ENSEA's 2025 hackathon."*

--- 

## Overview
PlantCare_AI is an innovative project that leverages artificial intelligence, electronics and mechanical design to assist farmers and plant enthusiasts in detecting plant illnesses and pests efficiently. By integrating multiple disciplines, the system ensures precise diagnosis, ease of use, and adaptability for various environments.

## Table of Contents
- [General Description](#general-description)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Contributors](#contributors)
- [Acknowlegements and Citation](#acknowlegements-and-citation)

---

## General Description

**Theme:** *"Engineering in a Constrained World: An Environmental Challenge"*

This project was developed as part of a hackathon with the theme emphasizing the importance of sustainable engineering practices in addressing environmental challenges. **PlantCare_AI** aligns with this theme in two major aspects:

1. **Purpose of the Project:**
   - Agricultural losses caused by plant diseases significantly impact global food security. Our project aims to mitigate these losses by detecting plant diseases early, allowing farmers to take timely and targeted action. By providing an accessible and cost-effective solution, we contribute to reducing the overuse of pesticides and preventing large-scale agricultural damage.

2. **Eco-conscious Design Choices:**
   - **Hardware Efficiency:** The project leverages a Raspberry Pi, a low-energy-consuming and cost-efficient microcontroller, for its operations.
   - **Reuse of AI Models:** Instead of training a new AI model from scratch, which is resource-intensive, we opted to adapt and use an open-source model.
   - **Local Network Usage:** The project minimizes reliance on cloud infrastructure by using a local network setup, reducing both environmental impact and dependency on high-energy server farms.

By prioritizing resource efficiency and practicality, **PlantCare_AI** embodies the principles of environmentally conscious engineering. It serves as an example of how innovation can address real-world problems while staying mindful of environmental constraints.

---

## Features
- **AI-Based Plant Disease Detection**
   - Detects plant illnesses and pests from leaf images using a pre-trained model.
   - Supports various crops like tomatoes, grapes, and apples, with predictions categorized into healthy or disease-specific classes.

- **Mechanical Integration**
   - A rack-and-pinion mechanism to enable camera mobility for capturing multiple plants

- **Electronics Module**
   - Includes LED indicators and buttons for user interaction.
   - Integrated resistors for circuit stability and control.

- **Web Interface**
   - A user-friendly website for visualizing detection results.
     
---

## How It Works
1. **Capture an Image**: The camera captures an image of a plant leaf, controlled via the mechanical setup.
2. **Image Processing**: The AI module preprocesses the image, making it suitable for the trained MobileNet model.
3. **Disease Prediction**: The AI predicts the health status or disease type and returns the result.
4. **User Interaction**: Results are displayed on the web interface, with LEDs and buttons indicating the system's status.

---

## Installation
### Prerequisites
- Raspberry Pi with Python 3.7+
- TensorFlow, Flask/Django, Torch. 
- 3D printer for the case and mechanism
### Steps
```bash
# Clone the repository
$ git clone https://github.com/ReemKhater/PlantCare_AI.git
$ cd PlantCare_AI
```

---

## Contributors
- **Benoit Baguelin** 
- **Kyle Dottin** 
- **Elio Flandin** 
- **Kevin Dugard** 
- **Reem Khater**

---

## Acknowledgments and Citation
- The dataset used in this project: [PlantVillage-Dataset](https://github.com/spMohanty/PlantVillage-Dataset.git).
- Open source machine learning model: [Plant-Disease-Detection](https://github.com/NouraAlgohary/Plant-Disease-Detection.git).

@article{Mohanty_Hughes_Salathé_2016,
title={Using deep learning for image-based plant disease detection},
volume={7},
DOI={10.3389/fpls.2016.01419},
journal={Frontiers in Plant Science},
author={Mohanty, Sharada P. and Hughes, David P. and Salathé, Marcel},
year={2016},
month={Sep}} 

--- 

# QR Code Generator

## Overview

Welcome to the QR Code Generator project! This Python-based application lets you quickly and easily generate QR codes from URLs. It incorporates a simple command-line interface and uses the robust `qrcode` library to generate the QR codes.

## Features

- **Easy to Use**: Simple command-line interface for entering URLs.
- **Customizable**: Easily modify QR code properties such as box size and border size.
- **Quick Setup**: Set up your development environment in minutes using virtual environments.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python 3.12](https://www.python.org/downloads/) or higher installed on your machine.
- [Pip](https://pip.pypa.io/en/stable/installation/) installed for package management.

### Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/QRcode_generator.git
   cd QRcode_generator
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv qr_env
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     qr_env\Scripts\activate
     ```
   - On macOS or Linux:
     ```bash
     source qr_env/bin/activate
     ```

4. **Install Required Packages**
   ```bash
   pip install qrcode[pil]
   ```

### Usage

1. Run the script:

   ```bash
   python generate_qr.py
   ```

2. Enter the URL when prompted. The script will generate a QR code and save it as `qr_code.png` in the current directory.

### Example

#### Generate QR Code from URL

```bash
Enter the URL: https://www.example.com
QR Code generated and saved as 'qr_code.png'
```

# Aurebesh Matrix

A simple Python program that creates a matrix-like effect using the Aurebesh font. Characters fall down the screen at varying speeds, creating a visually dynamic display reminiscent of the iconic "Matrix" digital rain.

![](images/program.gif)

## Features

- Displays random characters from the Aurebesh font.
- Characters fall at different speeds for a more dynamic effect.
- Adjustable density of falling characters.
- Customizable display size and font size.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**

   ```bash
   git clone git@github.com:blakeridgway/aurebesh-matrix.git
   cd aurebesh-matrix
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Pygame**:

   ```bash
   pip install pygame
   ```

## Usage

1. Run the program:

   ```bash
   python aurebesh_matrix.py
   ```

2. Press the close button on the window to exit the program.

## Customization

- **Density of Characters**: Adjust the line `if random.random() > 0.9:` in the code to change how frequently new characters are generated. Lowering the value will increase density.
  
- **Speed of Characters**: Modify the line `speed = random.randint(1, 5)` to change the range of falling speeds. For example, `random.randint(1, 10)` will allow for faster falling characters.

- **Font Size and Display Size**: Change the `font_size`, `width`, and `height` variables in the code to customize the appearance of the display.

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as you wish.

## Acknowledgments

- Inspired by the "Matrix" movie series.
- Special thanks to the creators of the Aurebesh font.

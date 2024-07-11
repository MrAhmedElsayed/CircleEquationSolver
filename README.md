# CircleEquationSolver

CircleEquationSolver is a Tkinter-based desktop application designed to help users solve the equation of a circle. By entering the center coordinates (h, k) and the radius (r), the app generates both the standard form and the general form of the circle equation.

## Features

- Simple and intuitive GUI using Tkinter
- Input fields for center coordinates (h, k) and radius (r)
- Generates and displays the standard form and general form of the circle equation
- Easy installation process

## Installation

To install CircleEquationSolver, download the installer from the [Google Drive link](https://drive.google.com/file/d/1VXsQdqtYRqKqWGZsQP_OpHi5NrDALkw0/view?usp=sharing) and run it on your computer.

## Usage

1. Open the CircleEquationSolver application.
2. Enter the x-coordinate (h) of the circle's center.
3. Enter the y-coordinate (k) of the circle's center.
4. Enter the radius (r) of the circle.
5. Click the "Generate Equation" button.
6. The application will display the standard form and general form of the circle equation.

## Example

Suppose you enter:
- Center x-coordinate (h): 3
- Center y-coordinate (k): -2
- Radius (r): 5

The application will display:
- Standard form: (x - 3)² + (y + 2)² = 25
- General form: x² + y² - 6x + 4y - 12 = 0

## Creating the Desktop Application

This project uses [PyInstaller](https://www.pyinstaller.org/) to create a standalone desktop application.

### Steps to Create the Desktop Application

1. Install PyInstaller:
    ```sh
    pip install pyinstaller
    ```

2. Navigate to the project directory and run PyInstaller:
    ```sh
    pyinstaller --onefile --windowed main.py
    ```
   Replace `main.py` with the name of your main Python script.

3. PyInstaller will generate a `dist` folder containing the executable file.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/yourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/yourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [Ahmed Elsayed](mailto:ahmedsayed551991@gmail.com).


# Volume Calculator Web App

A simple web application built with Python and Flask that calculates the volume of a rectangular prism based on user-inputted length, width, and height dimensions.

## Features
* Accepts decimal and whole number inputs for Length, Width, and Height.
* Calculates the volume (`Length × Width × Height`) on the backend via HTTP `POST` requests.
* Preserves entered dimensions in the form fields after calculation.
* Responsive UI styled with Bootstrap.

## Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML5, Jinja2, Bootstrap 6 (Alpha)

## Project Structure
```text
volume-calculator/
├── main.py
└── templates/
    └── index.html
```

## Getting Started

### Prerequisites
Make sure you have Python 3 and `pip` installed on your system.

### Installation & Running Locally
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd volume-calculator
   ```

2. **Install Flask:**
   ```bash
   pip install flask
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

4. **Open in your browser:**
   Navigate to `http://127.0.0` to use the calculator.

## Usage
1. Enter the **Length**, **Width**, and **Height** values into the input fields.
2. Click the **Calculate** button.
3. The calculated volume will appear directly above the button.

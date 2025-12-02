
# 📸 PNG to JPG Batch Converter

A simple, reliable project using Python and Batch scripting to convert all PNG files within a user-selected folder into optimized JPG images.

## ✨ Features

  * **Interactive Folder Selection:** Uses a standard Windows dialog box to select the input folder via a Batch script.
  * **Batch Conversion:** Converts all `.png` files found in the selected directory.
  * **Transparency Handling:** Automatically handles the alpha (transparency) channel in PNGs by replacing it with a solid white background, ensuring clean JPG output.
  * **High Quality Output:** Saves images with a JPEG quality setting of 95.

## 🛠️ Prerequisites

Before running the converter, you must have the following installed:

1.  **Python 3:** Ensure Python is installed and accessible from your command line (i.e., the `py` or `python` command works).
2.  **Pillow Library:** The required image processing library for Python.

### Installation

Install the necessary Python library using `pip`:

```bash
pip install Pillow
```

## 🚀 How to Use

### 1\. Project Setup

Place the three main files in the same folder:

  * `converter.py` (The Python script)
  * `browse.vbs` (The VBScript file for the folder dialog)
  * `RunConverter.bat` (The Windows Batch executable)

### 2\. Execution

Double-click the **`RunConverter.bat`** file.

1.  A Windows folder selection dialog will appear with the title "Select the Folder with your PNG files:".
2.  Navigate to and select the folder containing the PNG images you wish to convert. Click **OK**.
3.  The console will display the selected folder path and start the conversion process.
4.  A success or error message will be printed for each file processed.

### 3\. Output

All converted `.jpg` files will be saved into a new folder named **`jpg_output`** created in the same location as your scripts.

## 📂 Project Structure

```
PNG_TO_JPG_CONVERTER/
├── RunConverter.bat     <-- EXECUTE THIS FILE
├── converter.py         <-- Main Python logic
├── browse.vbs           <-- Folder selection helper script
└── jpg_output/          <-- Folder where converted JPGs are saved
```

## 📄 Code Details

### `converter.py`

This script handles the image manipulation using the Pillow library.

| Key Functionality | Details |
| :--- | :--- |
| **Input** | Takes the input directory as a command-line argument (`sys.argv[1]`). |
| **Transparency Fix** | If `img.mode == 'RGBA'`, it creates a new white background (`Image.new('RGB', ...)`) and pastes the transparent image onto it. |
| **Saving** | Saves the image using `img.save(..., 'JPEG', quality=95)`. |

### `RunConverter.bat`

This is the main driver script for Windows users.

1.  It calls `cscript //NOLOGO browse.vbs` to launch the folder picker.
2.  It uses a `for /f` loop to capture the resulting folder path into the `selected_folder` variable.
3.  It executes the Python script: `py converter.py "%selected_folder%"`.

-----

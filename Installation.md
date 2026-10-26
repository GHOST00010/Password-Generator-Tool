# Password Generator Tool — Installation Guide

This guide explains how to download and run the **Password Generator Tool** on a Windows computer.

## Method 1: Run the Windows Executable (Recommended)

Use this method if you want to run the application without installing Python.

### Step 1: Download the Project

Open the GitHub repository:

**[Password Generator Tool — GitHub](https://github.com/GHOST00010/Password-Generator-Tool)**

Click **Code → Download ZIP** to download the project, then extract the ZIP file to a folder on your computer.

Alternatively, if the project provides `passgen.exe` under **Releases**, download the executable from there.

### Step 2: Locate the Executable

Open the extracted project folder and find the ***`dist`*** folder.

Inside it, locate:

***`passgen.exe`***

### Step 3: Run the Application

Double-click ***`passgen.exe`*** to launch the Password Generator Tool.

If you prefer to run it using PowerShell:

1. Open the project folder.
2. Open the ***`dist`*** folder.
3. Click the address bar, type `powershell`, and press Enter.
4. Run the following command:
   ```powershell
   .\passgen.exe
   ```

**Note:** The executable must be included in the downloaded project or downloaded separately from GitHub Releases. If the `dist` folder or executable is missing, download the executable from the project's Releases section, if available.

This method does not require a separate Python installation.

---

## Method 2: Run from Python Source Code

Use this method if you want to run or modify the Python source code.

### Step 1: Install Python

Download and install Python 3 from the official website:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

During installation on Windows, enable **Add Python to PATH** if that option is shown.

Verify the installation by opening Command Prompt or PowerShell and running:

```bash
python --version
```

### Step 2: Download the Source Code

Open the repository:

[https://github.com/GHOST00010/Password-Generator-Tool](https://github.com/GHOST00010/Password-Generator-Tool)

Click **Code → Download ZIP**, then extract the downloaded ZIP file.

Alternatively, if Git is installed, run:

```bash
git clone https://github.com/GHOST00010/Password-Generator-Tool.git
```

Open the downloaded project folder. The folder name may be `Password-Generator-Tool`, depending on how you downloaded it.

### Step 3: Run the Python Program

Open a terminal in the project folder containing `passgen.py` and run:

```bash
python passgen.py
```

The program should start if Python is installed correctly and the source code is available.

---

## Troubleshooting

- **`passgen.exe` is missing:** Check the project's GitHub Releases section or confirm that the executable was included in the ZIP download.
- **Windows displays a security warning:** Only run the executable if you trust its source. Verify that it came from the official project repository. Do not bypass warnings unless you have verified the file is safe.
- **The application closes immediately:** Try launching it from PowerShell to see whether an error message appears.
- **`python` is not recognized:** Install Python and ensure it is added to PATH, then reopen the terminal.

## Important Information

- The Windows executable is built using PyInstaller.
- Method 1 does not require users to install Python separately.
- Method 2 requires Python to be installed.
- The current executable is a standalone application, not a traditional installation wizard. It does not automatically install the application into Program Files or create desktop shortcuts.

**Be Safe. Be Secure!**


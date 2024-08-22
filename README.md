# Running the Streamlit Text-to-Speech Application

This guide will walk you through the process of setting up and running the Streamlit Text-to-Speech application on your local machine. These instructions are applicable for Windows, Linux, and macOS.

## Prerequisites

- Anaconda or Miniconda installed on your system. If you don't have it installed, download and install it from the [official Anaconda website](https://www.anaconda.com/products/distribution).

## Setup Instructions

### 1. Clone the Repository

First, clone the repository containing the Streamlit application to your local machine. If you haven't already, you can do this by running:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Replace `your-username` and `your-repo-name` with the appropriate values.

### 2. Create a Conda Environment

We'll create a new conda environment with Python 3.9.19. Open your terminal (Command Prompt or Anaconda Prompt on Windows, Terminal on macOS or Linux) and run the following commands:

```
conda create -n tts_app python=3.9.19
```

This command creates a new conda environment named `tts_app` with Python 3.9.19.

### 3. Activate the Conda Environment

Activate the newly created environment:

- On Windows:
  ```
  conda activate tts_app
  ```

- On macOS and Linux:
  ```
  source activate tts_app
  ```

### 4. Install Required Packages

With the environment activated, install the required packages. Make sure you're in the directory containing the `requirements.txt` file, then run:

```
pip install -r requirements.txt
```

This will install all the necessary dependencies for the Streamlit application.

### 5. Run the Streamlit Application

Now you're ready to run the Streamlit application. In the same terminal, with the `tts_app` environment still activated, run:

```
streamlit run streamlit_tts_app.py
```

This command will start the Streamlit server and should automatically open the application in your default web browser. If it doesn't open automatically, the terminal will display a local URL (usually `http://localhost:8501`) which you can copy and paste into your web browser.

## Troubleshooting

- If you encounter any issues with package installations, make sure your conda environment is activated and try updating pip:
  ```
  pip install --upgrade pip
  ```
  Then attempt to install the requirements again.

- If you face any "command not found" errors, ensure that you have activated the conda environment correctly.

- For any other issues, please check the error messages in the terminal for specific details and try searching for solutions online or consult the documentation of the relevant packages.

## Closing the Application

To stop the Streamlit application, you can press `Ctrl+C` in the terminal where it's running.

To deactivate the conda environment when you're done, simply run:

```
conda deactivate
```

## Additional Notes

- Remember to activate the `tts_app` conda environment each time you want to run the application.
- Keep your environment up to date by periodically running `pip install -r requirements.txt` in case any dependencies are updated.

If you encounter any problems or have any questions, please open an issue in the GitHub repository. Happy text-to-speech converting!
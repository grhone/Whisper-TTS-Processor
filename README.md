# Text-to-Speech Processor - OpenAI Whisper

This Python script converts text from a file into spoken word audio using OpenAI's GPT models. It supports standard and high-definition voice synthesis.

## Requirements

- Python 3.6 or higher
- A virtual environment (recommended)
- An OpenAI API key

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Set up a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

4. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

- Create a `.env` file in the project root directory.
- Add your OpenAI API key to the .env file:

```makefile
OPENAI_API_KEY=your_api_key_here
```

## Usage
Run the script using the following command:

```bash
python path/to/script.py
```

### Options
- `--hd`: Use the high-definition voice synthesis model (tts-1-hd).

The script reads a text file named `script.txt` located in the same directory as the script and generates an MP3 file for each line of text. The files are named speech_1.mp3, speech_2.mp3, etc.

Ensure the `script.txt` file exists in the same directory as the script, containing the text you wish to convert to speech.

## Output

The generated audio files are saved in the script's directory, named according to their corresponding line numbers in the `script.txt` file.
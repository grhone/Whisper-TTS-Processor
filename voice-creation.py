from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv
from colorama import Fore
from colorama import init
import argparse 

init(convert=True)

# Load the environment variables from .env file
load_dotenv()

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Process the -h flag for HD voice.")
# Use --hd to avoid conflict with the conventional help flag -h
parser.add_argument("--hd", help="Use tts-1-hd model for high-definition voice synthesis", action="store_true")
args = parser.parse_args()

# Determine the model based on the presence of the --hd flag
model = "tts-1-hd" if args.hd else "tts-1"

print(f"{Fore.CYAN}Model: {Fore.LIGHTBLACK_EX}{model}")

api_key=os.environ.get("OPENAI_API_KEY")

print(f"{Fore.CYAN}API Key: {Fore.LIGHTBLACK_EX}{api_key}{Fore.WHITE}")

print(f"{Fore.CYAN}Loading OpenAPI client...{Fore.WHITE}")

client = OpenAI( api_key=api_key )

script_file_path = Path(__file__).parent / "script.txt"

print(f"{Fore.CYAN}Script file: {Fore.LIGHTBLACK_EX}{script_file_path}{Fore.WHITE}")

print(f"{Fore.CYAN}Reading script file...{Fore.WHITE}")

if script_file_path.exists():
    with open(script_file_path, 'r', encoding='utf-8') as script_file:
        for index, line in enumerate(script_file.readlines(), start=1):
            line = line.strip()  # Remove any extra whitespace
            if line:  # Check if the line is not empty
                print(f"{Fore.CYAN}Processing line {index}: {Fore.LIGHTBLACK_EX}{line[:30]}...{Fore.WHITE}")
                speech_file_path = Path(__file__).parent / f"speech_{index}.mp3"
                response = client.audio.speech.create(
                    model=model,
                    voice="alloy",
                    input=line
                )
                response.stream_to_file(speech_file_path)
                print(f"{Fore.GREEN}Created file: {Fore.LIGHTBLACK_EX}{speech_file_path}{Fore.WHITE}")
else:
    print(f"{Fore.RED}The file 'script.txt' was not found in the script directory.{Fore.WHITE}")

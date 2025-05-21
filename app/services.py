import subprocess

def generate_linkedin_post(topic: str) -> str:
    prompt = f"Write a professional and engaging LinkedIn post about: {topic}"

    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama3.2:latest', prompt],
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'  # Specify encoding to avoid UnicodeDecodeError
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.strip() if e.stderr else str(e)
        return f"Error generating post: {error_message}"
    except FileNotFoundError:
        return "Error: Ollama CLI not found. Make sure Ollama is installed and in your PATH."

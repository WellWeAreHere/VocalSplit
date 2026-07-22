import subprocess
import os
import sys


def separate_audio(input_file: str):
    """
    Runs Demucs on the uploaded song.
    """

    output_dir = "output"

    os.makedirs(output_dir, exist_ok=True)

    command = [
        sys.executable,
        "-m",
        "demucs",
        input_file,
        "-o",
        output_dir,
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    print(result.stderr)

    result.check_returncode()

    return output_dir
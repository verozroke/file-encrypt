import os
from dotenv import load_dotenv
import subprocess


def obfuscate_directory(src_directory, output_directory):
    # Generate project configuration
    subprocess.run(["pyarmor", "gen", "-O", output_directory, src_directory])
    
    # Path to the generated configuration file
    config_path = os.path.join(output_directory, "pyarmor_config.json")
    
    # Apply the configuration to obfuscate the project
    subprocess.run(["pyarmor", "cfg", config_path])

if __name__ == "__main__":
    load_dotenv()
    src_directory = os.getenv('SOURCE_DIRECTORY')
    output_directory = os.getenv('OBFUCATION_OUTPUT_DIRECTORY')
    obfuscate_directory(src_directory, output_directory)

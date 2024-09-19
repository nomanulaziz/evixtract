import subprocess

def create_image(device, output):
    command = [
        'dd', f'if={device}', f'of={output}', 'bs=4M', 'status=progress'
    ]
    subprocess.run(command)
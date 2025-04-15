import subprocess


def get_last_command():
    with open("/home/nabeel/.zsh_history", "r") as file:
        lines = file.readlines()
        last_line = lines[-2] if lines else ""

    index = last_line.find(";") + 1

    if index != -1:
        last_line = last_line[index:]

    return last_line


def correct_command(command_words, correct_word):
    command_words.pop(0)
    command_words.insert(0, correct_word)
    result = " ".join(command_words)
    return result


def run_command(command):
    subprocess.run(command, shell=True)

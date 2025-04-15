import defs
import difflib

commands = ["mkdir", "ls", "cd", "nvim", "touch", "cat", "pwd", "cp", "mv"]
command = defs.get_last_command()
command_words = command.split(" ")
first_command_word = command_words[0]

correct_word = difflib.get_close_matches(first_command_word, commands, 1, 0.5)
correct_word = correct_word[0] if correct_word else ""

correct_cmd = defs.correct_command(command_words, correct_word)

defs.run_command(correct_cmd)

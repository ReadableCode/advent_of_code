# %%
# Imports #


# %%
# Vars #


def get_text_input_lines(file_path, debug=False):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    if debug:
        print("-------- text file contents --------")
        for text_line in text_lines:
            print(text_line)
        print("------------------------------------")

    return text_lines



def get_problems(file_path):
    ls_problems = []
    
    ls_rows = get_text_input_lines(file_path)
    
    for row in ls_rows:
        


# %%

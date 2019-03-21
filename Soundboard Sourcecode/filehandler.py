def get_button_info(number):
    with open("songs.csv", "r") as fp:
        for i, line in enumerate(fp, start=1):
            if i == number:
                line = line.strip()
                line = line.split(", ")
                return line


def create_empty_file():
    with open("songs.csv", "w") as fp:
        for i in range(1, 10):
            fp.write(",\n")


def is_file_there():
    try:
        with open("songs.csv", "r"):
            pass
    except Exception:
        create_empty_file()


def save_values(row, name, adress):
    lines = []
    string = name + ", " + adress
    with open("songs.csv", "r") as fp:
        for line in fp:
            lines.append(line.strip())
    currentline = 1
    with open("songs.csv", "w") as fp:
        for line in lines:
            if currentline == row:
                fp.write(string + "\n")
            else:
                fp.write(line + "\n")
            currentline = currentline + 1


def delete_value(row):
    lines = []
    with open("songs.csv", "r") as fp:
        for line in fp:
            lines.append(line.strip())
    currentline = 1
    with open("songs.csv", "w") as fp:
        for line in lines:
            if currentline == row:
                fp.write(",\n")
            else:
                fp.write(line + "\n")
            currentline = currentline + 1

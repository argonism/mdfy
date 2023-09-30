def write(content, filepath):
    with open(filepath, "w") as file:
        for item in content:
            file.write(str(item) + "\n")


class Mdfy:
    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, content):
        with open(self.filepath, "w") as file:
            for item in content:
                file.write(str(item) + "\n")

def write(content, filepath):
    with open(filepath, "w") as file:
        for item in content:
            file.write(str(item) + "\n")


class Mdfy:
    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def write(self, content):
        with open(self.filepath, "w") as file:
            for item in content:
                file.write(str(item) + "\n")

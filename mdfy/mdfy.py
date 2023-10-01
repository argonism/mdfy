def write(content, filepath):
    with open(filepath, "w") as file:
        for item in content:
            file.write(str(item) + "\n")


class Mdfier:
    def __init__(self, filepath):
        self.filepath = filepath

    @classmethod
    def stringify(cls, content):
        return "\n".join([str(item) for item in content])

    def write(self, content):
        markdown = self.stringify(content)
        with open(self.filepath, "w") as file:
            file.write(markdown + "\n")

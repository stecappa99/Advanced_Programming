
morse_list = ["._", "_...", "_._.", "_..",
              ".", ".._.", "__.", "....",
              "..", ".___", "_._", "._..",
              "__", "_.", "___", ".__.",
              "__._", "._.", "...", "_",
              ".._", "..._", ".__", "_.._"
              "_.__", "__.."]


class Node:
    def __init__(self, morse_value, value):
        self._val = value
        self._morse_value = morse_value
        self._nodes = []

    def add_node(self, node):
        self._nodes.append(node)

    def set_val(self, value):
        self._val = value

    def nodes_contains(self, value):
        return False if len(self._nodes) == 0 or (value != self._nodes[0].get_morse_value() and value != self._nodes[1].get_morse_value()) else True

    def get_morse_value(self):
        return self._morse_value

    def next_node(self, value):
        return self._nodes[0] if value == self._nodes[0].get_morse_value() else self._nodes[1]

    def __str__(self):
        return f"Value: {self._val}\nMorse: {self._morse_value}\nNodes:{len(self._nodes)}"

class Morse:

    def __init__(self):
        self.build_morse_tree()


    def build_morse_tree(self):
        tree = [Node(".", ""), Node("_", ""), Node("u", ""), Node(" ", " ")]
        def build(pos, val, node):
            if len(val) > 0:
                if not node.nodes_contains(val[0]):
                    node.add_node(Node(val[0], ""))
                build(pos, val[1:], node.next_node(val[0]))
            else:
                node.set_val(chr(pos + ord('A')))

        for i in range(len(morse_list)):
            node = tree[0] if morse_list[i][0] == tree[0].get_morse_value() else tree[1]
            build(i, morse_list[i], node)
            print(node)

if __name__ == "__main__":
    m = Morse()





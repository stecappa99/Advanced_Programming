
morse_list = ["._", "_...", "_._.", "_..",
              ".", ".._.", "__.", "....",
              "..", ".___", "_._", "._..",
              "__", "_.", "___", ".__.",
              "__._", "._.", "...", "_",
              ".._", "..._", ".__", "_.._",
              "_.__", "__.."]


class Node:
    def __init__(self, morse_value, value):
        self._val = value
        self._morse_value = morse_value
        self._dot = None
        self._dash = None

    def set_dot(self):
        self._dot = Node(".", "")

    def set_dash(self):
        self._dash = Node("_", "")

    def set_val(self, value):
        self._val = value

    def get_morse_value(self):
        return self._morse_value

    def get_value(self):
        return self._val

    def next_node(self, value):
        return self._dot if value == "." else self._dash

    def set_next_node(self, value):
        if value == ".":
            self.set_dot()
        else:
            self.set_dash()

    def __str__(self):
        return f"\nValue: {self._val}\tMorse: {self._morse_value}\tDot: {self._dot}\tDash: {self._dash}"


class Morse:

    def __init__(self):
        self._tree = []
        self.build_morse_tree()

    def build_morse_tree(self):
        self._tree = [Node(".", ""), Node("_", "")]

        def build(pos, val, node):
            if len(val) > 0:
                if node.next_node(val[0]) is None:
                    node.set_next_node(val[0])
                build(pos, val[1:], node.next_node(val[0]))
            else:
                node.set_val(chr(pos + ord('A')))

        for i in range(len(morse_list)):
            node = self._tree[0] if morse_list[i][0] == self._tree[0].get_morse_value() else self._tree[1]
            build(i, morse_list[i], node)

    def encode(self, plain_text):
        sup = ""
        for i in range(len(plain_text)):
            if plain_text[i] != " ":
                sup += morse_list[ord(plain_text[i]) - ord("A")]
                if i < len(plain_text) - 1 and plain_text[i + 1] != " ":
                    sup += "u"
            else:
                sup += " "
        return sup

    def visit_tree(self, node, cod):
        return node.get_value() if len(cod) <= 0 else self.visit_tree(node.next_node(cod[0]), cod[1:])

    def get_node(self, value):
        for node in self._tree:
            if node.get_morse_value() == value:
                return node
        return None

    def decode(self, coded):
        return " ".join(["".join([self.visit_tree(self.get_node(w[0]), w) for w in word.split("u")]) for word in coded.split()])


if __name__ == "__main__":
    M = Morse()
    print(f"SOS SAVE THE DEVS CHATGPT RULEZ, {M.encode('SOS SAVE THE DEVS CHATGPT RULEZ')}")
    print(f"....u.u._..u._..u___ .__u___u._.u._..u_.., {M.decode('....u.u._..u._..u___ .__u___u._.u._..u_..')}")




#! python

class TrieNode(object):
    def __init__(self, root, is_word):
        self.table = {}
        self.root = root
        self.is_word = is_word

    def append_all(self, items):
        if items:
            for item in items:
                if item is "":
                    t = TrieNode("", True)
                    self.table[""] = t
                elif item[0] not in self.table:
                    if len(item) > 1:
                        t = TrieNode(item[0], False)
                        self.table[item[0]] = t
                        t.append_all([item[1:],])
                    else:
                        t = TrieNode(item[0], True)
                        self.table[item[0]] = t

                else:
                    t = self.table[item[0]]
                    if len(item) > 1:
                        t.append_all([item[1:],])
                    else:
                        t.is_word = True

    def size(self):
        return len(self.table)

    def get(self, item, is_prefix=False, counter=0):
        if not is_prefix:
            if item:
                if item is "":
                    return ""
                elif item[0] in self.table:
                    t = self.table[item[0]]
                    if len(item) > 1:
                        return str(t.root) + str(t.get(item[1:]))
                    else:
                        return str(t.root)
                else:
                    return ""
        else:
            if item:
                if item is "":
                    return ""
                elif item[0] in self.table:
                    # print(self.table)
                    t = self.table[item[0]]
                    if len(item) > 1:
                        return str(t.root) + str(t.get(item[1:], is_prefix))
                    else:
                        total = str(t.root)
                        for item2 in t.table:
                            total += ", "+ str(counter) + str(t.get(item2, is_prefix, counter + 1))
                        return total
                else:
                    return ""
    def __str__(self):
        return self.root

    def __repr__(self):
        """Return a string representation of this hash table."""
        return self.root

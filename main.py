# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from node import Node, Trie

the_trie = Trie()
the_trie.insert("a")
the_trie.insert("and")
the_trie.insert("anti")
the_trie.insert("anthem")

print(the_trie.keys_starting_with("an"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

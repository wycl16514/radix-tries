CHILD_NUM = 26

class Node:
    def __init__(self, key_node):
        self.key_node = key_node
        self.children = {}



class Trie:  # 字典树对象
    def __init__(self):
        self.root = Node(False)

    def __search(self, node, s):
        if s == "":
            return node.key_node

        if len(s) > 1:
            c, tail = s[0], s[1:]
        else:
            c, tail = s[0], ""

        if c in node.children:
            return self.__search(node.children[c], tail)

        return False

    def search(self, s):
        if self.root is None :
            return False
        else:
            return self.__search(self.root, s)

    def search_node(self, node, s):
        if s == "" :
            return node

        if len(s) > 1:
            c, tail = s[0], s[1:]
        else:
            c, tail = s[0], ""

        if (c in node.children) is False:
            return None
        else:
            return self.search_node(node.children[c], tail)

    def insert(self, s):
        return self.__insert(self.root, s)

    def __insert(self, node, s):
        if s == "": #所有边对应上，设置节点的key_node属性
            node.key_node = True
            return

        if len(s) > 1:
            c, tail = s[0], s[1:]
        else:
            c, tail = s[0], ""

        if c in node.children: #当前节点有和当前字符匹配的边
            return self.__insert(node.children[c], tail)
        else:
            return self.__add_new_branch(node, s) # 增加新的边与节点

    def __add_new_branch(self, node, s):
        if s == "":
            node.key_node = True
            return
        if len(s) > 1:
            c, tail = s[0], s[1:]
        else:
            c, tail = s[0], ""
        node.children[c] = Node(False) # 增加新的节点和边
        return self.__add_new_branch(node.children[c], tail)

    def __split(self, s):
        if len(s) > 1:
            c, tail = s[0], s[1:]
        else:
            c, tail = s[0], ""
        return c, tail

    def remove(self, s):
        return self.__remove(self.root, s)

    def __remove(self, node, s): # 该调用返回两个值，第一个用于表明当前节点是否被删除，第二个表明节点是否"悬挂"
        if s == "":
            deleted = node.key_node
            return deleted, len(node.children.keys()) == 0
        c, tail = self.__split(s)
        if c in node.children:
            deleted, dangling = self.__remove(node.children[c], tail)
            if deleted and dangling:
                del node.children[c]
                if deleted is True and len(node.children.keys()) > 0:
                    dangling = False
                return deleted, dangling # 当前节点是实心点或含有其他分支
            else:
                return False, False

    def longest_prefix(self, s):
        prefix = ""
        return self.__longest_prefix(self.root, s, prefix)

    def __longest_prefix(self, node, s, prefix):
        if s == "":
            if node.key_node:  # 这里意味着输入字符串是存储在树中的单词
                return prefix
            else:
                return None

        c, tail = self.__split(s)
        if (c in node.children) is False:
            if node.key_node: # 找到最长匹配的单词
                return prefix
            else:
                return None  # 当前树中不存在与给定字符串形成前缀匹配的单词
        else:
            result = self.__longest_prefix(node.children[c], tail, prefix + c)  # 看看能不能再多匹配一个字符
            if result is not None:
                return result
            elif node.key_node: # 不能继续多匹配字符，而且当前节点是实心，那么当前节点对应的字符串就是最长匹配字符
                return prefix
            else:
                return None

    def keys_starting_with(self, prefix):
        node = self.search_node(self.root, prefix)
        if node is None:
            return []
        else:
            return self.__all_keys(node, prefix)

    def __all_keys(self, node, prefix):
        keys = []
        if node.key_node:
            keys.append(prefix) # 输入的前缀字符串是当前节点的前缀
        for c in node.children.keys():
            keys += self.__all_keys(node.children[c], prefix + c) # 在当前单词基础上延长一个字符然后看给定字符串是否是存在树中的单词
        return keys






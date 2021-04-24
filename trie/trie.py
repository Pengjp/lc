a_val = ord('a')

class Node:
    def __init__(self):
        self.pass_cnt = 0
        self.end_cnt = 0
        self.nexts = [None] * 26

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        if not word:
            return
        node = self.root
        node.pass_cnt += 1
        for chr in word:
            path = ord(chr) - a_val
            if not node.nexts[path]:
                node.nexts[path] = Node()
            node = node.nexts[path]
            node.pass_cnt += 1
        node.end_cnt += 1

    def delete(self, word):
        if self.search(word):
            node = self.root
            node.pass_cnt -= 1
            for chr in word:
                path = ord(chr) - a_val
                node.nexts[path].pass_cnt -= 1
                if node.nexts[path].pass_cnt == 0:
                    node.nexts[path] = None
                    return
                node = node.nexts[path]
        node.end_cnt -= 1

    def search(self, word):
        node = self.root
        for chr in word:
            path = ord(chr) - a_val
            if node.nexts[path]:
                node = node.nexts[path]
            else:
                return False
        return node.end_cnt > 0

    def prefixNumber(self, pre):
        node = self.root
        for chr in pre:
            path = ord(chr) - a_val
            if not node.nexts[path]:
                return 0
            node = node.nexts[path]
        return node.pass_cnt

trie = Trie()
word = 'abc'
trie.insert(word)
trie.insert(word)
print(trie.prefixNumber('abcd'))
# if trie.search(word): print('found')
# else: print('not found')
#
# word = 'abcd'
# trie.insert(word)
#
# if trie.search(word): print('found')
# else: print('not found')
#
# if trie.search('a'): print('found')
# else: print('not found')
#
# if trie.search('abcde'): print('found')
# else: print('not found')
#
# trie.delete('abc')
# if trie.search('abc'): print('found')
# else: print('not found')
#
# trie.delete('abc')
# if trie.search('abc'): print('found')
# else: print('not found')

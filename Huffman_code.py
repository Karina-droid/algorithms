import heapq

class Node:
    def __init__(self, symbol=None, freq=None):
        self.symbol = symbol
        self.freq = freq
        self.right = None
        self.left = None
        self.huff = ''  #tree direction (0/1)

    def __lt__(self, next):
        return self.freq < next.freq

def build_Huffman_tree(chars, freq):
    #create a priority queue of nodes
    priority_queue = [Node(chars, freq) for c, f in zip(chars, freq)]
    heapq.heapify(priority_queue)

    while(len(priority_queue) > 1):
        left_child = priority_queue.pop()
        right_child = priority_queue.pop()
        merged_node = Node(freq = left_child.freq + right_child.freq)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_huffman_codes(node, code="", huffman_codes={}):
    if node != None:
        if node.symbol != None:
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)
    return huffman_codes


import tkinter
from tkinter import filedialog
from tkinter import messagebox

'''def is_empty(queue):
    if len(queue) == 0:
        return True
    return False

def enqueue(queue, element):
    # If queue is empty, then directly insert without any comparison
    if is_empty(queue):
        queue.append(element)
    else:
        # Loop to check where frequency of current element in queue becomes greater than frequency of element passed
        found = False
        for i in range(len(queue)):
            # queue[i] gets the tuple. Queue[i][0] gets its frequency
            if element[0] < queue[i][0]:
                queue.insert(i, element)
                found = True
                break
        if not found:
            queue.append(element)
    return queue'''


'''def count_frequency2(text):
    # Counts the number of times letters appear in a text
    frequency = {}
    prev=""
    for char in text:
        if char != " ":
            if char in frequency:
                if char==prev:
                    ok=frequency[char].pop()
                    ok+=1
                    frequency[char].append(ok)
                    prev=char
                else:
                    frequency[char].append(1)
                    prev=char
            else:
                frequency[char] = [1]
                prev=char
    return frequency'''



'''def build_huffman_tree(frequency):
    # Create a priority queue that stores the letters and their frequency in ascending order
    priority_queue = []
    for char in frequency:
        priority_queue = enqueue(priority_queue, (frequency[char], char))
    # print(priority_queue)

    while len(priority_queue) > 1:
        left = None
        right = None
        left_index = 0
        for i in range(2):
            minimum = 999
            if i == 1:
                priority_queue.remove(left)
            for element in priority_queue:
                if i == 0:
                    if type(element) == dict and element["value"] < minimum:
                        left = element
                        minimum = element["value"]
                        left_index = priority_queue.index(element)
                    elif type(element) == tuple and element[0] < minimum:
                        left = element
                        minimum = element[0]
                        left_index = priority_queue.index(element)
                
                
                else:
                    if type(element) == dict and element["value"] <= minimum:
                        right = element
                        minimum = element["value"]
                    elif type(element) == tuple and element[0] <= minimum:
                        right = element
                        minimum = element[0]
        priority_queue.remove(right)

        # left = priority_queue[0]
        # right = priority_queue[1]
        if type(left) == tuple:
            left_freq = left[0]
            left = left[1]
            tree = {"value" : left_freq, "left" : {"char" : left, "value": left_freq}, "left" : {}, "right" : {}}
        else:
            left_freq = left["value"]
            tree = {"value" : left_freq, "left" : left}
        if type(right) == tuple:
            right_freq = right[0]
            right = right[1]
            tree["value"] = tree["value"] + right_freq
            tree["right"] = {"value" : right, "left" : {}, "right" : {}}
        else:
            right_freq = right["value"]
            tree["value"] = tree["value"] + right_freq
            tree["right"] = right
        # priority_queue = [tree] + priority_queue[2:]
        priority_queue = priority_queue[0 : left_index] + [tree] + priority_queue[left_index : ]

    return priority_queue[0]'''

'''def compressed_code(table,order_freq):
    byte=""
    check=True
    while check==True:
        check=False
        for i in table:
            if type(order_freq[i])==int:
                check=True
                byte+=table[i]*order_freq[i]
                order_freq[i]=[]
                print(order_freq)
            elif type(order_freq[i])==list:
                if order_freq[i]==[]:
                    continue
                check=True
                byte+=table[i]*order_freq[i].pop(0)
                print(order_freq)
    return byte
def compressed_code2(table,order_freq):
    byte=""
    check=True
    while check==True:
        check=False
        for i in table:
            if type(order_freq[i])==int:
                check=True
                byte+=table[i]*order_freq[i]
                order_freq[i]=[]
                print(order_freq)
            elif type(order_freq[i])==list:
                if order_freq[i]==[]:
                    continue
                check=True
                byte+=table[i]*order_freq[i].pop(0)
                print(order_freq)
    return byte'''


def count_frequency(text):
    # Counts the number of times letters appear in a text
    frequency = {}
    for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

def count_frequency3(text):
    # Counts the number of times letters appear in a text
    frequency = []
    temp=[]
    prev=""
    for char in text:
            if char in temp:
                if char==prev:
                    ok=frequency.pop()
                    new=ok[1]+1
                    frequency.append((char,new))
                    prev=char
                else:
                    temp.append(char)
                    frequency.append((char,1))
                    prev=char
            else:
                temp.append(char)
                frequency.append((char,1))
                prev=char
    return frequency

def build_huffman_tree(frequency):
    nodes = [{'char': c, 'value': f} for c, f in frequency.items()]
    while len(nodes)>1:
        nodes = sorted(nodes, key=lambda x: x['value'])
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = {'value': left['value'] + right['value'], 'left': left, 'right': right}
        nodes.append(parent)
    return nodes[0]

def traverse_tree(node, encoding_table, code=''):
    if 'char' in node: 
        encoding_table[node['char']] = code
    else: 
        traverse_tree(node['left'], encoding_table, code + '0')
        traverse_tree(node['right'], encoding_table, code + '1')

def build_encoding_helper(huffman_tree):
    encoding_table = {}
    traverse_tree(huffman_tree, encoding_table)
    return encoding_table

def build_encoding_table(table,freq):
    final_table={}
    while len(final_table)!=len(table):
        for i in freq:
            for j in table:
                if i==j:
                    final_table[i]=table[j]
                else:
                    continue
    return final_table

def decompress(encoded_text, encoding_table):
    current_code = ''
    decoded_text = ''
    for bit in encoded_text:
        current_code += bit
        for char, code in encoding_table.items():
            if current_code == code:
                decoded_text += char
                current_code = ''
                break
    return decoded_text


def compressed_code3(table,freq):
    byte=""
    while len(freq)!=0:
        i=freq[0]
        key=i[0]
        val=i[1]
        byte+=table[key]*val
        freq.pop(0)
    return byte

def add_padding(encoded_text):
    count = 0
    while len(encoded_text) % 8 != 0:
        encoded_text += "0"
        count += 1
    binary = bin(count)[2:].zfill(8)
    encoded_text = binary + encoded_text
    return encoded_text

def get_integer_array(encoded_text):
    array = []
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i+8]
        array.append(int(byte, 2))
    return array
def remove_padding(encoded_text):
    padding_info = encoded_text[:8]
    amount_of_padding = int(padding_info, 2)
    encoded_text_without_padding = encoded_text[8 : len(encoded_text) - amount_of_padding]
    return encoded_text_without_padding

def decompress_file():
    path = filedialog.askopenfilename()
    if not path.endswith(".bin"):
        messagebox.showerror("Error", "Please enter a compressed file")
        close()
        return
    filename = path.split("/")[-1].split(" ")[0]
    bits = ""
    with open(path, "rb") as file:
        file_content = file.read(1)
        while file_content:
            int_value = ord(file_content)
            binary_value = bin(int_value)[2:].zfill(8)
            bits += binary_value
            file_content = file.read(1)
        encoded_text_without_padding = remove_padding(bits)
        # new_path = path.rstrip(filename + " Compressed.txt")
        for i in range(len(path) - 1, 0, -1):
            if path[i] == "/":
                new_path = path[0 : i + 1]
                break

        with open(new_path + filename + ".txt", "r") as new_file:
            original_file_content = new_file.read()
            freq = count_frequency(original_file_content)
            freq3 = count_frequency3(original_file_content)
            tree = build_huffman_tree(freq)
            temptable=build_encoding_helper(tree)
            table = build_encoding_table(temptable,freq)
            with open(new_path + filename + " Decompressed.txt", "w") as output_file:
                output_file.write(decompress(encoded_text_without_padding, table))

    messagebox.showinfo("Success", "File Decompressed Successfully")
    close()

def close():
    root.quit()

def compress():
    path = filedialog.askopenfilename()
    if not path.endswith(".txt"):
        messagebox.showerror("Error", "Please enter a decompressed text file")
        close()
        return()
    filename = path.split("/")[-1].split(".")[0]
    with open(path, "r") as file:
        file_content = file.read()
        freq = count_frequency(file_content)
        # print("freq:", freq)
        freq3 = count_frequency3(file_content)
        # print("freq3:", freq3)
        tree = build_huffman_tree(freq)
        # print("Tree:",tree)
        temptable=build_encoding_helper(tree)
        # print("temptable:", temptable, "\n")
        table = build_encoding_table(temptable,freq)
        # print("final table:", table, "\n")
        byte = compressed_code3(table,freq3)
        padded_text = add_padding(byte)
        int_array = get_integer_array(padded_text)

        # path = path.rstrip("/" + filename + ".txt")
        for i in range(len(path) - 1, 0, -1):
            if path[i] == "/":
                path = path[0 : i + 1]
                break

        with open(path + "/" + filename + " Compressed.bin", "wb") as output_file:
            output_file.write(bytes(int_array))
    messagebox.showinfo("Success", "File Compressed Successfully")
    close()

root = tkinter.Tk()
root.geometry("350x350")
root.configure(bg="light blue")

label = tkinter.Label(text = "File Compression Using Huffman", pady=50, font=("", 12), fg="black", bg="light blue")
label.pack()

compress_btn = tkinter.Button(text="Compress", width=10, height=1, command=compress)
compress_btn.place(x=50, y=130)

decompress_btn = tkinter.Button(text="Decompress", width=10, height=1, command=decompress_file)
decompress_btn.place(x=200, y=130)

root.mainloop()
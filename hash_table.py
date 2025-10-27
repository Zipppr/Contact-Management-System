class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    '''

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)

        node = self.data[index]

        # If empty bucket
        if node is None:
            self.data[index] = Node(key, new_contact)
            return

        # Traverse linked list
        prev = None
        while node:
            # If contact already exists → update number
            if node.key == key:
                node.value.number = number
                return
            prev = node
            node = node.next

        # Add new node at end
        prev.next = Node(key, new_contact)

    def search(self, key):
        index = self.hash_function(key)
        node = self.data[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            node = self.data[i]
            if not node:
                print("Empty")
                continue
            while node:
                print(f"- {node.value}", end=" ")
                node = node.next
            print()


# ------------------ TESTING ------------------

table = HashTable(10)
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.print_table()

print("\nSearch Result:", table.search("John"))

table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")
table.insert("Rebecca", "999-444-9999")  # update

table.print_table()
print(table.search("Chris"))  # None

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def __repr__(self):
#         return f'Node({repr(self.value)})'

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def __str__(self):
#         r = ""
#         cur = self.head

#         while cur is not None:
#             r += f'({cur.value})'
#             if cur.next is not None:
#                 r += ' -> '

#             cur = cur.next

#         return r

#     def insert_at_head(self, node):
#         node.next = self.head
#         self.head = node

#     def find(self, value):
#         cur = self.head

#         # walk the linked list
#         while cur is not None:
#             if cur.value == value:
#                 # Found it!
#                 return cur

#             cur = cur.next

#         return None

#     def delete(self, value):
#         cur = self.head

#         # Special case of deleting the head of the list

#         if cur.value == value:
#             self.head = self.head.next
#             return cur

#         # General case

#         prev = cur
#         cur = cur.next

#         while cur is not None:
#             if cur.value == value:  # Delete this one
#                 prev.next = cur.next   # Cuts out the old node
#                 return cur

#             else:
#                 prev = prev.next
#                 cur = cur.next

#         return None

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # self.bucket = [None for i in range(capacity)]
        # self.bucket = [LinkedList()] * self.capacity <- changed my mind on this
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
            self.bucket = [None] * self.capacity
        else:
            self.capacity = capacity
            self.capacity = MIN_CAPACITY
            self.bucket = [None] * self.capacity
        self.overload = 0.7
        self.underload = 0.2
        self.count = 0
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # return len(self.bucket)
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.overload

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    # this is the hashing function-------------------------------
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

#     def my_hashing_function(s):
#     string_bytes = s.encode()
# ​
#     total = 0
# ​
#     for b in string_bytes:
#         total += b
# ​
#     return total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # self.bucket[slot] = HashTableEntry(key, value)
        # -------------------------------------------------------

        # number of things stored in the hash table / number of slots in the array
        # When computing the load, keep track of the number of items in the hash table as
        # you go.
        # * When you put a new item in the hash table, increment the count
        # * When you delete an item from the hash table, decrement the count
        # When is the hash table overloaded?
        # * It's overloaded when load factor > 0.7
        # * It's underloaded when load factor < 0.2 (Stretch)

        # Allocate a new array of bigger size, typically double the previous size
        #  (or half the size if resizing down, down to some minimum)
        # if self.count / self.get_num_slots() < self.overload:
        #     self.resize(self.capacity * 2)

        # self.bucket[self.hash_index(key)] for reference
        # since we have to do searching for the key implement something similiar to delete in singly linked list except change value
        slot = self.hash_index(key)

        # search bucket for that hash index
        cur = self.bucket[slot]

        # If the position is None make a hashtable entry at that location
        if cur is None:
            self.bucket[slot] = HashTableEntry(key, value)
        # if that index already has a hashtable entry there
        else:
            while cur is not None:
                # check to see if those keys match
                if cur.key == key:
                    # if they do match change that value
                    cur.value = value
                    return
                # *****keeps the loop going steping throught the values****    
                previous = cur
                cur = cur.next
            
            # if there is no key to match and the location is not empty
            cur = HashTableEntry(key, value)
            # set the previous.next pointer to point to current value
            previous.next = cur
        self.count += 1 

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # hash_entry = self.bucket[slot]
        # if hash_entry is not None:
        #     self.put(key, None)
        # return print('Warning Entry Not Found')
#----------------------------------------------------------------------
# number of things stored in the hash table / number of slots in the array
        # When computing the load, keep track of the number of items in the hash table as
        # you go.
        # * When you put a new item in the hash table, increment the count
        # * When you delete an item from the hash table, decrement the count <----------
        # When is the hash table overloaded?
        # * It's overloaded when load factor > 0.7
        # * It's underloaded when load factor < 0.2 (Stretch)<---------------------------

        # Allocate a new array of bigger size, typically double the previous size
        #  (or half the size if resizing down, down to some minimum)
        # if self.count / self.get_num_slots() < self.underload:
        #     if self.get_num_slots() // 2 >= 8:
        #         self.resize(self.capacity // 2)
                
        # self.bucket[self.hash_index(key)] for reference

        # since we have to do searching for the key implement something similiar to delete in singly linked
        slot = self.hash_index(key)

        # search bucket for that hash index
        cur = self.bucket[slot]

        # If the position is None make a give warning message
        # empty slot and no key here
        if cur is None:
            print('Warning Entry Not Found')
        # if that index already has a hashtable entry there
        else:
        # check to see if those keys match
            # check to see if the head key value matches
            while cur is not None:
                if cur.key == key:
                   cur.value = None
                   return
                # **keeps the loop going steping throught the values****    
                previous = cur
                cur = cur.next
            print('Warning Entry Not Found')
        # if self.count == 0:
        #     return
        # else:
        #     self.count -= 1
            

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # hash_entry = self.bucket[slot]
        # if hash_entry is not None:
        #     return hash_entry.value
        # return None
        slot = self.hash_index(key)
        #set the head
        cur = self.bucket[slot]
            # need to use while loop to continue the loop through the values with the next pointer
        while cur is not None:
            if cur.key == key:
                return cur.value
            # continue the loop
            cur = cur.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
#         Resize:
# In a nutshell, take everything out of the old hash table array, and put it in a
# new, resized array.
# 1. Allocate a new array of bigger size, typically double the previous size
#    (or half the size if resizing down, down to some minimum)
# 2. Traverse the old hash table -- O(n) over the number of elements in the hash
#    table
#    For each of the elements:
#       Figure it's slot in the bigger (or smaller), new array
#       Put it there
    # pass in new_capacity to current capacity
        self.capacity = new_capacity
        # set old to current self.bucket
        old = self.bucket
        # set the new size to [None] * self.capacity as i did before
        self.bucket = [None] * self.capacity
    # go through the previous list and pull out the item
        for item in old:
            # need to loop and use the next pointer to continue throught the list
            while item is not None:
                # can use our methods since we replaced self.bucket with out new items
                self.put(item.key, item.value)
                item = item.next

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

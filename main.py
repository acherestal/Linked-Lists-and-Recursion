from linked_list import LinkedList

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)

    print("Original list:")
    ll.display()

    print("Sum:", ll.recursive_sum())
    print("Search 10:", ll.recursive_search(10))
    print("Search 999:", ll.recursive_search(999))

    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()

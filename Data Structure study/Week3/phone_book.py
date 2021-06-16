class PhoneBook:
    def __init__(self):
        self.book = [None] * 10000000
        
    def Add(self, name, number):
        self.book[number] = name
        
    def Del(self, number):
        if self.book[number] is not None:
            self.book[number] = None
        
    def Find(self, number):
        if self.book[number] is None:
            return "not found"
        
        return self.book[number]

def process_queries(queries):
    for query in queries:
        q = query.split()
        cmd = q[0]
        number = int(q[1])
        if cmd == "add":
            phonebook.Add(q[2], number)
        elif cmd == "find":
            print(phonebook.Find(number))
        elif cmd == "del":
            phonebook.Del(number)

if __name__ == '__main__':
    phonebook = PhoneBook()
    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)

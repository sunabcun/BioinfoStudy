class Database:
    def __init__(self, n_tables, lines):
        self.n_tables = n_tables
        self.lines = lines
        #print("self lines: ", self.lines)
        self.ranks = [0] * n_tables
        self.parents = list(range(n_tables))
        self.max = max(self.lines)

    def merge(self, dst, src):
        dst_parent = self.get_parent(dst)
        #print("parents: ", self.parents)
        src_parent = self.get_parent(src)
        #print("parents: ", self.parents)
        #print("dst: ", dst, "src: ", src)
        #print("dst_parent: ", dst_parent, "src_parent: ", src_parent)
        
        if dst_parent == src_parent:
            return False
        
        if self.ranks[dst_parent] < self.ranks[src_parent]:
            self.parents[dst_parent] = self.parents[src_parent]
            self.lines[src_parent] += self.lines[dst_parent]
            self.lines[dst_parent] = 0
        
        else:
            self.parents[src_parent] = self.parents[dst_parent]
            self.lines[dst_parent] += self.lines[src_parent]
            self.lines[src_parent] = 0
            
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1
        
        self.max = max(self.max, self.lines[dst_parent], self.lines[src_parent])

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, table):
        if (table != self.parents[table]):
            self.parents[table] = self.get_parent(self.parents[table])
        
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    lines = list(map(int, input().split()))
    assert len(lines) == n_tables
    db = Database(n_tables, lines)
   
    for i in range(n_queries):
        dst, src = map(int, input().split())
       # print("before ranks :", db.ranks)
        #print("before parents: ", db.parents)
        db.merge(dst - 1, src - 1)
        #print("ranks :", db.ranks)
       
        print(db.max)


if __name__ == "__main__":
    main()

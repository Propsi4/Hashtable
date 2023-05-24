class Dictionary:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, value):
        return (sum(ord(char) for char in value)) % self.size
    def make_null(self):
        self.table = [[] for _ in range(self.size)]
    def insert(self, value):
        index = self._hash(value)
        self.table[index].append(value)

    def member(self, value):
        index = self._hash(value)
        for v in self.table[index]:
            if v == value:
                return True
        return False

    def delete(self, value):
        index = self._hash(value)
        for i, v in enumerate(self.table[index]):
            if v == value:
                del self.table[index][i]
                return
        raise KeyError(f"{value} not found")\

    def print(self):
        for index, cell in enumerate(self.table):
            if len(cell) > 0:
                values = []
                for item in cell:
                    values.append(item)
                    
                print(f"{index}: {values}")


if __name__ == "__main__":
    hashtable = Dictionary(50)
    names = ['Adam', 'Benjamin', 'Charles', 'David', 'Edward', 'Frank',
              'George', 'Henry', 'Isaac', 'James', 'Kevin', 'Luke', 'Matthew',
                'Nathan', 'Oliver', 'Peter', 'Quentin', 'Robert', 'Stephen', 'Thomas',
                  'Victor', 'William', 'Xavier', 'Yusuf', 'Zachary']

    for name in names:
        hashtable.insert(name)
    hashtable.delete("Isaac")
    hashtable.delete("Oliver")
    hashtable.print()
    print(hashtable.member("Nathan"))
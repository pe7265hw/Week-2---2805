class Author:
    def __init__(self, name):
        self.name = name
        self.books_published = []

    def publish(self, title):
        self.books_published.append(title)
        return self.books_published

    def __str__(self):
        if self.books_published:
            published= ", ".join(self.books_published)
            return f"{self.name}: {published}" 
        else:
            "This author has no books published."
    
a1 = Author("Stephen King")
a1.publish("Cujo")
a1.publish("IT")

print(a1)

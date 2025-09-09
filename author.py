from dataclasses import dataclass

class Author:
    #Initializing the Author class, accepts name, contains a list of books published
    def __init__(self, name):
        self.name = name
        self.books_published = []

    #Appends a title to the authors bibliography, does not add if the title already exists
    def publish(self, title):
        if title in self.books_published:
            print(f'Sorry, {title} is already in the authors bibliography!')
        else:
            self.books_published.append(title)
        return self.books_published

    #Prints a formatted statement of the author and their books
    def __str__(self):
        if self.books_published:
            published= ", ".join(self.books_published)
            return f"{self.name}: {published}" 
        else:
            "This author has no books published."
    


"""To be perfectly honest besides the decoration(?) of @dataclass im not exactly sure
what seperates a dataclass from a regular class, I did not realize we were supposed to
have watched the videos before class on monday and I did not get a chance to watch the videos.
My mistake, I'll make sure to be ready for next class."""
@dataclass
class Student:
    def __init__(self,name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa
    
    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, current GPA = {self.gpa}'
  

    
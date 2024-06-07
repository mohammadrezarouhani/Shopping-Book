from cgi import test
import random
from database.card import create_card
from database.category import create_category, update_category
from database.product import create_product
from faker import Faker

f = Faker()


def create_book():
    books = [
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "year": 1960,
            "price": 7.19,
        },
        {"title": "1984", "author": "George Orwell", "year": 1949, "price": 6.99},
        {
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "year": 1813,
            "price": 5.99,
        },
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "price": 10.29,
        },
        {
            "title": "Moby-Dick",
            "author": "Herman Melville",
            "year": 1851,
            "price": 9.99,
        },
        {
            "title": "War and Peace",
            "author": "Leo Tolstoy",
            "year": 1869,
            "price": 12.49,
        },
        {
            "title": "Crime and Punishment",
            "author": "Fyodor Dostoevsky",
            "year": 1866,
            "price": 11.29,
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "year": 1951,
            "price": 8.99,
        },
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "year": 1937,
            "price": 8.29,
        },
        {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "year": 1932,
            "price": 7.99,
        },
        {
            "title": "Anna Karenina",
            "author": "Leo Tolstoy",
            "year": 1877,
            "price": 12.99,
        },
        {
            "title": "The Adventures of Huckleberry Finn",
            "author": "Mark Twain",
            "year": 1884,
            "price": 7.59,
        },
        {
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "year": 1954,
            "price": 22.99,
        },
        {
            "title": "Alice's Adventures in Wonderland",
            "author": "Lewis Carroll",
            "year": 1865,
            "price": 5.49,
        },
        {
            "title": "Jane Eyre",
            "author": "Charlotte Bronte",
            "year": 1847,
            "price": 6.99,
        },
        {
            "title": "Wuthering Heights",
            "author": "Emily Bronte",
            "year": 1847,
            "price": 5.99,
        },
        {"title": "The Iliad", "author": "Homer", "year": -750, "price": 13.29},
        {"title": "The Odyssey", "author": "Homer", "year": -800, "price": 12.49},
        {
            "title": "Les Misérables",
            "author": "Victor Hugo",
            "year": 1862,
            "price": 14.99,
        },
        {
            "title": "Great Expectations",
            "author": "Charles Dickens",
            "year": 1861,
            "price": 8.49,
        },
        {
            "title": "The Divine Comedy",
            "author": "Dante Alighieri",
            "year": 1320,
            "price": 13.99,
        },
        {
            "title": "The Brothers Karamazov",
            "author": "Fyodor Dostoevsky",
            "year": 1880,
            "price": 12.49,
        },
        {
            "title": "Madame Bovary",
            "author": "Gustave Flaubert",
            "year": 1856,
            "price": 9.99,
        },
        {
            "title": "Don Quixote",
            "author": "Miguel de Cervantes",
            "year": 1605,
            "price": 15.99,
        },
        {
            "title": "The Picture of Dorian Gray",
            "author": "Oscar Wilde",
            "year": 1890,
            "price": 6.49,
        },
        {
            "title": "A Tale of Two Cities",
            "author": "Charles Dickens",
            "year": 1859,
            "price": 7.99,
        },
        {
            "title": "The Stranger",
            "author": "Albert Camus",
            "year": 1942,
            "price": 10.49,
        },
        {
            "title": "The Metamorphosis",
            "author": "Franz Kafka",
            "year": 1915,
            "price": 7.49,
        },
        {
            "title": "One Hundred Years of Solitude",
            "author": "Gabriel Garcia Marquez",
            "year": 1967,
            "price": 12.99,
        },
        {
            "title": "The Sound and the Fury",
            "author": "William Faulkner",
            "year": 1929,
            "price": 10.99,
        },
        {
            "title": "Frankenstein",
            "author": "Mary Shelley",
            "year": 1818,
            "price": 6.99,
        },
        {
            "title": "The Grapes of Wrath",
            "author": "John Steinbeck",
            "year": 1939,
            "price": 9.99,
        },
        {
            "title": "Heart of Darkness",
            "author": "Joseph Conrad",
            "year": 1899,
            "price": 7.49,
        },
        {"title": "Dracula", "author": "Bram Stoker", "year": 1897, "price": 6.99},
        {
            "title": "The Count of Monte Cristo",
            "author": "Alexandre Dumas",
            "year": 1844,
            "price": 13.99,
        },
        {"title": "Catch-22", "author": "Joseph Heller", "year": 1961, "price": 8.99},
        {
            "title": "The Sun Also Rises",
            "author": "Ernest Hemingway",
            "year": 1926,
            "price": 8.99,
        },
        {
            "title": "The Bell Jar",
            "author": "Sylvia Plath",
            "year": 1963,
            "price": 7.99,
        },
        {
            "title": "Of Mice and Men",
            "author": "John Steinbeck",
            "year": 1937,
            "price": 5.99,
        },
        {"title": "Lolita", "author": "Vladimir Nabokov", "year": 1955, "price": 11.99},
        {"title": "Beloved", "author": "Toni Morrison", "year": 1987, "price": 10.99},
        {
            "title": "Invisible Man",
            "author": "Ralph Ellison",
            "year": 1952,
            "price": 9.99,
        },
        {
            "title": "Rebecca",
            "author": "Daphne du Maurier",
            "year": 1938,
            "price": 8.49,
        },
        {
            "title": "Slaughterhouse-Five",
            "author": "Kurt Vonnegut",
            "year": 1969,
            "price": 7.99,
        },
        {
            "title": "Fahrenheit 451",
            "author": "Ray Bradbury",
            "year": 1953,
            "price": 9.99,
        },
        {
            "title": "The Old Man and the Sea",
            "author": "Ernest Hemingway",
            "year": 1952,
            "price": 6.99,
        },
        {"title": "The Shining", "author": "Stephen King", "year": 1977, "price": 8.99},
        {
            "title": "Gone with the Wind",
            "author": "Margaret Mitchell",
            "year": 1936,
            "price": 10.49,
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "year": 1988,
            "price": 9.99,
        },
        {"title": "On the Road", "author": "Jack Kerouac", "year": 1957, "price": 7.99},
        {
            "title": "A Clockwork Orange",
            "author": "Anthony Burgess",
            "year": 1962,
            "price": 8.49,
        },
        {
            "title": "East of Eden",
            "author": "John Steinbeck",
            "year": 1952,
            "price": 10.99,
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "year": 1951,
            "price": 8.99,
        },
        {
            "title": "To the Lighthouse",
            "author": "Virginia Woolf",
            "year": 1927,
            "price": 9.99,
        },
        {"title": "The Road", "author": "Cormac McCarthy", "year": 2006, "price": 8.99},
        {
            "title": "Middlemarch",
            "author": "George Eliot",
            "year": 1871,
            "price": 11.49,
        },
        {"title": "Siddhartha", "author": "Hermann Hesse", "year": 1922, "price": 7.49},
        {
            "title": "The Master and Margarita",
            "author": "Mikhail Bulgakov",
            "year": 1967,
            "price": 11.99,
        },
        {
            "title": "The Name of the Rose",
            "author": "Umberto Eco",
            "year": 1980,
            "price": 9.99,
        },
        {
            "title": "Watership Down",
            "author": "Richard Adams",
            "year": 1972,
            "price": 8.99,
        },
        {
            "title": "The Unbearable Lightness of Being",
            "author": "Milan Kundera",
            "year": 1984,
            "price": 9.99,
        },
        {"title": "Life of Pi", "author": "Yann Martel", "year": 2001, "price": 8.49},
        {
            "title": "Love in the Time of Cholera",
            "author": "Gabriel Garcia Marquez",
            "year": 1985,
            "price": 12.49,
        },
        {
            "title": "The Kite Runner",
            "author": "Khaled Hosseini",
            "year": 2003,
            "price": 10.49,
        },
        {
            "title": "Memoirs of a Geisha",
            "author": "Arthur Golden",
            "year": 1997,
            "price": 9.99,
        },
        {
            "title": "Never Let Me Go",
            "author": "Kazuo Ishiguro",
            "year": 2005,
            "price": 8.99,
        },
        {
            "title": "The Book Thief",
            "author": "Markus Zusak",
            "year": 2005,
            "price": 9.99,
        },
        {"title": "Atonement", "author": "Ian McEwan", "year": 2001, "price": 8.49},
        {"title": "The Road", "author": "Cormac McCarthy", "year": 2006, "price": 8.99},
        {
            "title": "The Girl with the Dragon Tattoo",
            "author": "Stieg Larsson",
            "year": 2005,
            "price": 9.99,
        },
        {
            "title": "The Help",
            "author": "Kathryn Stockett",
            "year": 2009,
            "price": 10.49,
        },
        {
            "title": "Shantaram",
            "author": "Gregory David Roberts",
            "year": 2003,
            "price": 13.99,
        },
        {"title": "The Road", "author": "Cormac McCarthy", "year": 2006, "price": 8.99},
        {
            "title": "The Curious Incident of the Dog in the Night-Time",
            "author": "Mark Haddon",
            "year": 2003,
            "price": 7.99,
        },
        {
            "title": "The Goldfinch",
            "author": "Donna Tartt",
            "year": 2013,
            "price": 11.99,
        },
        {
            "title": "The Night Circus",
            "author": "Erin Morgenstern",
            "year": 2011,
            "price": 9.99,
        },
        {
            "title": "The Fault in Our Stars",
            "author": "John Green",
            "year": 2012,
            "price": 8.49,
        },
        {"title": "Gone Girl", "author": "Gillian Flynn", "year": 2012, "price": 9.49},
        {
            "title": "The Girl on the Train",
            "author": "Paula Hawkins",
            "year": 2015,
            "price": 10.99,
        },
        {
            "title": "All the Light We Cannot See",
            "author": "Anthony Doerr",
            "year": 2014,
            "price": 12.49,
        },
        {
            "title": "Big Little Lies",
            "author": "Liane Moriarty",
            "year": 2014,
            "price": 9.99,
        },
        {
            "title": "The Underground Railroad",
            "author": "Colson Whitehead",
            "year": 2016,
            "price": 10.49,
        },
        {
            "title": "Little Fires Everywhere",
            "author": "Celeste Ng",
            "year": 2017,
            "price": 9.99,
        },
        {
            "title": "Where the Crawdads Sing",
            "author": "Delia Owens",
            "year": 2018,
            "price": 11.99,
        },
        {
            "title": "The Silent Patient",
            "author": "Alex Michaelides",
            "year": 2019,
            "price": 9.99,
        },
        {
            "title": "Normal People",
            "author": "Sally Rooney",
            "year": 2018,
            "price": 8.49,
        },
        {"title": "Educated", "author": "Tara Westover", "year": 2018, "price": 12.99},
        {
            "title": "The Vanishing Half",
            "author": "Brit Bennett",
            "year": 2020,
            "price": 10.49,
        },
        {
            "title": "The Midnight Library",
            "author": "Matt Haig",
            "year": 2020,
            "price": 9.99,
        },
        {
            "title": "The Giver of Stars",
            "author": "Jojo Moyes",
            "year": 2019,
            "price": 9.99,
        },
        {
            "title": "American Dirt",
            "author": "Jeanine Cummins",
            "year": 2020,
            "price": 10.99,
        },
        {
            "title": "Daisy Jones & The Six",
            "author": "Taylor Jenkins Reid",
            "year": 2019,
            "price": 9.99,
        },
        {
            "title": "The Night Watchman",
            "author": "Louise Erdrich",
            "year": 2020,
            "price": 10.49,
        },
        {
            "title": "Anxious People",
            "author": "Fredrik Backman",
            "year": 2020,
            "price": 9.99,
        },
        {
            "title": "Such a Fun Age",
            "author": "Kiley Reid",
            "year": 2019,
            "price": 9.49,
        },
        {
            "title": "The Institute",
            "author": "Stephen King",
            "year": 2019,
            "price": 11.49,
        },
        {
            "title": "A Man Called Ove",
            "author": "Fredrik Backman",
            "year": 2012,
            "price": 8.99,
        },
        {
            "title": "The Light We Lost",
            "author": "Jill Santopolo",
            "year": 2017,
            "price": 8.49,
        },
        {
            "title": "The Dutch House",
            "author": "Ann Patchett",
            "year": 2019,
            "price": 9.99,
        },
        {"title": "Circe", "author": "Madeline Miller", "year": 2018, "price": 10.49},
        {
            "title": "Eleanor Oliphant Is Completely Fine",
            "author": "Gail Honeyman",
            "year": 2017,
            "price": 9.49,
        },
        {
            "title": "The Water Dancer",
            "author": "Ta-Nehisi Coates",
            "year": 2019,
            "price": 10.99,
        },
        {
            "title": "The Tattooist of Auschwitz",
            "author": "Heather Morris",
            "year": 2018,
            "price": 9.99,
        },
        {
            "title": "The Henna Artist",
            "author": "Alka Joshi",
            "year": 2020,
            "price": 8.99,
        },
    ]

    for i, b in enumerate(books):
        create_product(
            random.randint(0, 10**6),
            i + 1,
            i + 1,
            b.get("title"),
            "test",
            b.get("price"),
            random.randint(5, 50),
            b.get("year"),
            [b.get("author")],
        )


def create_fake_card():
    for i in range(100):
        create_card(i + 1)


def create_fake_category():
    book_categories = [
        "Fiction",
        "Non-Fiction",
        "Mystery/Thriller",
        "Science Fiction",
        "Fantasy",
        "Romance",
        "Historical Fiction",
        "Young Adult",
        "Horror",
    ]

    credit_types = [
        "Credit Card",
        "Mortgage",
        "Auto Loan",
        "Personal Loan",
        "Student Loan",
        "Home Equity Loan",
        "Line of Credit",
        "Payday Loan",
        "Small Business Loan",
        "Credit Builder Loan",
    ]

    for i in range(100):
        create_category(
            random.choice(book_categories), f.state(), random.choice(credit_types)
        )


create_book()
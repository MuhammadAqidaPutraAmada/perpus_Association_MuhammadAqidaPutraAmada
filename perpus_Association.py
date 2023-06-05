class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.ada = True

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.pinjam = []

    def borrow_book(self, book):
        if book.ada:
            book.ada = False
            self.pinjam.append(book)
            print(f"{self.name} berhasil meminjam buku: {book.title}")
        else:
            print(f"Maaf, buku {book.title} sedang dipinjam.")

    def return_book(self, book):
        if book in self.pinjam:
            book.ada = True
            self.pinjam.remove(book)
            print(f"{self.name} berhasil mengembalikan buku: {book.title}")
        else:
            print(f"Maaf, buku {book.title} tidak ada dalam daftar buku yang dipinjam.")

    def display_borrowed_books(self):
        print(f"Daftar Buku yang Dipinjam oleh {self.name}:")
        if len(self.pinjam) == 0:
            print("Tidak ada buku yang dipinjam.")
        else:
            for book in self.pinjam:
                print(f"Judul: {book.title}")
                print(f"Penulis: {book.author}")
                print(f"Status Ketersediaan: {'Tersedia' if book.ada else 'Dipinjam'}")
                print("")


member = LibraryMember(input("Masukkan nama anggota perpustakaan: "))

# INPUT
n = int(input("Berapa banyak buku yang ingin dipinjam? "))

for i in range(n):
    print(f"\nBuku ke-{i+1}:")
    title = input("Judul: ")
    author = input("Penulis: ")

    book = Book(title, author)
    member.borrow_book(book)

# SHOW DAFTAR BUKU YANG DIPINJAM
member.display_borrowed_books()

# INPUT PENGEMBALIAN BUKU
n = int(input("Berapa banyak buku yang ingin dikembalikan? "))

for i in range(n):
    print(f"\nBuku ke-{i+1}:")
    title = input("Judul: ")
    author = input("Penulis: ")

    book = Book(title, author)
    member.return_book(book)

# Menampilkan daftar buku yang dipinjam setelah pengembalian
member.display_borrowed_books()

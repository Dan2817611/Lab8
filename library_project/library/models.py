from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Book(models.Model):
    SECTION_CHOICES = [
        ('Технічна', 'Технічна'),
        ('Художня', 'Художня'),
        ('Економічна', 'Економічна'),
    ]
    BOOK_TYPE_CHOICES = [
        ('Посібник', 'Посібник'),
        ('Книга', 'Книга'),
        ('Періодичне видання', 'Періодичне видання'),
    ]
    inventory_number = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    year_of_publication = models.IntegerField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book_type = models.CharField(max_length=20, choices=BOOK_TYPE_CHOICES)
    copies = models.IntegerField()
    max_loan_period = models.IntegerField()

    def __str__(self):
        return str(self.inventory_number)

class Reader(models.Model):
    card_number = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    address = models.TextField()
    course = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
    group = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.card_number)

class BookIssue(models.Model):
    issue_code = models.IntegerField(primary_key=True)
    issue_date = models.DateField()
    reader_card_number = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book_inventory_number = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reader: {self.reader_card_number}, Book: {self.book_inventory_number}"

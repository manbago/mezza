from django.db import models

# Create your models here.
from mezzanine.pages.models import Page
from mezzanine.generic.fields import KeywordsField
from mezzanine.generic.fields import CommentsField
from mezzanine.generic.fields import RatingField

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.

class Author(Page):
    dob = models.DateField("Date of birth")
    comments = CommentsField()
    rating = RatingField()

class Book(models.Model):
    author = models.ForeignKey("Author")
    cover = models.ImageField(upload_to="authors")
    keywords = KeywordsField()
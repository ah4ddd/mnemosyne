#defines tables
#defines columns
#defines relationships
#defines how objects look to humans
#the schema

from django.db import models

#lives in database
class Topic(models.Model):# this class becomes the table
    # Each Topic has a text column, max 100 characters
    text = models.CharField(max_length=100)
    #timestaps the created topic
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):# just prints the object
        return self.text

class Entry(models.Model): #same deal, new tables and entity
    # Each entry belongs to ONE topic, A Topic can have MANY Entries
    # A foreign key is a column in one table that stores the ID of a row in another table
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # if topic is deleted, delete all its Entries
    text = models.TextField() # CharFiel but unlimited lenght, stored in different SQL, better for paragraphs
    date_added = models.DateTimeField(auto_now_add=True) #timestamp again

    class Meta: # configuration for Django, not logic  just cosmetics
        verbose_name_plural = 'entries'

    def __str__(self): # controls how entries show up in admin.
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text

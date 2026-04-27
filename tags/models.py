from django.db import models

# This is part of the Django ContentType framework
# It helps Django know WHICH model (Product, Collection, etc.)
from django.contrib.contenttypes.models import ContentType

# This allows us to create a "dynamic foreign key"
from django.contrib.contenttypes.fields import GenericForeignKey


# -----------------------------
# TAG MODEL (simple model)
# -----------------------------
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name





# -----------------------------
# GENERIC RELATION MODEL
# -----------------------------
class TaggedItem(models.Model):

    # Normal ForeignKey: each tag item belongs to one Tag
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # Step 1: Stores the MODEL TYPE (Product, Collection, etc.)
    # Example: "Product"
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    # Step 2: Stores the OBJECT ID inside that model
    # Example: 5 (meaning Product with id=5)
    object_id = models.PositiveIntegerField()

    # Step 3: Combines content_type + object_id
    # This gives the actual object (Product, Collection, etc.)
    content_object = GenericForeignKey()

    # Automatically stores when the tag was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tag} -> {self.content_object}"
from django.db import models

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Mouse(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()



# Add new Feeding model below Cat model
class Feeding(models.Model):
  date = models.DateField("Feeding Date")
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'L'
    default=MEALS[0][1]
  )

  # Create a cat_id FK (this creates the association)
  # and handles deleting eals when a mouse is deleted from the DB
  mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
  #  ForeignKey = one to many relationship

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ["-date"]


class Toy(models.Model):
  name = models.CharField(max_length=50),
  color = models.CharField(max_length=20)

  def __str__(self):
      return self.name
  



# AWS Photo stuff
class Photo(models.Model):
  url = models.CharField(max_length=200)
  mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)


  def __str__(self):
    return f" Photo for mouse_id: {self.mouse_id} @{self.url} "



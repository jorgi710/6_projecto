from django.db import models

# Create your models here.

class Question(models.Model):
    """Model definition for Question."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.question_text     
        
class Choice(models.Model):
    """Model definition for Choice."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        """Meta definition for Choice."""

        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'
        ordering = ["votes"]

    def __str__(self):
        """Unicode representation of Choice."""
        return self.choice_text + "-->" +str(self.votes)


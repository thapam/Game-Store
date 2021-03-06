from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_developer = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=32, default="") #MD5 Hash of email+salt
    def __str__(self):
        return "User: " + self.user.username

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #developer
    title = models.CharField(max_length=250)
    href = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=250)
    def __str__(self):
        return "Developer: " + self.user.username + ", Title: " + self.title


class PlayerGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_on = models.DateTimeField(auto_now_add=True)
    purchased_price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=3000, blank=True, null=True)
    def __str__(self):
        return "Player: " + self.user.username + ", Game: " + self.game.title


class ScoreBoard(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    def __str__(self):
        return "Game: " + self.game.title + ", User: " + self.user.username + ", Score: " + str(self.score) + " Time: " + self.timestamp.strftime('%Y-%m-%d %H:%M')


class Payment(models.Model):
    pid = models.CharField(max_length=250)
    sid = models.CharField(max_length=250, default="gamestore123")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    checksum = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    ref = models.CharField(max_length=250)
    def __str__(self):
        return "Id: " + self.pid + ", Amount: " + str(self.amount) + ", Completed: " + str(self.completed)

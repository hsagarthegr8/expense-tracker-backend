from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Wallet(models.Model):
    CATEGORY_CHOICES = (
        ('B', 'Bank Account'),
        ('C', 'Cash'),
        ('W', 'Wallets'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    balance = models.FloatField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def add_money(self, money):
        self.balance += money
        self.save()

    def deduct_money(self, money):
        self.balance -= money
        self.save()




class Transaction(models.Model):
    TYPE_CHOICES = (
        ('I', 'Income'),
        ('E', 'Expense'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    amount = models.FloatField()
    description = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} {self.amount} {self.type}'

    def save(self):
        if self.type == 'I':
            self.wallet.add_money(self.amount)
        else:
            self.wallet.deduct_money(self.amount)

        super().save()





    
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
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} {self.amount} {self.type}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            if self.type == 'I':
                self.wallet.add_money(self.amount)
            else:
                self.wallet.deduct_money(self.amount)
        super().save()

    def delete(self, using=None, keep_parents=False):
        if self.type == 'I':
            self.wallet.deduct_money(self.amount)
        else:
            self.wallet.add_money(self.amount)
        super().delete()

    def update_wallet_or_amount(self, transaction_type, amount, wallet):
        if self.wallet == wallet:
            if self.type == transaction_type:
                if self.type == 'I':
                    self.wallet.add_money(amount - self.amount)
                else:
                    self.wallet.add_money(self.amount - amount)
            else:
                if self.type == 'I':
                    self.wallet.deduct_money(self.amount + amount)
                else:
                    self.wallet.add_money(self.amount + amount)
        else:
            if self.type == 'I':
                self.wallet.deduct_money(self.amount)
            else:
                self.wallet.add_money(self.amount)

            if transaction_type == 'I':
                wallet.add_money(amount)
            else:
                wallet.deduct_money(amount)
            wallet.save()

        self.wallet.save()






    
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#import uuid

# Create your models here.
class Item(models.Model): #//Donation//
		ItemName_M = models.CharField(max_length=200, null=True)
		ItemDesc_M = models.CharField(max_length=20, null=True)
		Quantity_M= models.CharField(max_length=200, null=True)
		Unit_M = models.CharField(max_length=200, null=True)
		Price_M = models.CharField(max_length=200, null=True)
class meta:
		db_table = "Registry Table"


class ClientInformation(models.Model): #//Donator Info//
		CName_M = models.CharField(max_length=50, null=True)
		CAddress_M	= models.CharField(max_length=50, null=True)
		CContact_M = models.PositiveIntegerField(default =0, blank=True, null=True, validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(0)])
		CEmail_M = models.EmailField(max_length=254, default="", blank=True, null=True)
class meta:
   		db_table = "Client Information"


class BuyerInformation(models.Model): #//Receiver Information//
		BName_M = models.CharField(max_length=50, null=True)
		BAddress_M = models.CharField(max_length=50, null=True)
		BContact_M = models.PositiveIntegerField(default =0, blank=True, null=True, validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(0)])
		BEmail_M = models.EmailField(max_length=254, default="", blank=True, null=True)
		BCompanyName_M = models.CharField(max_length=30, null=True)
class meta:
		db_table = "Buyer information"


class RecycableMaterialsReport(models.Model): #//Received Donations//
		RMDate_M = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
		RMItemCode_id_M = models.ForeignKey(Item, default="", on_delete= models.CASCADE, blank=True, null=True)
		RMCNo_id_M = models.ForeignKey(ClientInformation, default="", on_delete= models.CASCADE, blank=True, null=True)
		RMBNo_id_M = models.ForeignKey(BuyerInformation, default="", on_delete= models.CASCADE, blank=True, null=True)
		RMPickupDate_M = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
		RMStatus_M = (
			('Received', 5),
			('Pending', 4),
			('Cancelled', 3),
			('Rescheduled', 2),
			('For Pick-up', 1),
			)
class meta:
		db_table = "Recycable Materials Monitoring"


class FeedbackReport(models.Model):
		FBR_CNo_M = models.ForeignKey(ClientInformation, default="", on_delete= models.CASCADE, blank=True, null=True)
		FBR_BNo_M = models.ForeignKey(BuyerInformation, default="", on_delete= models.CASCADE, blank=True, null=True)
		RATING_CHOICES_M =(
			('Very Satisfied', 5),
			('Satisfied', 4),
			('Neutral', 3),
			('Disssatisfied', 2),
			('Very Disssatisfied', 1),
			)
		FBR_Rating_M = models.CharField(max_length=100, choices=RATING_CHOICES_M)
		FBR_Desc_M = models.CharField(max_length=50, null=True)
		FBR_Comments_M = models.CharField(max_length=1000, null=True)
class meta:
		db_table = "FeedBack Report"


class PaymentMethod(models.Model):
		PAYMENT_MODE_M =(
			('Cash on Pick-up', 4),
			('Online Banking', 3),
			('GCash', 2),
			('Pay Maya', 1),
			)
class meta:
		db_table = "Payment Method"


class PaymentInformation(models. Model):
		PI_ItemCode_M = models.ForeignKey(Item, default="", on_delete= models.CASCADE, blank=True, null=True)
		PI_PM_id_M = models.ForeignKey(PaymentMethod, default="", on_delete= models.CASCADE, blank=True, null=True)
		PI_AcctName_M = models.CharField(max_length=50, null=True)
		PI_AcctNo_M = models.CharField(max_length=50, null=True)
class meta:
		db_table = "Payment Information"

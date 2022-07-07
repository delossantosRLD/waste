from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, ClientInformation, BuyerInformation, FeedbackReport

def MainPage(request):
	return render(request,'welcomepage.html')

def AboutPage(request):
	return render(request,'about.html')

def sellerpage(request):
	if request.method == "POST":
		ItemName_M = request.POST['ItemName_M']
		ItemDesc_M = request.POST['ItemDesc_M']
		Quantity_M = request.POST['Quantity_M']
		Unit_M = request.POST['Unit_M']
		Price_M = request.POST['Price_M']
		item = Item(ItemName_M = ItemName_M,
		ItemDesc_M = ItemDesc_M,
		Quantity_M = Quantity_M,
		Unit_M = Unit_M,
		Price_M = Price_M,
		)
		
		item.save()

	else:
		return render(request,'sellerpage.html')
	itemss =   Item.objects.all()
	return render(request,'sellerpage.html',{'itemss':itemss})

def displayrec(request):
	disrec=Item.objects.all()
	context ={'disrec':disrec}
	return render(request,'recycablelist.html', context)

def disrec(request):
	disrec=Item.objects.all()
	context ={'disrec':disrec}
	return render(request,'recstatus.html', context)

def Deleterec(request,recid):
	recitem= Item.objects.get(id = recid)
	recitem.delete()
	return render(request,'welcomepage.html')

def Editrec(request,recid):
	recitem = Item.objects.get(id = recid)
	itemss = Item.objects.all()
	return render(request,'sellerpage.html',{'recitem':recitem,
		'itemss':itemss,
		})

def Updaterec(request,recid):
	itemss = Item.objects.get(id = recid)
	itemss.ItemName_M = request.POST['ItemName_M']
	itemss.ItemDesc_M = request.POST['ItemDesc_M']
	itemss.Quantity_M = request.POST['Quantity_M']
	itemss.Unit_M = request.POST['Unit_M']
	itemss.Price_M = request.POST['Price_M']
	itemss.save()
	return redirect('MainPage')

def buyerpage(request):
	if request.method == "POST":
		BName_M = request.POST['BName_M']
		BAddress_M = request.POST['BAddress_M']
		BContact_M = request.POST['BContact_M']
		BEmail_M = request.POST['BEmail_M']
		BCompanyName_M = request.POST['BCompanyName_M']
		blist = BuyerInformation(BName_M = BName_M,
		BAddress_M = BAddress_M,
		BContact_M = BContact_M,
		BEmail_M = BEmail_M,
		BCompanyName_M = BCompanyName_M,
		)
		blist.save()

	else:
		return render(request,'buyerpage.html')
	blists = BuyerInformation.objects.all()
	return render(request,'buyerpage.html',{'blists':blists})

def displaybuyer(request):
	disbuy=BuyerInformation.objects.all()
	context ={'disbuy':disbuy}
	return render(request,'buyerlist.html', context)

def Deletebuyer(request,buyid):
	buyerInformation= BuyerInformation.objects.get(id = buyid)
	buyerInformation.delete()
	return render(request,'welcomepage.html')

def Editbuyer(request,buyid):
	buyerInformation = BuyerInformation.objects.get(id = buyid)
	blists = BuyerInformation.objects.all()
	return render(request,'buyerpage.html',{'buyerInformation':buyerInformation,
		'blists':blists,
		})

def Updatebuyer(request,buyid):
	blists = BuyerInformation.objects.get(id = buyid)
	blists.BName_M = request.POST['BName_M']
	blists.BAddress_M = request.POST['BAddress_M']
	blists.BContact_M = request.POST['BContact_M']
	blists.BEmail_M = request.POST['BEmail_M']
	blists.BCompanyName_M = request.POST['BCompanyName_M']
	blists.save()
	return redirect('MainPage')
	

def sellerinfo(request):
	if request.method == "POST":
		CName_M = request.POST['CName_M']
		CAddress_M = request.POST['CAddress_M']
		CContact_M = request.POST['CContact_M']
		CEmail_M = request.POST['CEmail_M']
		slist = ClientInformation(CName_M = CName_M,
		CAddress_M = CAddress_M,
		CContact_M = CContact_M,
		CEmail_M = CEmail_M,
		)
		slist.save()

	else:
		return render(request,'sellerinfo.html')
	slists = ClientInformation.objects.all()
	return render(request,'sellerinfo.html',{'slists':slists})

def Deleteseller(request,sellid):
	clientInformation= ClientInformation.objects.get(id = sellid)
	clientInformation.delete()
	return render(request,'welcomepage.html')

def Editseller(request,sellid):
	clientInformation = ClientInformation.objects.get(id = sellid)
	slists = ClientInformation.objects.all()
	return render(request,'sellerinfo.html',{'clientInformation':clientInformation,
		'slists':slists,
		})

def Updateseller(request,sellid):
	slists = ClientInformation.objects.get(id = sellid)
	slists.CName_M = request.POST['CName_M']
	slists.CAddress_M = request.POST['CAddress_M']
	slists.CContact_M = request.POST['CContact_M']
	slists.CEmail_M = request.POST['CEmail_M']
	slists.save()
	return redirect('MainPage')

def displayseller(request):
	dissell=ClientInformation.objects.all()
	context ={'dissell':dissell}
	return render(request,'sellerlist.html', context)

def createdfeedback(request):
	ms= ['Very Satisfied', 'Satisfied', 'Neutral', 'Disssatisfied', 'Very Disssatisfied']
	if request.method == "POST":
		FBR_Rating_M = request.POST.getlist('FBR_Rating_M')
		print(FBR_Rating_M)
		if FBR_Rating_M==['Very Satisfied']:
			print('5')
		if FBR_Rating_M==['Satisfied']:
			print('4')
		if FBR_Rating_M==['Neutral']:
			print('3')
		if FBR_Rating_M==['Disssatisfied']:
			print('2')
		if FBR_Rating_M==['Very Disssatisfied']:
			print('1')
		FBR_Desc_M = request.POST['FBR_Desc_M']
		FBR_Comments_M = request.POST['FBR_Comments_M']
		fbck = FeedbackReport(FBR_Rating_M = FBR_Rating_M,
		FBR_Desc_M = FBR_Desc_M,
		FBR_Comments_M = FBR_Comments_M,
		)
		fbck.save()
	else:
		return render(request,'feedback.html')
	fbcks = FeedbackReport.objects.all()
	return render(request,'feedback.html',{'fbcks':fbcks})

def displayfeedback(request):
	disfb=FeedbackReport.objects.all()
	context ={'disfb':disfb}
	return render(request,'feedback.html', context)

def Deletefeedback(request,fbid):
	fbcks= FeedbackReport.objects.get(id = fbid)
	fbcks.delete()
	return render(request,'feedback.html')




from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.MainPage, name='MainPage'),
	path('AboutPage',views.AboutPage, name='AboutPage'),

	path('sellerpage',views.sellerpage, name='sellerpage'),
	path('displayrec',views.displayrec, name='displayrec'),
	path('disrec',views.disrec, name='disrec'),
	path('deleterec/<int:recid>',views.Deleterec, name = "deleterec"),
	path('editrec/<int:recid>',views.Editrec, name = "editrec"),
	path('updaterec/<int:recid>',views.Updaterec, name = "updaterec"),
	
	path('buyerpage',views.buyerpage, name='buyerpage'),
	path('displaybuyer',views.displaybuyer, name='displaybuyer'),
	path('deletebuyer/<int:buyid>',views.Deletebuyer, name = "deletebuyer"),
	path('editbuyer/<int:buyid>',views.Editbuyer, name = "editbuyer"),
	path('updatebuyer/<int:buyid>',views.Updatebuyer, name = "updatebuyer"),

	path('sellerinfo',views.sellerinfo, name='sellerinfo'),
	path('displayseller',views.displayseller, name='displayseller'),
	path('deleteseller/<int:sellid>',views.Deleteseller, name = "deleteseller"),
	path('editseller/<int:sellid>',views.Editseller, name = "editseller"),
	path('updateseller/<int:sellid>',views.Updateseller, name = "updateseller"),

	path('createdfeedback',views.createdfeedback, name='createdfeedback'),
	path('displayfeedback',views.displayfeedback, name='displayfeedback'),
	path('deletefeedback/<int:fbid>',views.Deletefeedback, name = "deletefeedback"),

	# path('itemlist',views.itemlist, name='itemlist'),
	# path('displayitems', views.displayitems, name='displayitems'),
	]
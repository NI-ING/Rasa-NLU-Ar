import arabic_reshaper
from bidi.algorithm import get_display
import re

regex = re.compile(r'[\n\r\t]')
lookups_dir ="data/lookups"



def enteties_detection(txt):
	enteties_dict ={
	"hotel_name" : "NONE",
	"etoile_nbr" : "NONE",
	"gouv_name" : "NONE",
	"nbr_nights" : "NONE",
	"nbr_room" : "NONE",
	"nb_adult" : "NONE",
	"nb_childs" : "NONE"
	}
		
	reshaped_text = arabic_reshaper.reshape(txt)    # correct its shape
	req = get_display(reshaped_text)           # correct its direction
	txt_list=[]
	txt_list=req.split(" ")
	print ("\nreq = "+req+"\n")
	#print(txt_list)
	
	#------------hotel ------------------------------

	f = open(lookups_dir+'/hotels.txt', encoding='utf-8')
	hotels = f.readlines()
	
	for i in range(len(hotels)) :
		hotels[i]=regex.sub("", hotels[i])
	
	for row in hotels:
		reshaped_text = arabic_reshaper.reshape(row)    # correct its shape
		new_row = get_display(reshaped_text)           # correct its direction	
		if new_row in req:
			start_index=req.find(new_row)
			end_index=start_index + len(new_row)
			TAG=" $hotel_name$ "
			req=req.replace(new_row,TAG)
			enteties_dict["hotel_name"]=new_row
			

	f.close()
	
	#------------ nbr etoile-----------------------------
	
	f = open(lookups_dir+'/etoile.txt', encoding='utf-8')
	etoiles = f.readlines()
	
	for i in range(len(etoiles)) :
		etoiles[i]=regex.sub("", etoiles[i])
	
	for row in etoiles:
		reshaped_text = arabic_reshaper.reshape(row)    # correct its shape
		new_row = get_display(reshaped_text)           # correct its direction	
		if new_row in req:
			start_index=req.find(new_row)
			end_index=start_index + len(new_row)
			TAG=" $etoile_nbr$ "
			req=req.replace(new_row,TAG)
			enteties_dict["etoile_nbr"]=new_row
			

	f.close()
				
	
	#------------ gouv name ------------------------------

	f = open(lookups_dir+'/gouv.txt', encoding='utf-8')
	gouvs = f.readlines()

	for i in range(len(gouvs)) :
		gouvs[i]=regex.sub("", gouvs[i])
	
	for row in gouvs:
		reshaped_text = arabic_reshaper.reshape(row)    # correct its shape
		new_row = get_display(reshaped_text)           # correct its direction	
		if new_row in req:
			start_index=req.find(new_row)
			end_index=start_index + len(new_row)+1
			TAG=" $gouv_name$ "
			req=req.replace(new_row,TAG)
			enteties_dict["gouv_name"]=new_row

	f.close()


	#------------ nights nbr ------------------------------

	f = open(lookups_dir+'/nbrNight.txt', encoding='utf-8')
	nbnights = f.readlines()
	
	for i in range(len(nbnights)) :
		nbnights[i]=regex.sub("", nbnights[i])
	
	for row in nbnights:
		reshaped_text = arabic_reshaper.reshape(row)    # correct its shape
		new_row = get_display(reshaped_text)           # correct its direction	
		if new_row in req:
			start_index=req.find(new_row)
			end_index=start_index + len(new_row)+1
			TAG=" $nbr_nights$ "
			req=req.replace(new_row,TAG)
			enteties_dict["nbr_nights"]=new_row

	f.close()

	#------------ room nbr ------------------------------

	f = open(lookups_dir+'/rooms.txt', encoding='utf-8')
	rooms = f.readlines()
	
	for i in range(len(rooms)) :
		rooms[i]=regex.sub("", rooms[i])
	
	for row in rooms:
		reshaped_text = arabic_reshaper.reshape(row)    # correct its shape
		new_row = get_display(reshaped_text)           # correct its direction	
		if new_row in req:
			start_index=req.find(new_row)
			end_index=start_index + len(new_row)+1
			TAG=" $nbr_room$ "
			req=req.replace(new_row,TAG)
			enteties_dict["nbr_room"]=new_row

	f.close()

	#------------ nbr adults ------------------------------

	f = open(lookups_dir+'/adults.txt', encoding='utf-8')
	adults = f.readlines()
	
	for i in range(len(adults)) :
		adults[i]=regex.sub("", adults[i])
	
	for row in adults:
		reshaped_text = arabic_reshaper.reshape(row)    # correct its shape
		new_row = get_display(reshaped_text)           # correct its direction	
		if new_row in req:
			start_index=req.find(new_row)
			end_index=start_index + len(new_row)+1
			TAG=" $nb_adult$ "
			req=req.replace(new_row,TAG)
			enteties_dict["nb_adult"]=new_row

	f.close()
	

	#------------ nbr childs ------------------------------

	f = open(lookups_dir+'/childs.txt', encoding='utf-8')
	childs = f.readlines()
	
	for i in range(len(childs)) :
		childs[i]=regex.sub("", childs[i])
	
	for row in childs:
		reshaped_text = arabic_reshaper.reshape(row)    # correct its shape
		new_row = get_display(reshaped_text)           # correct its direction	
		if new_row in req:
			start_index=req.find(new_row)
			end_index=start_index + len(new_row)+1
			TAG=" $nb_childs$ "
			req=req.replace(new_row,TAG)
			enteties_dict["nb_childs"]=new_row

	f.close()
	#print("\nfinal requet : \n"+req)

	return enteties_dict



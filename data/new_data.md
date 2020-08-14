## intent:salutation
- السلام
- تحية
- اهلا
- سلام
- مرحبا
- اهلا بك
## intent:au_revoir
- على خير
- الى القاء
- الوداع
- وداعاً
- تصبح على خير
- امسيك على خير
- في امان الله
##intent:reservation

- اريد ان احجز  فندق 
- هل هناك غرفة للحجز 
- هل يمكنني ان احجز فندق 
- هل هناك غرف للحجز في فندق
- فندق من فضلك
- غرفة في فندق 
##intent:reservation/nbr_person

- اريد ان احجز فندق ل[ثلاث اشخاص](nbr_person) 
- أريد أن احجز فندق ل[شخصين](nbr_person) 
- هل هناك غرفة للحجز ل[شخص واحد] nbr_person)
- هل هناك غرفة للحجز ل[شخصان](nbr_person) 
- هل يمكنني أن احجز فندق ل[ثلاث اشخاص](nbr_person)
- هل يمكنني أن احجز فندق ل[شخص واحد](nbr_person)
- هل هناك حجز في فندق ل[شخصان](nbr_person)
- هل هناك حجز في فندق ل[اربع اشخاص](nbr_person)
- هل هناك غرف للحجز في فندق   $hotel_name$ لمدة $nbr_night$ ؟
- فندق ل[شخصين](nbr_person) من فضلك
- فندق ل[ثلاث اشخاص](nbr_person) من فضلك
- غرفة ل[شخصين](nbr_person) من فضلك
- غرفة ل[ثلاث اشخاص](nbr_person) من فضلك

##intent:reservation/nb_adlult+nb_enfant
- حجز ل[شخصين](nb_adult) و [طفلان](nb_enfant)
- حجز ل[ثلاث اشخاص](nb_adult) و [ثلاث اطفال](nb_enfant)
- حجز ل[أربعة أطفال](nb_enfant) و [شخصان](nb_adult)
- [ثلاث اشخاص](nb_adult) و [ثلاث اطفال](nb_enfant)
- [شخصين](nb_adult) و [طفلين](nb_enfant)
- [ثلاث اشخاص](nb_adult) و [ثلاث اطفال](nb_enfant)
- [ثلاثة اشخاص](nb_adult) و [ثلاثة اطفال](nb_enfant)
- [شخصان](nb_adult) و [طفل واحد](nb_enfant)
- [ثلاث اشخاص](nb_adult) و [طفلان](nb_enfant)
- [شخصين](nb_adult) و [ثلاث اطفال](nb_enfant)
- [شخصين](nb_adult) و [ثلاثة اطفال](nb_enfant)
- [شخصان](nb_adult) و [ثلاث اطفال](nb_enfant)
- [شخصان](nb_adult) و [ثلاثة اطفال](nb_enfant)
- [طفل واحد](nb_adult) و [شخصان](nb_enfant)

##intent:hotel_search
- أريد أن أسأل على فندق
- هل يمكنني أن اتحصل على بعض المعلومات على فندق 

##intent:hotel_search/etoile
- أريد فندق ذو [ثلاث نجوم](nbr_etoile)
- أريد فندق ذو [اربع نجوم](nbr_etoile)
- فندق ذو [اربع نجوم](nbr_etoile) من فضلك 
- هل هناك فندق ل[اربعة نجوم](nbr_etoile)
- هل هناك فندق ل[نجمتان](nbr_etoile)


##intent:reservation/nb_enfant_inf_2ans
- صفر
- واحد
- واحدة
- اثنان
- اثنين
- ثلاث
- ثلاثة
- اربع
- اربعة
- خمس
- خمسة


## lookup:nbr_person  
lookups/new_lookups/persons.txt

## lookup:nb_enfant  
lookups/new_lookups/childs.txt

## lookup:nb_adult 
lookups/new_lookups/adults.txt

## regex:greet
- hey[^\s]*
## regex:zipcode
- [0-9]{5}

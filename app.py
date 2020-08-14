import intent_detection
import enteties_detection
import arabic_reshaper
from bidi.algorithm import get_display

model_dir ="models/default/model_20200704-161827"

#text= "أريد أن احجز غرفتان لشخصين "

def rasa_nlu(text):
	
	rasa_values ={
	"intent_name" : "NONE",
	"enteties_names" : "NONE"
	}
	enteties_values = enteties_detection.enteties_detection(text)
	jsonIntent = intent_detection.intent_detection(model_dir,text)

	#print("\n\n enteties :  ")
	#print(enteties_values)

	x = jsonIntent["intent"]
	int_value = x["name"]
	#print("\n\n intent :  "+ int_value)
	

	rasa_values["intent_name"] = int_value
	rasa_values["enteties_names"] = enteties_values
	return(rasa_values)


x=rasa_nlu("أريد أن احجز غرفة لشخصين في فندق الياسمين")
print(x)

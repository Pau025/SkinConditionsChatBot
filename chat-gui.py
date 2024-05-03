
from tkinter import*
#Agente
from utils import *
from logic import * 

#Knowledge Base 

clauses = []

#René 
clauses.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PielInflamada) & Sintoma(x, PielSensible) & Sintoma(x, Ardor) & Sintoma(x, Brotes)) ==> Enfermo(x, RosaceaT1)"))
clauses.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PielSensible) & Sintoma(x, PielGraso) & Sintoma(x, Brotes)) ==> Enfermo(x, RosaceaT2)"))
clauses.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, PorosDilatados) & Sintoma(x, PielGraso) & Sintoma(x, Bultos)) ==> Enfermo(x, RosaceaT3)"))
clauses.append(expr("(Sintoma(x, Enrojecimiento) & Sintoma(x, OjosLacrimosos) & Sintoma(x, OjosIrritados) & Sintoma(x, OjosEnrojecidos) & Sintoma(x, VisionBorrosa)) ==> Enfermo(x, RosaceaT4)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Recomendar(x, Demodex)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaMetronidazol)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaMetronidazol)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaMetronidazol)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaMetronidazol)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaAcidoZelaico)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaAcidoZelaico)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaAcidoZelaico)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaAcidoZelaico)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, CremaRetinoides)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, CremaRetinoides)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, CremaRetinoides)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, CremaRetinoides)"))
clauses.append(expr("Enfermo(x, RosaceaT1) ==> Tratamiento(x, OralDoxiciclina)"))
clauses.append(expr("Enfermo(x, RosaceaT2) ==> Tratamiento(x, OralDoxiciclina)"))
clauses.append(expr("Enfermo(x, RosaceaT3) ==> Tratamiento(x, OralDoxiciclina)"))
clauses.append(expr("Enfermo(x, RosaceaT4) ==> Tratamiento(x, OralDoxiciclina)"))
clauses.append(expr("(Sintoma(x, Picor) & Sintoma(x, Surcos) & Sintoma(x, PicorConocidos)) ==> Enfermo(x, Sarna)"))
clauses.append(expr("Enfermo(x, Sarna) ==> Recomendar(x, Biopsia)"))
clauses.append(expr("Enfermo(x, Sarna) ==> Tratamiento(x, Antihistaminico)"))
clauses.append(expr("Enfermo(x, Sarna) ==> Tratamiento(x, Permetrina)"))
clauses.append(expr("Sintoma(x, Telarana) ==> Enfermo(x, Telangeictasias)"))
clauses.append(expr("Enfermo(x, Telangeictasias) ==> Recomendar(x, NoSol)"))
clauses.append(expr("Enfermo(x, Telangeictasias) ==> Tratamiento(x, Escleroterapia)"))
clauses.append(expr("(Sintoma(x, RonchasRojas) & Sintoma(x, Erupcion) & Sintoma(x, FiebreAlta)) ==> Enfermo(x, Taxicodermia)"))
clauses.append(expr("Enfermo(x, Taxicodermia) ==> Tratamiento(x, NoMedicamentos)"))
clauses.append(expr("(Sintoma(x, Picor) & Sintoma(x, Hinchazon) & Sintoma(x, Enrojecimiento) & Sintoma(x, RonchaRojas)) ==> Enfermo(x, Urticaria)"))
clauses.append(expr("Enfermo(x, Urticaria) ==> Tratamiento(x, Corticoides)"))
clauses.append(expr("Enfermo(x, Urticaria) ==> Tratamiento(x, Antihistaminico)"))
clauses.append(expr("Sintoma(x, Fiebre) ==> Tratamiento(x, Paracetamol)"))
clauses.append(expr("Sintoma(x, FiebreAlta) ==> Tratamiento(x, Paracetamol)"))

#Maria Paula
#clauses.append(expr(""))
clauses.append(expr("Sintoma(x, PuntosBlancos) ==> Enfermo(x, Acne)"))
clauses.append(expr("(Sintoma(x, PuntosBlancos) & Sintoma(x, PuntosNegros) & Sintoma(x, Papulas)) ==> Enfermo(x, Acne)"))
clauses.append(expr("Sintoma(x, Papulas) ==> Enfermo(x, Acne)"))
clauses.append(expr("(Sintoma(x, PuntosBlancos) & Sintoma(x, Papulas) & Sintoma(x, Seborrea)) ==> Enfermo(x, Acne)"))
clauses.append(expr("(Sintoma(x, PuntosBlancos) & Sintoma(x, PuntosNegros) & Sintoma(x, Papulas) & Sintoma(x, Seborrea)) ==> Enfermo(x, Acne)"))
clauses.append(expr("Enfermo(x, Acne) ==> Tratamiento(Clindamicina)"))
clauses.append(expr("Enfermo(x, Acne) ==> Tratamiento(x, GelPeroxidoBenzoilo)"))
clauses.append(expr("Enfermo(x, Acne) ==> Tratamiento(x, Tretinoina)"))
clauses.append(expr("(Sintoma(x, Vesiculas) & Sintoma(x, DolorBoca) & Sintoma(x, Fiebre)) ==> Enfermo(x, Herpes)"))
clauses.append(expr("(Sintoma(x, Vesiculas) & Sintoma(x, Fiebre)) ==> Enfermo(x, Herpes)"))
clauses.append(expr("(Sintoma(x, Vesiculas) & Sintoma(x, DolorBoca)) ==> Enfermo(x, Herpes)"))
clauses.append(expr("Sintoma(x, Vesiculas) ==> Enfermo(x, Herpes)"))



# Gabriela Lujan

# Tratamientos
clauses.append(expr("Enfermo(x, Melasma) ==> Tratamiento(x, ProtectorSolar)"))
clauses.append(expr("Enfermo(x, Melasma) ==> Tratamiento(x, CremasTopicas)"))
clauses.append(expr("Enfermo(x, Melasma) ==> Tratamiento(x, ExfoliacionesQuimicas)"))
clauses.append(expr("Enfermo(x, Melasma) ==> Tratamiento(x, Laser)"))
clauses.append(expr("Enfermo(x, Melanoma) ==> Tratamiento(x, ExtirpacionQuirurjica)"))
clauses.append(expr("Enfermo(x, PitiriasisVersicolor) ==> Tratamiento(x, CremasAntimicoticas)"))
clauses.append(expr("Enfermo(x, PitiriasisVersicolor) ==> Tratamiento(x, ChampusAntimicoticas)"))
clauses.append(expr("Enfermo(x, PitiriasisVersicolor) ==> Tratamiento(x, PastillasAntimicoticas)"))
clauses.append(expr("Enfermo(x, Psoriasis) ==> Tratamiento(x, CremasTopicas)"))
clauses.append(expr("Enfermo(x, Psoriasis) ==> Tratamiento(x, Fototrapia)"))
clauses.append(expr("Enfermo(x, Psoriasis) ==> Tratamiento(x, MedicamentosOrales)"))
clauses.append(expr("Enfermo(x, Psoriasis) ==> Tratamiento(x, MedicamentosInyectables)"))

# Recomendaciones
clauses.append(expr("Enfermo(x, Melasma) ==> Recomendacion(x, MinimiceSol)"))
clauses.append(expr("Enfermo(x, Melasma) ==> Recomendacion(x, ControlEstres)"))
clauses.append(expr("Enfermo(x, Melasma) ==> Recomendacion(x, ProductosSinFragancias)"))
clauses.append(expr("Enfermo(x, Melasma) ==> Recomendacion(x, Dermatologo)"))
clauses.append(expr("Enfermo(x, Melasma) ==> Recomendacion(x, DietaEquilibrada)"))
clauses.append(expr("Enfermo(x, Melanoma) ==> Recomendacion(x, DietaEquilibrada)"))
clauses.append(expr("Enfermo(x, Melanoma) ==> Recomendacion(x, MinimiceSol)"))
clauses.append(expr("Enfermo(x, Melanoma) ==> Recomendacion(x, ControlEstres)"))
clauses.append(expr("Enfermo(x, Melanoma) ==> Recomendacion(x, Dermatologo)"))
clauses.append(expr("Enfermo(x, Melanoma) ==> Recomendacion(x, ExaminePiel)"))
clauses.append(expr("Enfermo(x, Melanoma) ==> Recomendacion(x, NoFumar)"))
clauses.append(expr("Enfermo(x, Melanoma) ==> Recomendacion(x, Segumiento)"))
clauses.append(expr("Enfermo(x, PitiriasisVersicolor) ==> Recomendacion(x, DietaEquilibrada)"))
clauses.append(expr("Enfermo(x, PitiriasisVersicolor) ==> Recomendacion(x, MinimiceSol)"))
clauses.append(expr("Enfermo(x, PitiriasisVersicolor) ==> Recomendacion(x, MinimiceCalor)"))
clauses.append(expr("Enfermo(x, Psoriasis) ==> Recomendacion(x, DietaEquilibrada)"))
clauses.append(expr("Enfermo(x, Psoriasis) ==> Recomendacion(x, ControlEstres)"))
clauses.append(expr("Enfermo(x, Psoriasis) ==> Recomendacion(x, NoFumar)"))

# Sintomas
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheMejilla) & Sintoma(x, NoMolestia) ==> Enfermo(x, Melasma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheFrente) & Sintoma(x, NoMolestia) ==> Enfermo(x, Melasma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParchePuenteNariz) & Sintoma(x, NoMolestia) ==> Enfermo(x, Melasma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheLabioSuperior) & Sintoma(x, NoMolestia) ==> Enfermo(x, Melasma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheMenton) & Sintoma(x, NoMolestia) ==> Enfermo(x, Melasma)"))
clauses.append(expr("Sintoma(x, CambioLunar) & Sintoma(x, Asimetria) & Sintoma(x, Borde) & Sintoma(x, Color) & Sintoma(x, Diametro) & Sintoma(x, Evolucion) ==> Enfermo(x, Melanoma)"))
clauses.append(expr("Sintoma(x, SurgeLunar) & Sintoma(x, Asimetria) & Sintoma(x, Borde) & Sintoma(x, Color) & Sintoma(x, Diametro) & Sintoma(x, Evolucion) ==> Enfermo(x, Melanoma)"))
clauses.append(expr("Sintoma(x, CambioLunar) & Sintoma(x, Asimetria) & Sintoma(x, Borde) & Sintoma(x, Color) & Sintoma(x, Diametro) & Sintoma(x, Evolucion) & Sintoma(x, Molestia) ==> Enfermo(x, Melanoma)"))
clauses.append(expr("Sintoma(x, SurgeLunar) & Sintoma(x, Asimetria) & Sintoma(x, Borde) & Sintoma(x, Color) & Sintoma(x, Diametro) & Sintoma(x, Evolucion) & Sintoma(x, Molestia) ==> Enfermo(x, Melanoma)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParchePecho) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheEspalda) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheHombros) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheSuperiorBrazos) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheCabeza) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheMarron) & Sintoma(x, ParcheAbdomen) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParchePecho) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheEspalda) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheHombros) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheSuperiorBrazos) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheCabeza) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRosa) & Sintoma(x, ParcheAbdomen) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParchePecho) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheEspalda) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheHombros) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheSuperiorBrazos) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheCabeza) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheAbdomen) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParchePecho) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheEspalda) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheHombros) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheSuperiorBrazos) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheCabeza) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheBlanco) & Sintoma(x, ParcheAbdomen) & Sintoma(x, NoMolestia) ==> Enfermo(x, PitiriasisVersicolor)"))
clauses.append(expr("Sintoma(x, ParcheRojo) & Sintoma(x, ParcheInflamado) & Sintoma(x, Molestia) & Sintoma(x, ParcheEscamoso) ==> Enfermo(x, Psoriasis)"))

doctor_kb = FolKB(clauses)

conversation_state = 'start'
name = ''

def save_to_kb(name, symptom):
    doctor_kb.tell(expr(f"Sintoma({name}, {symptom})\n"))

def process_input(input):
    global conversation_state
    global name

    response = "Favor de contestar s o n. Presione s para continuar."

    if conversation_state == 'start':
        #Asks for user's name
        response = "Hola! Estoy aquí para ayudarte con tus problemas de salud. Para empezar, ¿cuál es tu nombre?"
        conversation_state = 'get_name'
    elif conversation_state == 'get_name':
        #Saves user's name
        name = input
        response  = f"Un gusto, {name}. Te haremos una serie de preguntas, diagnosticaremos y trataremos tu problema. Para empezar, ¿presentas enrojecimiento en la piel?"
        conversation_state = 'get_enrojecimiento'
    elif conversation_state == 'get_enrojecimiento':
        if input.lower() == 's':
            save_to_kb(name, "Enrojecimiento")
            response = "¿Presenta fiebre?"
            conversation_state = "get_Fiebre"
        else: 
            response = "¿Presenta ojos irritados?"
            conversation_state = "get_OjosIrritados"
    elif conversation_state == 'get_OjosIrritados':
        if input.lower() == 's':
            save_to_kb(name, "OjosIrritados")
            response = "¿Presenta ojos lacrimosos?"
            conversation_state = "get_OjosLacrimosos"
        else: 
            response = "¿Presenta ojos lacrimosos?"
            conversation_state = "get_OjosLacrimosos"
    
    elif conversation_state == 'get_OjosIrritados':
        if input.lower() == 's':
            save_to_kb(name, "OjosIrritados")
            response = "¿Presenta ojos lacrimosos?"
            conversation_state = "get_OjosLacrimosos"
        else: 
            response = "¿Presenta ojos lacrimosos?"
            conversation_state = "get_OjosLacrimosos"
    elif conversation_state == 'get_OjosLacrimosos':
        if input.lower() == 's':
            save_to_kb(name, "OjosLacrimosos")
            response = "¿Presenta ojos enrojecidos?"
            conversation_state = "get_OjosEnrojecidos"
        else: 
            response = "¿Presenta ojos enrojecidos?"
            conversation_state = "get_OjosEnrojecidos"
    elif conversation_state == 'get_OjosEnrojecidos':
        if input.lower() == 's':
            save_to_kb(name, "OjosLacrimosos")
            response = "¿Presenta visión borrosa?"
            conversation_state = "get_VisionBorrosa"
        else: 
            response = "¿Presenta visión borrosa?"
            conversation_state = "get_VisionBorrosa"
    elif conversation_state == 'get_VisionBorrosa':
        if input.lower() == 's':
            save_to_kb(name, "VisionBorrosa")
            response = "¿Presenta piel inflamada?"
            conversation_state = "get_PielInflamada"
        else: 
            response = "¿Presenta piel inflamada?"
            conversation_state = "get_PielInflamada"
    elif conversation_state == 'get_PielInflamada':
        if input.lower() == 's':
            save_to_kb(name, "PielInflamada")
            response = "¿Presenta piel sensible?"
            conversation_state = "get_PielSensible"
        else: 
            response = "¿Presenta piel sensible?"
            conversation_state = "get_PielSensible"
    elif conversation_state == 'get_PielSensible':
        if input.lower() == 's':
            save_to_kb(name, "PielSensible")
            response = "¿Presenta piel graso?"
            conversation_state = "get_PielGraso"
        else: 
            response = "¿Presenta piel graso?"
            conversation_state = "get_PielGraso"
    elif conversation_state == 'get_PielGraso':
        if input.lower() == 's':
            save_to_kb(name, "PielGraso")
            response = "¿Presenta brotes en la piel?"
            conversation_state = "get_Brotes"
        else: 
            response = "¿Presenta brotes en la piel?"
            conversation_state = "get_Brotes"
    elif conversation_state == 'get_PielGraso':
        if input.lower() == 's':
            save_to_kb(name, "PielGraso")
            response = "¿Presenta brotes en la piel?"
            conversation_state = "get_Brotes"
        else: 
            response = "¿Presenta brotes en la piel?"
            conversation_state = "get_Brotes"
    elif conversation_state == 'get_Brotes':
        if input.lower() == 's':
            save_to_kb(name, "Brotes")
            response = "¿Presenta ardor en la piel?"
            conversation_state = "get_Ardor"
        else: 
            response = "¿Presenta ardor en la piel?"
            conversation_state = "get_Ardor"
    elif conversation_state == 'get_Ardor':
        if input.lower() == 's':
            save_to_kb(name, "Ardor")
            response = "¿Presenta poros dilatados?"
            conversation_state = "get_PorosDilatados"
        else: 
            response = "¿Presenta poros dilatados?"
            conversation_state = "get_PorosDilatados"
    elif conversation_state == 'get_PorosDilatados':
        if input.lower() == 's':
            save_to_kb(name, "PorosDilatados")
            response = "¿Presenta bultos?"
            conversation_state = "get_Bultos"
        else: 
            response = "¿Presenta bultos?"
            conversation_state = "get_Bultos"
    elif conversation_state == 'get_Bultos':
        if input.lower() == 's':
            save_to_kb(name, "Bultos")
            response = "¿Presenta fiebre?"
            conversation_state = "get_Fiebre"
        else: 
            response = "¿Presenta fiebre?"
            conversation_state = "get_Fiebre"

    elif conversation_state == 'get_Fiebre':
        if input.lower() == 's':
            save_to_kb(name, "Fiebre")
            response = "¿Presentan sus conocidos fiebre alta?"
            conversation_state = "get_FiebreAlta"
        else: 
            response = "¿Presenta picor?"
            conversation_state = "get_Picor"
    elif conversation_state == 'get_FiebreAlta':
        if input.lower() == 's':
            save_to_kb(name, "FiebreAlta")
            response = "¿Presenta picor?"
            conversation_state = "get_Picor"
        else: 
            response = "¿Presenta picor?"
            conversation_state = "get_Picor"
    
    elif conversation_state == 'get_Picor':
        if input.lower() == 's':
            save_to_kb(name, "Picor")
            response = "¿Presentan sus conocidos Picor?"
            conversation_state = "get_PicorConocidos"
        else: 
            response = "¿Presenta hinchazon?"
            conversation_state = "get_Hinchazon"
    elif conversation_state == 'get_PicorConocidos':
        if input.lower() == 's':
            save_to_kb(name, "PicorConocidos")
            response = "¿Tienes surcos en la piel?"
            conversation_state = "get_Surcos"
        else: 
            response = "¿Tienes surcos en la piel?"
            conversation_state = "get_Surcos"
    
    elif conversation_state == 'get_Surcos':
        if input.lower() == 's':
            save_to_kb(name, "Surcos")
            response = "¿Presenta hinchazon?"
            conversation_state = "get_Hinchazon"
        else: 
            response = "¿Presenta hinchazon?"
            conversation_state = "get_Hinchazon"

    elif conversation_state == 'get_Hinchazon':
        if input.lower() == 's':
            save_to_kb(name, "Hinchazon")
            response = "¿Presenta telarañas en la piel?"
            conversation_state = "get_Telarana"
        else: 
            response = "¿Presenta telarañas en la piel?"
            conversation_state = "get_Telarana"
    
    elif conversation_state == 'get_Hinchazon':
        if input.lower() == 's':
            save_to_kb(name, "Hinchazon")
            response = "¿Presenta telarañas en la piel?"
            conversation_state = "get_Telarana"
        else: 
            response = "¿Presenta telarañas en la piel?"
            conversation_state = "get_Telarana"
        
    elif conversation_state == 'get_Telarana':
        if input.lower() == 's':
            save_to_kb(name, "Telarana")
            response = "¿Presenta Ronchas Rojas en la piel?"
            conversation_state = "get_RonchasRojas"
        else: 
            response = "¿Presenta Ronchas Rojas en la piel?"
            conversation_state = "get_RonchasRojas"

    elif conversation_state == 'get_RonchasRojas':
        if input.lower() == 's':
            save_to_kb(name, "RonchasRojas")
            response = "¿Presenta puntos blancos en la cara?"
            conversation_state = "get_PuntosBlancos"
        else: 
            response = "¿Presenta puntos blancos en la cara?"
            conversation_state = "get_PuntosBlancos"
    
    elif conversation_state == 'get_PuntosBlancos':
        if input.lower() == 's':
            save_to_kb(name, "PuntosBlancos")
            response = "¿Presenta puntos negros en la cara?"
            conversation_state = "get_PuntosNegros"
        else: 
            response = "¿Presenta puntos negros en la cara?"
            conversation_state = "get_PuntosNegros"
    
    elif conversation_state == 'get_PuntosNegros':
        if input.lower() == 's':
            save_to_kb(name, "PuntosNegros")
            response = "¿Presenta papulas en la cara?"
            conversation_state = "get_Papulas"
        else: 
            response = "¿Presenta papulas en la cara?"
            conversation_state = "get_Papulas"

    elif conversation_state == 'get_Papulas':
        if input.lower() == 's':
            save_to_kb(name, "Papulas")
            response = "¿Padece de piel grasa y escamosa, así como caspa en la cara?"
            conversation_state = "get_Seborrea"
        else: 
            response = "¿Padece de piel grasa y escamosa, así como caspa en la cara?"
            conversation_state = "get_Seborrea"

    elif conversation_state == 'get_Seborrea':
        if input.lower() == 's':
            save_to_kb(name, "Seborrea")
            response = "¿Presenta vesiculas en la boca?"
            conversation_state = "get_Vesiculas"
        else: 
            response = "¿Presenta vesiculas en la boca?"
            conversation_state = "get_Vesiculas"

    elif conversation_state == 'get_Vesiculas':
        if input.lower() == 's':
            save_to_kb(name, "Vesiculas")
            response = "¿Presenta dolor de boca?"
            conversation_state = "get_DolorBoca"
        else: 
            response = "¿Presenta dolor de boca?"
            conversation_state = "get_DolorBoca"    

    elif conversation_state == 'get_DolorBoca':
        if input.lower() == 's':
            save_to_kb(name, "DolorBoca")
            
            diag = fol_fc_ask(doctor_kb, expr("Enfermo({}, x)".format(name)))
            diag = list(diag)

            if len(diag) > 0:
                response = "El diagnóstico: " + (", ".join(str(e[x]) for e in diag)) + ". Quisieras conocer tratamientos?" + "\n" 
                conversation_state = "get_Treatment"
            else: 
                response = "Felicidades! No presentas condiciones de la piel."
        else: 
            diag = fol_fc_ask(doctor_kb, expr("Enfermo({}, x)".format(name)))
            diag = list(diag)

            if len(diag) > 0:
                response = "El diagnóstico: " + (", ".join(str(e[x]) for e in diag)) + ". Quisieras conocer tratamientos?" + "\n" 
                conversation_state = "get_Treatment"
            else: 
                response = "Felicidades! No presentas condiciones de la piel."
                

    elif conversation_state == "get_Treatment":
        if input.lower() == "s":

            treatment = fol_fc_ask(doctor_kb, expr("Tratamiento({}, x)".format(name)))
            treatment = list(treatment)

            if len(treatment) > 0:
                response = "Los tratamientos: " + (", ".join(str(e[x]) for e in treatment)) + ". Quisieras conocer recomendaciones?" + "\n" 
                conversation_state = "get_Rec"
        else:
            response = "De acuerdo. Recuerde asistir a un médico certificado!"
        
    elif conversation_state == "get_Rec":
        if input.lower() == "s":

            recs = fol_fc_ask(doctor_kb, expr("Recomendacion({}, x)".format(name)))
            recs = list(recs)

            if len(recs) > 0:
                response = "Las recomendaciones son: " + (", ".join(str(e[x]) for e in recs)) + ". Recuerde asistir a un médico certificado!" + "\n" 
            else:
                response = "No hay recomendaciones."
        else:
            response = "De acuerdo. Recuerde asistir a un médico certificado!"


        

    return response   

win = Tk()
win.title('Medical ChatBot')

win.geometry("400x500")
win.resizable(width=False, height=False)

win.iconbitmap('doctor_icon.ico')

ChatLog = Text(win, bd=0, bg="white", wrap=WORD,height="8", width="50", font=("Arial", 10))
ChatLog.config(state=DISABLED)


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    response = process_input(msg)

    

    # Display response in chat window
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, "You: " + msg + "\n")
    ChatLog.insert(END, "Dr. Bot: " + response + "\n")
    ChatLog.config(state=DISABLED)

    # Clear entry field
    EntryBox.delete(0, END)

    ChatLog.yview(END)




SendButton = Button(win, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )
EntryBox = Text(win, bd=0, bg="white",width="29", height="5", font="Arial")



scrollbar = Scrollbar(win, command=ChatLog.yview, cursor="heart")


#Bind scrollbar to Chat window

ChatLog['yscrollcommand'] = scrollbar.set


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

win.mainloop()
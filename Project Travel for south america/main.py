from ai import call_gpt

def main():
    lugares_turisticos_sudamerica = {
    "Brasil": ["Cristo Redentor", "Pan de Azúcar", "Amazonas", "Cataratas del Iguazú", "Copacabana"],
    "Argentina": ["Buenos Aires", "Cataratas del Iguazú", "Perito Moreno", "Bariloche", "Mendoza","ishuaia","patagonia"],
    "Colombia": ["Cartagena", "Bogotá", "Medellín", "Parque Tayrona", "Eje Cafetero"],
    "Chile": ["Desierto de Atacama", "Torres del Paine", "Isla de Pascua", "Valparaíso", "Santiago"],
    "Perú": ["Machu Picchu", "montaña arcoiris", "Lago Titicaca", "Líneas de Nazca", "huayhuash","reserva pacaya samiria","mancora"],
    "Venezuela": ["Salto Ángel", "Canaima", "Los Roques", "Mérida", "Mochima"],
    "Ecuador": ["Galápagos", "Quito", "Mitad del Mundo", "Baños", "Cuenca"],
    "Uruguay": ["Montevideo", "Punta del Este", "Colonia del Sacramento", "Cabo Polonio", "Piriápolis"],
    "Bolivia": ["Salar de Uyuni", "La Paz", "Lago Titicaca", "Potosí", "Sucre"],
    "Paraguay": ["Asunción", "Encarnación", "Ruinas Jesuíticas", "Cerro Cora", "Saltos del Monday"]
    }
   
    print("I am your travel guide through South America")
    name=str(input("whats's your name: "))
    print(f"Welcome, {name}!")
    
    mostrar_lugares(lugares_turisticos_sudamerica)
    pais_elegido=seleccionar_pais(lugares_turisticos_sudamerica)
    if pais_elegido:
        lugares = lugares_turisticos_sudamerica[pais_elegido]
        seleccionar_lugar(lugares, pais_elegido)

  
def mostrar_lugares(lugares_turisticos_sudamerica):
    print("Que pais quieres conoces")
    for idx, pais in enumerate(lugares_turisticos_sudamerica.keys(), start=1):
        print(f"{idx}. {pais}")

def seleccionar_pais(lugares_turisticos_sudamerica):
    try:
        seleccion= int(input("\nSelect a country by entering its number: "))
        pais_elegido=list(lugares_turisticos_sudamerica.keys())[seleccion-1]
        
        for idx,lugar in enumerate (lugares_turisticos_sudamerica[pais_elegido], start=1):
                print(f"{idx}. {lugar}")
        
        return  pais_elegido

    except (ValueError, IndexError):
        print("\nInvalid selection. Please enter a valid number from the list.")

def seleccionar_lugar(lista_lugares, pais):
    respuesta=True
    informacion=["How to get there?","Cost", "What to eat?", "Tips","security" ]
    try:
        seleccion = int(input("\nSelect a place by entering its number: "))
        lugar_elegido = lista_lugares[seleccion - 1]

        descripcion_lugar=call_gpt(f"Make a brief description of the {lugar_elegido} of the country {pais} simple and most importantly")
        print(descripcion_lugar)
        
        while respuesta:
            print("\nWhat do you want to know?: ")
            for idx, categoria in enumerate(informacion,start=1):
                print(f'{idx}.{categoria}')
            print("0. Salir")
            try: 
                info_preg = int(input("Select an option: "))
                if info_preg==1:
                    como_llegar=call_gpt(f'Give a brief summary of how to get to {lugar_elegido}')
                    print(como_llegar)
                elif info_preg==2:
                    costo=call_gpt(f'Give a brief summary of the approximate cost to visit {lugar_elegido}, without food and without accommodation.')
                    print(costo)
                elif info_preg==3:
                    que_comerr=call_gpt(f'Give a brief summary of what to eat in {lugar_elegido}')
                    print(que_comerr)
                elif info_preg==4:
                    consejos=call_gpt(f'Provide a brief summary of practical information and tips for {lugar_elegido}, such as the best time to travel, money (ATM locations), local culture ')
                    print(consejos)
                elif info_preg==5:
                    consejos=call_gpt(f'Provide a brief summary of location-specific safety information for {lugar_elegido}, including areas to avoid and emergency numbers (police, fire, ambulance).')
                    print(consejos)
                else:
                    break
            except (ValueError, IndexError):
                print("Por favor, ingresa un número válido.")

    except (ValueError, IndexError):
        print("\n Invalid selection. Please enter a valid number from the list.")

        
if __name__ == "__main__":
    main()
    
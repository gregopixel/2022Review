# Molecular Mass Calculator by Gregory



class Element:                    # Create Class of elements with properties of name and mass
  def __init__(self, name, mass):
    self.name = name
    self.mass = mass

# Assign masses to elements
H = Element("Hydrogen", 1.008)
He = Element("Helium", 4.0026)
Li = Element("Lithium", 6.94)
Be = Element("Beryllium", 9.0122)
B = Element("Boron", 10.81)
C = Element("Carbon", 12.011)
N = Element("Nitrogen", 14.007)
O = Element("Oxygen", 15.999)
F = Element("Fluorine", 18.998)
Ne = Element("Neon", 20.180)
Na = Element("Sodium", 22.990)
Mg = Element("Magnesium", 24.305)
Al = Element("Aluminium", 26.982)
Si = Element("Silicon", 28.085)
P = Element("Phosphorous", 30.974)
S = Element("Sulfur", 32.06)
Cl = Element("Chlorine", 35.45)
Ar = Element("Argon", 39.948)
K = Element("Potassium", 39.098)
Ca = Element("Calcium", 40.078)

# List of Elements
strElements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]
objElements = [H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca]

# Function to ask for repeat
def Again():
  ask = input("Want to go again? [Y/N]: ")
  while ask.lower() not in ["y", "n", "yes", "no"]: # Trap error
    ask = input("Unexpected input. \n Want to go again? [Y/N]: ") 
  if ask.lower() in ["yes", "y"]:
    Start() # Call start to restart
  

def Start():
  # START
    global molecule
    global totalMass
    totalMass = 0 # initial mass of molecule is zero


    # Placed in while loop checking whether totalMass == 0 to trap errors users may make.


    while totalMass == 0:
        molecule = input("Enter molecule: ") # Read input from user
        print("")
        findElement() # call function to find elements

        if totalMass == 0:  # Trap errors
            print("No elements were recognised, make sure to capitalise the first letter of each element.")

        else:
            # Final total mass
            print(f"Total mass: {totalMass}") # Print final total mass
      
            Again() # Call function to ask if user wants to go again


def findElement():
    global molecule
    global totalMass
    for i in range (19, -1, -1): # See how many of each element is present
      elementCount = molecule.count(strElements[i]) # Number of each element
      if elementCount > 0: # only shows elements that are present in the user's input
        pos = molecule.find(strElements[i]) # Find position of element
        if i in {0, 4, 5, 6, 15}:
          '''
          Checks if letters after H, B, C, N, and S correspond to actual elements (e.g. H and He),
          so code will not count He as He AND H
          '''
          
          if len(molecule) > pos+1:
            if molecule[pos+1] in {"e", "l", "a", "i"}:
              continue
            elif ord(molecule[pos+1]) > 96 and ord(molecule[pos+1]) < 123:
              break


        
        if pos < len(molecule) - 1:
          if ord(molecule[pos+1]) > 48 and ord(molecule[pos+1]) < 58: # Check if there is a number after the element
            elementCount *= int(molecule[pos+1]) # Multiply element by number
          elif ord(molecule[pos+1]) > 96 and ord(molecule[pos+1]) < 123: # If there is a letter, check for number after that letter
            if pos+2 < len(molecule): # Ensure that there is actually something after the second letter
              if ord(molecule[pos+2]) > 48 and ord(molecule[pos+2]) < 58:
                elementCount *= int(molecule[pos+2]) # Multiply element by number

        
        print(f"Number of {strElements[i]}: {elementCount}") # Print number of individual elements 
        print(f"Mass of {strElements[i]}: {objElements[i].mass*elementCount}\n") # Print total mass of that element

        
        
        
        totalMass += objElements[i].mass*elementCount # Add all elements together




Start() # Initiate program

































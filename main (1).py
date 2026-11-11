from pyscript import display, document

#Drill
def add_new_guy(e):
    document.getElementById('result').innerHTML = ' '
    student_firstname = document.getElementById('fname').value
    student_lastname = document.getElementById('lname').value
    student_name = str(student_firstname) + " " + str(student_lastname)
    
    Teacher = {'Maria Dela Cruz'}
    G10 = {'John Doe'}
    G11 = {'Jane Doe'}
    G12 = {'Juan Dela Cruz'}

    Club_New_Student = G10 | G11 | G12 | Teacher
    Club_New_Student.add(student_name)

    display(f'The club members are: {Club_New_Student}', target='result')
    display(f'There are {len(Club_New_Student)} members in the club.', target='result')

#Skillstest
nonmetal_Elements = {
    "H": "Hydrogen. Symbol. H. Atomic Number. 1. Atomic Mass. 1.008.",
    "He": "Helium. Symbol. He. Atomic Number. 2. Atomic Mass. 4.003.",
    "C": "Carbon. Symbol. C. Atomic Number. 6. Atomic Mass. 12.011.",
    "N": "Nitrogen. Symbol. N. Atomic Number. 7. Atomic Mass. 14.007.",
    "O": "Oxygen. Symbol. O. Atomic Number. 8. Atomic Mass. 15.999.",
    "F": "Fluorine. Symbol. F. Atomic Number. 9. Atomic Mass. 18.998.",
    "Ne": "Neon. Symbol. Ne. Atomic Number. 10. Atomic Mass. 20.180.",
    "P": "Phosphorus. Symbol. P. Atomic Number. 15. Atomic Mass. 30.974.",
    "S": "Sulfur. Symbol. S. Atomic Number. 16. Atomic Mass. 32.060.",
    "Cl": "Chlorine. Symbol. Cl. Atomic Number. 17. Atomic Mass. 35.450.",
    "Ar": "Argon. Symbol. Ar. Atomic Number. 18. Atomic Mass. 39.948.",
    "Se": "Selenium. Symbol. Se. Atomic Number. 34. Atomic Mass. 78.971.",
    "Br": "Bromine. Symbol. Br. Atomic Number. 35. Atomic Mass. 79.904.",
    "Kr": "Krypton. Symbol. Kr. Atomic Number. 36. Atomic Mass. 83.798.",
    "I": "Iodine. Symbol. I. Atomic Number. 53. Atomic Mass. 126.904.",
    "Xe": "Xenon. Symbol. Xe. Atomic Number. 54. Atomic Mass. 131.293.",
    "At": "Astatine. Symbol. At. Atomic Number. 85. Atomic Mass. [210].",
    "Rn": "Radon. Symbol. Rn. Atomic Number. 86. Atomic Mass. [222].",
    "Ts": "Tennessine. Symbol. Ts. Atomic Number. 117. Atomic Mass. [294].",
    "Og": "Oganesson. Symbol. Og. Atomic Number. 118. Atomic Mass. [294]."
}


def ElementFind(e):
    document.getElementById('output').innerHTML = ' '
    NM_Element_Symbol = document.getElementById('NMelement').value

    
    display(nonmetal_Elements.get(NM_Element_Symbol, ("The element is not a nonmetal.")))

# seatwork
from pyscript import display, document

def view_club(e):
    document.getElementById('result').innerHTML = ' '
    verifclubmember = ['Dwayne Chua', 'Marcus Viray', 'Jesse Villante', 'Kaizer Chua', '6 7']
    firstname = document.getElementById('fname').value
    lastname = document.getElementById('lname').value
    unverifclubmember = str(firstname) + " " + str(lastname)
    club_member_checker = unverifclubmember in verifclubmember

display_message = (f'Sorry {unverifclubmember}, your name is not on the list.', f'Congratulations {unverifclubmember}! You are now part of the Unknown Club.')
display(display_message[club_member_checker], target='result')



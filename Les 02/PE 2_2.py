# Schrijf nu ook een programma dat de gebruiker vraagt om de score van een multiplechoice toets. Het
# programma bepaalt of het resultaat voldoende is. Bij meer dan 15 punten is de deelnemer geslaagd!

score = eval(input('Geef je score '))
if score > 15:
    print('Gefeliciteerd')
    print('Met een score van ' + str(score) + ' ben je geslaard!')

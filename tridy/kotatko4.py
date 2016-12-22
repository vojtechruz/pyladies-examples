# Abychom snadno rozeznali nekolik mnoukajicich kotatek, kazde kotatko nyni mnouka svym jmenem
# V metode zamnoukej() nyni muzeme pristupovat k atributum instance pres self. self.jmeno pristupuje k atributu jmeno
# aktualni instance.


class Kotatko:
    def zamnoukej(self, zprava):
        print('{}: {}'.format(self.jmeno, zprava))


kotatko = Kotatko()
kotatko.jmeno = 'Micka'
kotatko.zamnoukej('Mnau?')
kotatko.zamnoukej('Mnau!!!!')

jineKotatko = Kotatko()
jineKotatko.jmeno = 'Mourek'
jineKotatko.zamnoukej('Mnaaaaaaau!')

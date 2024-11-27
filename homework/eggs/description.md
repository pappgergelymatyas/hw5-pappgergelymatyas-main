# Tojás

Van két tojásunk és egy 100 emeletes épület. Meg kell mondanunk, hogy mi az a legmagasabb szint, ahonnan leejtve még nem törik össze egy tojás. Ha már az első emeletről leesve összetörik a tojás akkor 0-t ad vissza, ha a 100. emeletről ledobva sem törik össze akkor pedig 100-at.

Ennél a feladatnál már találtok egy működő megoldást az eggs fájlban. Ennél egy jobb megoldást kellene írnotok. Annál jobb egy megoldás minél alacsonyabb a tesztnél kiírt **mean performance** értéke. Azaz átlagosan kevesebb dobás kell, hogy megtalálja a jó megoldást. Itt is van egy paraméter, ami egy függvény a breaks. Amikor ezt meghívjátok a függvényetekben az számít egy dobásnak. A teszt futásakor ez adja vissza, hogy eltörik e egy tojás egy adott emeleten vagy nem.

## parameters:

- breaks: function

  it takes an integer parameter of the floor number and returns a boolean value of whether the egg breaks or not

## returns:

an integer, the number of the highest floor where the egg doesn’t break

## Tesztek:

A VSCode tesztelő felületén, ha azokat a teszteket futtatjátok, ahol a legfelső szint a Python Tests névvel rendelkezik, akkor a teszt output
kiír néhány extra hasznos információt azon túl, hogy jó e a megoldás. Ezek a következők:

- Minimum drops
- Maximum drops
- Mean drops
- Total successful tests
- Wrong results
- Optimal performance?

Illetve, ha push után a GitHub felületén nézitek a teszteket akkor is látni fogjátok ezeket.

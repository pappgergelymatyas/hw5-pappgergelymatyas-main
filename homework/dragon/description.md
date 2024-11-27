# Sárkány

Egy elszabadult sárkányt keresünk, aki mindig a legnagyobb tehenet eszi meg a királyságban, majd ledől a környéken aludni. Mivel van tehénverseny minden évben, van egy listánk a tehenekről, méret szerint (csökkenő sorrend). Hogy fogunk neki a sárkány megtalálásának, hogy minél kevesebb farmra kelljen menni?

A bineáris keresés átismétlése a sárkányos feladaton keresztül. Mindenki talál a tasks mappában egy dragon
nevű fájlt, amiben ki kell javítani egy függvényt.

Ez a függvény picit eltér az órán felvázolt struktúrától. Itt már nem egy lista lesz a függvényetek paramétere, hanem egy is_dead függvény, amit nem nektek kell megírnotok. Ezt majd a tesztelő függvény adja meg. Nektek csak annyira kell használnotok, hogyha meghívjátok ezt a függvényt egy adott számmal, akkor az visszaadja, hogy az adott számú tehén halott e. **Figyeljetek arra, hogy akkor kaptok igaz értéket visszatérési értékként, ha a tehén halott.** A másik paraméteretek pedig a tehenek száma.

## parameters:

- is_dead: function

  it takes an integer parameter of the cows rank in the weight contest and returns a boolean value of whether a cow is dead or not

- number_of_cows: int

  the number of cows in the kingdom

## returns:

an integer, the rank of the largest (the one with the smallest rank starting from 1) cow that is dead, 0 if all alive

and it checks the least amount of cows possible

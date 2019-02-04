Calcul de taxes
---------------

Within the repository folder, run:
~~~bash
python calcul_de_taxes.py
~~~

You will be prompt to enter the content of your cart. Follow the instructions and enter each item according to the following format **<Qty\> <Item\> à <Price\>**

###### Examples:
* 1 livre à 12.49
* 1 CD musical à 14.99
* 1 barre de chocolat à 0.85

---

##### Tests

_Tests have been written but don't cover the whole perspective of what could go wrong._

To run the tests run:
~~~bash
python -m unittest calcul_de_taxes_test.py
~~~

###### Notes:
No function was written to check the user's input.
The program was not written in OOP though it could have
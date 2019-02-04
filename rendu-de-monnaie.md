Story: Rendu de monnaie
=======================


# Enoncé
Les supermarchés s’équipent de plus en plus de caisses automatiques. La plupart de ces caisses n’ acceptent que le paiement par carte bancaire bien qu’une part non négligeable de consommateurs paye encore en espèces (avec des billets et des pièces).

Une des problématiques rencontrées avec le paiement en espèces est le rendu de monnaie : comment rendre une somme donnée de façon optimale, c'est-à-dire avec le nombre minimal de pièces et billets ? C'est un problème qui se pose à chacun de nous quotidiennement, à fortiori aux caisses automatiques.

Dans cet exercice, on vous demande d’essayer de trouver une solution optimale pour rendre la monnaie dans un cas précis : quand une caisse automatique ne contient que des pièces de **2€**, des billets de **5€** et de **10€**.

Pour simplifier le problème, nous considérerons que toutes ces pièces et billets sont disponibles en **quantité illimitée**.

Voici quelques exemples de rendu de monnaie :
- Monnaie à rendre : 6
    - Solutions possibles : 2 + 2 + 2
    - Solution optimale : 2 + 2 + 2
- Monnaie à rendre : 1
    - Solutions possibles : solution impossible
- Monnaie à rendre : 10
    - Solutions possibles : 2 + 2 + 2 + 2 + 2, 5 + 5, 10
    - Solution optimale : 10
- Monnaie à rendre : 9223372036854775807
    - Solutions possibles : 922337203685477580*10 + 5 + 2

Le rendu de monnaie est exprimé par un objet **Change**. Cet objet a 3 propriétés : **coin2**, **bill5** et **bill10** qui, respectivement, stockent le nombre de pièces de 2€, de billets de 5€ et de billets de 10€.

Par exemple, si on reprend l’exemple n°2 du tableau (6€), on devrait obtenir un objet **Change** avec : **coin2** vaut 3 (3 pièces de 2€) **bill5** vaut 0 (pas de billet de 5€) **bill10** vaut 0 (pas de billet de 10€)

Implémentez la fonction **optimalChange($s)** qui retourne un objet **Change** contenant les pièces et billets dont la somme vaut **$s**. S’il est impossible de rendre la monnaie (comme dans l’exemple n°1), retournez **NULL**.

Pour obtenir un maximum de points votre solution devra toujours rendre la monnaie quand c’est possible et avec le nombre minimal de pièces et billets.

Données : *$s* est toujours un entier strictement positif inférieur ou égal à 2^31 - 1, soit *2147483647*.



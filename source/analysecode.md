# Analyse d'une page de code

## Introduction
Dans ce chapitre, je vais analyser le code de mon composant CoursePage, une page modèle de cours. Le code se situe en annexe et j'y ferai référence dans ce chapitre. Le but de ce chapitre est de comprendre dans l'ensemble comment fonction un composant VueJs et de repérer ce qui permet de produire tel élément de la page

## Analyse du code

Pour commencer, je vais expliquer la balise `template` qui englobe le code de la ligne 1 à 58. Le but de cette commande est de définir le modèle du composant. Ainsi, lorsque l’on appelera le composant, le système prendra le contenu de la balise `template`.  

Je vais ensuite m’intéresser à la balise `div` de classe `allpage`, se situant aux lignes 2 et 57. Ces dernières englobe l'entièreté de la page. C’est ici que le développeur code ce qui est destiné à apparaître dans la page. Il est intéressant d’utiliser une balise `div` car cela permet au système de mieux comprendre le code. De plus, il est facilement possible d'aplliquer des propriétés CSS à l’ensemble du composant en sélectionnant le contenu de cette balise. 

Ce qui se trouve à l’intérieur des `<!-- -->` sont des commentaires. Bien qu’il ne soit pas nécessaire d’en ajouter, ils permettent à celui qui examine le code de mieux comprendre ce dernier. En effet, on utilise les commentaires pour donner des informations spécifiques quant au fonctionnement du code. 

Pour ajouter à cela, il faut observer le composant `Menubar` entre les lignes 8 et 17. Ceci est un composant provenant directement de la bibliothèque de composants PrimeVue qui code un menu situé en haut de la page. Ce composant utilise lui aussi des `templates`. En effet, il est possible d’ajouter ce que l’on veut voir apparaître à gauche du menu (`template #start`) et ce que l’on veut voir à droite (`template #end`).

De plus, la balise `router-link`, située notamment à l'intérieur d'une balise `Button` ligne 11, permet de naviguer dans l'application. En effet, cette balise fait référence au router-vue, qui va se charger de changer l'URL de la page consultée et de rediriger l'utilisateur vers la page souhaitée. Cette opération est comparable au `link href=""` utilisé en HTML.

Aux lignes 26 et 29 se trouve le composant `sidebar`. Ce dernier est, comme son nom l'indique, une barre latérale que l'on peut ouvrir et fermer. Cet outil peut être très utile pour naviguer facilement à travers l'application sans devoir chercher un bouton dans la page. Il peut-être intéressant de s'intéresser au composant `PanelMenu` (ligne 28) contenu dans cette barre latérale. En effet, il fait référence par le terme `items` aux informations se trouvant dans le `script` entre les lignes 66 et 89. Cette méthode permet de définir à un seul endroit ces informations et, par conséquent, de ne pas devoir les réécrire de nombreuses fois. Il suffit de les appeler par le `model="items"`.

La balise `script`, située aux lignes 60 et 94, permet d’intégrer un script JavaScript au composant. Dans le composant étudié, il est possible de s'en servir pour indiquer différents éléments regroupés sous un terme que l’on peut ajouter au code juste en appelant ce dernier. Cela permet d’économiser de nombreuses lignes de code et de simplifier le travail car tout est regroupé en un seul endroit. 

En outre, il faut observer observer dès la ligne 96 la balise `style`. C'est principalement à l’intérieur de cette balise que l’on va indiquer les propriétés CSS que l’on veut appliquer au composant. C’est ici que le style de la page est principalement définit. 

## Conclusion 

Ainsi, j’ai présenté le fonctionnement générale du code définissant le composant `CoursePage`. La structure du code se compose de cinq parties : le `template`, la `div`, le `script` et le `style`. Il est important d’avoir une page bien structurée pour que le système puisse facilement comprendre le code et éviter des problèmes qui pouvent faire perdre un temps précieux au développeur. 

```{figure} images/coursepage1.png
---
width: 70%
---
Première partie de la page de cours
```

```{figure} images/coursepage2.png
---
width: 70%
---
Deuxième partie de la page de cours avec la sidebar ouverte
```

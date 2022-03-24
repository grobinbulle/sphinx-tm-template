# Analyse d'une page de code

## Introduction
Dans ce chapitre, je vais analyser le code de mon composant ListCourses, permettant à l'utilisateur de choisir son cours. Son code se situe en annexe en j'y ferai donc référence dans ce chapitre. Comme énoncé dans l'annexe, le code analysé est la version du 3 mars 2022 et ce n'est donc pas la version définitive. Ceci est dû à des problèmes rencontrés avec l'application repl sur laquelle je code mon application. 

## Analyse du code

Pour commencer, je vais expliquer la balise `template` qui englobe le code de la ligne 1 à 120. Le but de cette commande est de définir le modèle du composant. Ainsi, lorsque l’on appelera notre composant, le système prendra le contenu de la balise `template`. 

Entre les lignes 3 et 8 se trouve le contenu de la balise `head`. Le but de cette dernière est d’ajouter les informations générales de notre page que le moteur de recherche va utiliser. Ces indications ne sont donc pas visibles lorsque l’on regarde le rendu de notre page mais ne sont donc pas inutiles. On peut s’en servir pour indiquer le titre de notre page comme à la ligne 4, mais aussi pour donner une description à notre page comme l’on peut l’observer à la ligne 6. 

Je vais ensuite m’intéresser à la balise `body`, se situant aux lignes 9 et 118. Ces dernières contiennent le corps du composant. C’est donc ici que le développeur code ce qui est destiné à apparaître dans la page. Il est intéressant d’utiliser une balise `body` car cela permet au système de mieux comprendre le code. De plus, on peut facilement aplliquer des   propriétés CSS à l’ensemble du composant en sélectionnant le contenu de cette balise. 

Ce qui se trouve à l’intérieur des `<!-- -->` sont des commentaires. Bien qu’il ne soit pas nécessaire d’en ajouter, ils permettent à celui qui examine le code de mieux comprendre ce dernier. En effet, on utilise les commentaires pour donner des informations spécifiques quant au fonctionnement du code. 

Pour ajouter à cela, on observe le composant `Menubar` aux lignes 12 et 25. Ceci est un composant provenant directement de la bibliothèque de composants PrimeVue qui code pour un menu situé en haut de la page. Ce composant utilise lui aussi des `templates`. En effet, il est possible d’ajouter ce que l’on veut voir apparaître à gauche du menu (`template #start`) et ce que l’on veut voir à droite du menu (`template #end`). 

Le deuxième composant principal fonctionne de manière analogue à celui que l’on vient de regarder. En effet, le composant `Card` provient aussi de PrimeVue. Il code pour une simple carte qui peut être personnalisée par la suite. La seule différence notable entre les fonctionnements de ces deux composants est que la `template #start` code pour le haut de la page et la `template #end` pour le bas de la page. 

La balise `script`, située aux lignes 123 et 157, permet d’intégrer un script JavaScript au composant. Dans le composant que l’on étudie, on s’en sert pour indiquer différents éléments regroupés sous un terme que l’on peut ajouter au code juste en appelant ce dernier. Cela permet d’économiser de nombreuses lignes de code et de simplifier le travail car tout est regroupé en un seul endroit. 

En outre, on peut observer dès la ligne 160 la balise `style`. C'est principalement à l’intérieur de cette balise que l’on va indiquer les propriétés CSS que l’on veut appliquer au composant. C’est donc ici que l’on définit principalement le style de la page. 

## Conclusion 

Ainsi, j’ai présenté le fonctionnement générale du code définissant le composant `ListCourses`. La structure du code se compose de cinq parties : le `template`, le `head`, le `body`, le `script` et le `style`. Il est important d’avoir une page bien structurée pour que le système puisse facilement comprendre le code et éviter des problèmes qui peuvent faire perdre un temps précieux au développeur. 
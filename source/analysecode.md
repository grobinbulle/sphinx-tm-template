# Analyse d'une page de code

## Introduction
Dans ce chapitre, je vais analyser le code de mon composant CoursePage, une page modèle de cours que j'ai créée. Le code se situe en annexe et j'y ferai référence dans ce chapitre. Le but de ce chapitre est de comprendre dans l'ensemble comment fonctionne un composant VueJs et de repérer ce qui permet de produire tel élément de la page

## Analyse du code

Pour commencer, je vais expliquer la balise `template` qui englobe le code de la ligne 1 à 58. Le but de cette commande est de définir le modèle du composant. Ainsi, lorsque l’on appelera le composant, le système prendra le contenu de la balise `template`.  

Je vais ensuite m’intéresser à la balise `div` de classe `allpage`, se situant aux lignes 2 et 57. Ces dernières englobent l'ensemble de la page. C’est ici que le développeur code ce qui est destiné à apparaître. L'intérêt d'une balise `div` est de permettre au système de mieux comprendre le code. De plus, il est facilement possible d'appliquer des propriétés CSS à l’ensemble du composant en sélectionnant le contenu de cette balise. 

Ce qui se trouve à l’intérieur des `<!-- -->` sont des commentaires. Bien qu’il ne soit pas nécessaire d’en ajouter, ils permettent à celui qui examine le code de mieux le comprendre. En effet, on utilise les commentaires pour donner des informations spécifiques quant au fonctionnement du code. 

De surcroît, il faut observer le composant `Menubar` entre les lignes 8 et 17. Ceci est un composant provenant directement de la bibliothèque des composants PrimeVue qui code un menu situé en haut de la page. Il utilise lui aussi des `templates`. En effet, il est possible d’ajouter ce que l’on veut voir apparaître à gauche du menu (`template #start`) et ce que l’on veut voir à droite (`template #end`).

De plus, la balise `router-link`, située notamment à l'intérieur d'une balise `Button` ligne 11, permet de naviguer dans l'application. En effet, cette balise fait référence au router-vue, lequel va se charger de changer l'URL de la page consultée et de rediriger l'utilisateur vers la page souhaitée. Cette opération est comparable au `link href=""` utilisé en HTML.

Aux lignes 26 et 29 se trouve le composant `sidebar`. Ce dernier est, comme son nom l'indique, une barre latérale que l'on peut ouvrir et fermer. Cet outil peut être très utile pour naviguer facilement à travers l'application sans devoir chercher un bouton dans la page. Il peut être intéressant de s'intéresser au composant `PanelMenu` (ligne 28) contenu dans cette barre latérale. En effet, le terme `items` fait référence aux informations se trouvant dans le `script` entre les lignes 66 et 89. Cette méthode permet de définir à un seul endroit ces informations et, par conséquent, de ne pas devoir les réécrire de nombreuses fois. Il suffit de les appeler par le `model="items"`.

La balise `script`, située aux lignes 60 et 94, permet pour sa part d’intégrer un script JavaScript au composant. Dans celui qui est étudié, il est possible de s'en servir pour indiquer différents éléments regroupés sous un terme que l’on peut ajouter au code juste en appelant ce dernier. Cela permet d’économiser de nombreuses lignes de code et de simplifier le travail, tout étant regroupé en un seul endroit. 

Observons ensuite la balise `style` dès la ligne 96. C'est principalement à l’intérieur de cette balise que seront indiquées les propriétés CSS que l’on souhaite appliquer au composant. C’est principalement ici que le style de la page est défini. 

## Conclusion 

J’ai présenté le fonctionnement général du code définissant le composant `CoursePage`. La structure du code se compose de quatre parties: le `template`, la `div`, le `script` et le `style`. Une page bien structurée est une garantie que le système peut facilement comprendre le code et éviter des problèmes qui peuvent faire perdre un temps précieux au développeur. 

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

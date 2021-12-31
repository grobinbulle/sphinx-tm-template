# Les Technologies utilisées
## Introduction
Dans ce chapitre, nous allons découvrir et approfondir les technologies utilisées pour le développement de l’outil. Bien que la plupart des technologies comme le HTML, le CSS et le JavaScript ne soient pas méconnues des étudiants, d’autres technologies comme le Vue 3 ainsi que PrimeVue restent encore inconnues pour la plupart des élèves. Nous allons ainsi développer ces quelques technologies tout en approfondissant davantage ces deux dernières. 
## Le HTML
L’HTML (HyperText Marckup Language ou langage de balise pour l’hypertexte) constitue la structure de base des pages web. Cette technologie se charge des éléments “brutes” de la page sans aucune mise en page et sans aucune “décoration”. Il s’agit du minimum pour le bon fonctionnement de notre page. L’HTML désigne aussi les liens reliant les pages les unes aux autres, une base fondamentale pour la navigation.  

Pour ce faire, cette technologie fonctionne par des balises comme header, p,  title, … Ces balises servent à intégrer un élément à notre page ainsi qu’à en indiquer la valeur (paragraphe de texte, image, titre, …). L’élément à intégrer est inscrit entre la balise ouvrante (p) et la balise fermante (/p). 

Voici un exemple de page HTML. 

`````{admonition} Code Markdown
````markdown
```html
<!DOCTYPE html>
<html>
    <head>
        <title> Donne ici un titre à ta page html </title>
        <meta charset="UTF-8">
        <link href="C:\Users\Robin\OneDrive - EDUETATFR\TM 2021-2022\essai\css_exemple.css" rel="stylesheet" type="text/css">
        <script src="js.js"></script>
    </head>
    <body>
        <h1> Voici le titre principal </h1>
        <p> Et voilà le texte de la page</p>
        <h2> On crée les autres titres de la même manière </h2>
        <h3> On peut créer jusqu'à six niveaux de titres </h3>
        <h4> Titre de niveau 4 </h4>
        <h5> Titre de niveau 5 </h5>
        <h6> Titre de niveau 6 </h6>
        <p> Chaque titre peut contenir du texte, comme ici </p> 
    </body> 
</html>

```
````
`````

Voici un code HTML, nous n’allons pas examiner chaque ligne dans les moindres détails mais il peut être intéressant d’en regarder quelques-unes. 

De la ligne 3 à la ligne 6 s’étend la balise head, le contenu inséré dans cette partie n’est pas visible directement sur la page, il vient plutôt donner des informations sur cette dernière comme l’encodage (ici UTF-8) ou le nom de la page. 

Des lignes 7 à 16, nous observons le body de notre page, ceci représente la partie visible de la page web et donc le contenu que l’utilisateur rencontrera lors de sa navigation sur le site. 

Les différentes balises h1, h2, h3, … expriment différentes tailles de titre : plus le nombre est grand, plus le titre est petit. Cette balise permet aussi de mettre directement son contenu en gras sans l’intervention d’une autre balise spécifique 

```{figure} images/html_rendu.png
---
width: 100%
---
une légende
```

Voici donc le rendu de ce même code. Comme vous pouvez le constater, il s’agit ici vraiment de la base d’une page internet. Les éléments sont notamment tous alignés à gauche, tous écrits avec la même police et tous en noir. Il ne faut pas s’en cacher, cette page n’est pas du tout esthétique et est encore bien loin des pages que l’on consulte de nos jours. Pas de problème, ce problème sera réglé par le CSS qui viendra rendre notre page plus agréable et jolie. 


## Le CSS
Le CSS (Cascading Style Sheet ou feuille de style en cascade) est une technologie visant à décrire la présentation des pages HTML. Il est ainsi possible de définir le positionnement d’un élément, de le colorer, de changer ses dimensions, … Une multitude de possibilités s’offrent au développeur pour créer la page qu’il souhaite.  

Pour ce faire, nous devons sélectionner un élément par des “sélecteurs” pour ensuite lui effectuer les diverses modifications souhaitées. Ainsi, si nous voulons changer la couleur de tous les paragraphes de textes en rouge, il suffit de sélectionner l’élément <p> et de lui appliquer la commande “color : red”. Ainsi l’ensemble du texte des paragraphes deviendra rouge. 

Voici un exemple de code CSS. 

`````{admonition} Code Markdown
````markdown
```css
body{
    background-color: grey
}
p{
    color : red;
    font-size: 20px;
    margin-left: 30px;
}

```
````
`````

Comme vous le voyez ci-dessus, il s’agit du code CSS que nous allons appliquer à notre page. Nous y distinguons le sélecteur body (venant modifier l’ensemble de la page) ainsi que le sélecteur p (venant modifier tous les paragraphes de texte). Chaque sélecteur et suivi de deux accolades qui enfermeront les différentes instructions. Ces dernières sont séparées d’un point-virgule pour les distinguer clairement les unes des autres. 

```{figure} images/rendu_css.png
---
width: 100%
---
une légende
```
Voici donc ce code appliqué à la page HTML étudiée précédemment. Nous pouvons constater que le fond de la page est devenu gris, que le texte des paragraphes a grossi, est devenu rouge et s’est déplacé vers la gauche. Vous l’aurez deviné, ces changements ont été provoqués par l’ajout de notre code CSS. Ainsi, avec quelques notions d’Anglais, nous pouvons aisément deviner quelle ligne a provoqué quel changement. Cependant, notre page reste statique. En effet, il n’y a aucun effet et rein de dynamique. Pour coder une page visant à interagir avec l’utilisateur, nous allons nous intéresser au JavaScript.  

## Le JavaScript
Le JavaScript (ou JS) est la troisième et dernière base d’une page web avec le HTML et le CSS. Cette technologie permet notamment de dynamiser une page et de permettre une interaction avec l’utilisateur. Le JavaScript est, comme son nom l’indique, un langage de script. Un script est une suite d’instructions se referrant à une page. Pour interpréter le JavaScript, nous devons utiliser un interpréteur (en majorité Chrome) qui viendra appliquer les différentes commandes à la page web en question.  

Voici un exemple de code très simple en JavaScript. 
`````{admonition} Code Markdown
````markdown
```JavaScript

alert("Bonjour!");

function createParagraph() {
    let para = document.createElement('p');
    para.textContent = 'Vous avez cliqué !';
    document.body.appendChild(para);
  }

```
````
`````
Ce code crée deux éléments distincts dans notre page. En premier lieu, la commande alert(“Bonjour!) ouvrira un petit élément lorsqu’on lance la page. L’utilisateur devra appuyer sur un bouton pour enlever cette alarme et accéder au contenu de la page. 

En second lieu, nous créons une fonction, à l’aide de la commande function, qui créera un boutton affichant du texte à chaque click. La commande function permettra d’utiliser notre fonction dans notre page HTML par la suite. Dans ce code, nous créons une variable para qui affichera “Vous avez cliqué !” à chaque click. 

`````{admonition} Code Markdown
````markdown
```html

<!DOCTYPE html>
<html>
    <head>
        <title> Donne ici un titre à ta page html </title>
        <meta charset="UTF-8">
        <link href="C:\Users\Robin\OneDrive - EDUETATFR\TM 2021-2022\essai\css_exemple.css" rel="stylesheet" type="text/css">
        <script src="js.js"></script>
    </head>
    <body>
        <button onclick="createParagraph()">Cliquez-moi!</button>
    </body> 
</html>

```
````
`````
Ici, nous utilisons notre code directement dans notre page HTML. Nous utilisons notre fonction dans une balise button. Ainsi, à chaque click effectué sur ce bouton, la page web affichera “Vous avez clické !”. 

```{figure} images/alert_javascript.png
---
width: 100%
---
une légende
```
Nous voyons ci-dessus l’appel de la fonction alerte. Comme indiqué précédemment, cette simple ligne de code engendre cette petite fenêtre en haut de notre page. Cette alerte ne s’enlèvera que lorsque l’utilisateur clickera sur le bouton ok. Cela fait, l’utilisateur pourra ensuite accéder au contenu de notre page web. 

```{figure} images/click_test_img.png
---
width: 100%
---
une légende
```

Finalement, voilà ce que notre fonction createparagraph rend lorsqu’elle est appelée. En effet, après avoir cliqué 3 fois sur le bouton “Cliquez-moi!”, le texte “Vous avez cliqué” est apparu autant de fois. En théorie, ce programme peut s’effectuer à l’infini, de quoi s’amuser pendant de longues heures à essayer de faire apparaître notre phrase au maximum de reprises... 

## Vue.Js
### Introduction
Vue.js est connu tel un Framework JavaScript front-end open-source. En d’autres termes, Vue.js est une bibliothèque libre d’accès permettant la création de composants JavaScript visant la création d’application web. Utilisé notamment par Nintendo, Alibaba ou encore la plateforme de streaming Netflix, ce Framework vise à simplifier le travail d’un développeur front-end lors de la construction de sa page web. De nombreux Frameworks front-ends sont réputés des développeurs comme AngularJs ou encore ReactJs mais notre choix s’est bel et bien porté sur Vue.js. Nous verrons d’abord pourquoi notre décision s’est porté sur cette technologie et nous expliquerons ainsi les avantages que possède ce dernier par rapport à ses concurrents. De plus, nous approfondirons notamment les composants VueJs si chers aux yeux des développeurs front-end. 
### Pourquoi utiliser VueJs ?
Le choix d’un Framework dans le cadre d’un travail de maturité n’était pas chose aisée. En effet, nous recherchons un logiciel facile à la compréhension et à l’utilisation pour permettre à un étudiant, n’ayant pratiquement aucune base dans le monde du développement web, de pouvoir coder son projet sans à devoir dépenser un temps conséquent rien que pour comprendre le fonctionnement de sa technologie. Vue.js s’est démarqué des autres Framework par les nombreux avantages qu’il propose.
- 
# Les Technologies utilisées
## Introduction
Dans ce chapitre, nous allons découvrir et approfondir les technologies utilisées pour le développement de l’outil. Bien que la plupart des technologies comme le HTML, le CSS et le JavaScript ne soient pas méconnues des étudiants, d’autres technologies comme le Vue 3 ainsi que la bibliothèque de composant PrimeVue restent encore inconnues pour la plupart des élèves. Nous allons ainsi présenter ces technologies tout en approfondissant davantage les deux dernières. 
## Le HTML
L’HTML (HyperText Markup Language ou langage à balises pour l’hypertexte) constitue la structure de base des pages Web. Cette technologie se charge des éléments “brutes” de la page sans aucune mise en page et sans aucune “décoration”. L’HTML désigne aussi les liens reliant les pages les unes aux autres, une base fondamentale pour la navigation.  

Pour ce faire, cette technologie fonctionne par des balises. Ces balises servent à intégrer un élément à notre page ainsi qu’à en indiquer la valeur (paragraphe de texte, image, titre, …). L’élément à intégrer définit par les balises est inscrit entre la balise ouvrante et la balise fermante (contenant une barre oblique avant de nommer la balise qui doit être fermée).
Pour produire la page souhaitée à partir du code, ce dernier passe tout d'abord par le DOM (Document Object Model), qui va permettre aux programmes de lire et de manipuler le contenu de la page. Il fournit ainsi une représentation structurée des éléments de la page sous forme d'un arbre.

Voici un exemple de page HTML. 


```{code-block} html
---
linenos: true
---

<!DOCTYPE html>
<html>
    <head>
        <title> Donne ici un titre à ta page html </title>
        <meta charset="UTF-8">
        <link href="css_exemple.css" rel="stylesheet" type="text/css">
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

De la ligne 3 à 6 s’étend la balise :command:`head`. Le contenu inséré dans cette partie n’est pas visible directement sur la page. Il vient plutôt donner des informations sur cette dernière comme l’encodage (ici UTF-8) ou le nom de la page. 

Des lignes 7 à 16, nous observons le corps de la page, qui représente la partie visible de la page Web et donc le contenu que l’utilisateur voit en naviguant sur le site. 

Les différentes balises :command:`h1`, :command:`h2`, :command:`h3`, … expriment différentes tailles de titre : plus le nombre est grand, plus le titre est petit. Cette balise permet aussi de mettre directement son contenu en gras sans l’intervention d’une autre balise spécifique 

```{figure} images/html_rendu.png
---
width: 50%
---
Rendu de la page HTML
```

La figure 1 montre le rendu de ce même code. Comme on peut le constater, il s’agit vraiment de la base d’une page Web. Les éléments sont notamment tous alignés à gauche, tous écrits avec la même police et tous en noir. Il ne faut pas s’en cacher, cette page n’est pas du tout esthétique et est encore bien loin des pages que l’on consulte de nos jours. Pas de soucis, ce problème sera réglé par le CSS qui viend rendre notre page plus agréable et jolie. 


## Le CSS
Le CSS (Cascading Style Sheet ou feuille de style en cascade) est une technologie visant à décrire la présentation des pages HTML. Il est ainsi possible de définir le positionnement d’un élément, de le colorer, de changer ses dimensions, … Une multitude de possibilités s’offrent au développeur pour créer la page qu’il souhaite.  

Pour appliquer un style à un élément de la page, il faut sélectionner un élément par un sélecteur pour ensuite lui appliquer les diverses propriétés style souhaitées. Ainsi, si l'on veut changer la couleur de tous les paragraphes de texte en rouge, il suffit de sélectionner les éléments correspondants et de leur appliquer la propriété :command:`color: red`. Ainsi, l’ensemble du texte des paragraphes deviend rouge. 

Voici un exemple de code CSS. 


```{code-block}css
---
linenos: true
---
div {
  background-color:#339;
  color:#fff;
  padding:15px;
  border-bottom:5px solid red;
  margin-bottom:15px;
    }
```


Considérons le code CSS. Nous y distinguons le sélecteur :command:`body` (venant modifier l’ensemble de la page) ainsi que le sélecteur :command:`p` (venant modifier tous les paragraphes de texte). Chaque sélecteur est suivi de deux accolades qui enferment les différentes propriétés. Ces dernières sont séparées d’un point-virgule pour les distinguer clairement les unes des autres. 

```{figure} images/css_ex.png
---
width: 50%
---
Rendu de notre page CSS
```
En appliquant le code CSS vu précédemment, on peut constater que le fond de la page est devenu gris, que le texte des paragraphes a grossi, est devenu rouge et s’est déplacé vers la gauche. Vous l’aurez deviné, ces changements ont été provoqués par l’ajout de notre code CSS. Ainsi, avec quelques notions d’Anglais, nous pouvons aisément deviner quelle ligne a provoqué quel changement. Cependant, notre page reste statique. En effet, il n’y a aucun effet et rien de dynamique. Pour coder une page visant à interagir avec l’utilisateur, on utilise le JavaScript.  

## Le JavaScript
Le JavaScript (ou JS) est la troisième et dernière base d’une page Web avec le HTML et le CSS. Cette technologie permet notamment de dynamiser une page et de créer une interaction avec l’utilisateur. Le JavaScript est, comme son nom l’indique, un langage de script. Un script Java est une suite d’instructions se referrant à une page. Pour interpréter le JavaScript, il faut utiliser un interpréteur (en majorité Chrome) qui viendra appliquer les différentes commandes à la page Web en question.  

Voici un exemple de code très simple en JavaScript. 

```{code-block}JavaScript
---
linenos: true
---
alert("Bonjour!");

function createParagraph() {
    let para = document.createElement('p');
    para.textContent = 'Vous avez cliqué !';
    document.body.appendChild(para);
}
```

Ce code crée deux éléments distincts dans notre page. En premier lieu, la commande :command:`alert("Bonjour!")`alert ouvrire une boîte de dialogue lorsqu’on lance la page. L’utilisateur doit alors appuyer sur un bouton pour fermer cette alarme et accéder au contenu de la page. 

En second lieu, on définit une fonction, à l’aide de la commande :command:`function`, qui crée un boutton affichant du texte à chaque clic. Cette fonction peut être appelée par la suite. Dans ce code, nous créons une variable :command:`para` qui permet d'afficher “Vous avez cliqué !” à chaque clic. 


```{code-block}html
---
linenos: true
---

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

Ci-dessus, nous utilisons le code directement dans la page HTML. La fonction :command:`createParagraph` est utilisée dans une balise button. Ainsi, à chaque clic effectué sur ce bouton, la page Web affiche “Vous avez cliqué !”. 

```{figure} images/alert_javascript.png
---
width: 70%
---
Rendu de l'alerte JavaScript
```
La figue 3 montre l’appel de la fonction alerte. Comme indiqué précédemment, cette simple ligne de code engendre cette boîte de dialogue en haut de notre page. Cette alerte ne s’enlève que lorsque l’utilisateur clique sur le bouton OK. Cela fait, l’utilisateur peut ensuite accéder au contenu de la page Web. 

```{figure} images/click_test_img.png
---
width: 50%
---
Rendu du code JavaScript
```

La figure 4 montre l'effet de la fonction :command:`createParagraph` rend lorsqu’elle est appelée. En effet, après que l'utilisateur ait cliqué trois fois sur le bouton “Cliquez-moi!”, le texte “Vous avez cliqué” apparaît autant de fois. En théorie, ce programme peut s’exécuter à l’infini. 

## Vue.Js
### Introduction
Vue.js est un Framework JavaScript front-end open-source. En d’autres termes, Vue.js est une bibliothèque libre d’accès permettant la création de composants JavaScript visant la création d’application Web. Utilisé notamment par Nintendo, Alibaba ou encore la plateforme de streaming Netflix, ce Framework vise à simplifier le travail d’un développeur front-end lors de la construction de sa page Web. De nombreux Frameworks front-ends sont connus des développeurs comme Angular ou encore ReactJs mais notre choix s’est porté sur Vue.js. Ce framework étant bien moins connu des étudiants que les technologies abordées précédemment, nous approfondirons davantage cette dernière afin de comprendre pourquoi les frameworks sont utiles aux développeurs. Nous verrons d’abord pourquoi notre décision s’est porté sur cette technologie et nous expliquerons ainsi les avantages que possède ce dernier par rapport à ses concurrents. De plus, nous approfondirons notamment le concept de composants VueJs. 
### Pourquoi utiliser VueJs ?
Le choix d’un framework dans le cadre d’un travail de maturité n’était pas chose aisée. En effet, nous recherchions un framework facile à comprendre et à l’utilisation. Vue.js s’est finalement démarqué des autres framework par les nombreux avantages qu’il propose. 

En effet, VueJs est l'un des frameworks les plus légers du marché par son poids avoisinant les 20 Ko.  

De plus, Vue.js est très accessible pour un développeur débutant : son apprentissage et sa syntaxe sont faciles à comprendre et un résultat probant peut déjà être obtenu en quelques lignes de code. Cet aspect fut primordial au choix de cette technologie car il permettait ainsi à un étudiant n’ayant que très peu de bases dans le monde du développement Front-end de pouvoir coder efficacement le plus rapidement possible sans à devoir perdre des heures précieuses pour assimiler le fonctionnement de sa technologie. VueJs utilise le bundler nommé "Webpack". Ce dernier transforme le code VueJs en code Javascript. Cela permet donc à Vue d'avoir des commandes plus complètes et plus facile à comprendre lorsque l'on les lit.

Un autre avantage à ne pas négliger est que ce framework a été conçu pour pouvoir être utilisé de manière incrémentale. De ce fait, il peut être aisément possible d’ajouter un élément Vue sur une page contenant des éléments provenants de technologies différentes, ce qui n’est pas anodin pour un développeur devant à multiples reprises utiliser différentes bibliothèques de composants pour satisfaire ses besoins. Par conséquent, Vue.js s’adapte aux différents besoins du développeur. 

De plus, Vue utilise aussi le concept de réactivité automatique. Ce mechanisme permet au framework de détecter si les données de la page ont été modifiées ou non. Ainsi, le framework met automatiquement la page à jour. VueJs construit un DOM virtuel gardant les traces des modifications Vue pour qu'elles soient ainsi lues et mise à jour dans le vrai DOM.

Pour ajouter à cela, Vue est une technologie très performante. Ce framework est effectivement fort efficace peu importe s’il s’agit d’une simple page ou d’une application multi-pages. Le rendu final est donc rapide, fluide et la synchronisation des données est efficace. 

Enfin, cette technologie offre la possibilité de créer facilement ses propres directives ou composants que l’on peut sauvegarder sous des fichiers “.vue” (Single File Component). Ces composants se suffisent à eux-mêmes, possédant leurs propres props et style. En outre, ces derniers peuvent même être réutilisés ailleurs dans le code et même dans d’autres projets. 

Ainsi, Vue.js demeurait être une solution adéquate dans le cadre d’un travail de maturité. Cette technologie peut aisément et rapidement se comprendre et être utilisée par le développeur. Elle s’adapte aussi à ses différents besoins et peut être mêlée facilement à des technologies différentes. 
### Les composants
Des éléments importants apporté par VueJs sont les composants. Ces derniers viennent enrichir le HTML de façon modulaire. En d’autres termes, il nous est possible de créer un élément codé en HTML et possédant ses propres fonctionnalités que l’on peut facilement intégrer à notre code par le biais d’une simple balise personnalisée. Le catalogue de fonctionnalités du HTML étant limité, les composant permettent d’y ajouter de nombreux éléments plus complexes qui sont d’une grande utilité pour le développeur. Ainsi, nous allons observer le fonctionnement de ces fameux composants si utiles aux développeurs. 
#### Créer un composant
Tout d’abord, nous allons comprendre comment créer un composant très simple. Nous allons produire un élément qui, lorsque la balise que l’on a créée est appelée, contiendra la balise HTML :command:`First component`. 

```{code-block}vue
---
linenos: true
Vue.component('exemple-composant',{ 

template : '<p>First component</p>'' 

}) 

```
Il existe de nombreuses manières de créer un composant mais celle-ci est particulièrement simple à assimiler. La balise que l’on a créée s’appelle :command:`exemple-composant`. Par conséquent, pour utiliser ce composant, il suffit d'utiliser la balise <exemple-composant>. Par la suite, nous devons utiliser ce composant tel une instance Vue créée par la commande JavaScript : 
```{code-block}JavaScript
---
linenos: true
---
new Vue({  
  el: '#tuto'  
}); 

```
Enfin, nous devons appeler notre composant dans notre code HTML par sa balise personnalisée insérée dans une div. 

Ainsi, il est affiché "First component".

De plus, les composants peuvent être utilisés plusieurs fois dans le même code et même dans d’autres pages de code n’ayant pas nécessairement un rapport particulier avec la première page. 
#### Les props
Pour rendre notre composant plus intéressant, il est possible d’y ajouter des :command:`props`. 
```{code-block}vue
---
linenos: true
---
Vue.component('nom', { 
  props: ['nom'], 
  template: '<p>Mon nom est {{nom}}</p>' 
}); 
```
Les :command:`props` sont des propriétés dont le composant attend une valeur. Dans cet exemple, il est créé une propriété ‘nom’ qui n’affichera pas la même valeur selon ce que l’on codera en HTML: 
```html
<div id="tuto"> 
  <nom nom="Toto"></nom> 
</div> 
```
Ainsi, la propriété attendue par le composant sera “Toto”. Par conséquent, notre code affichera : 

Mon nom est Toto 

```{figure} images/schema_props.jpg
---
width: 50%
---
Schéma expliquant le fonctionnement de notre composant 
```
### PrimeVue
Enfin, VueJs est complété par la bibliothèque de composants PrimeVue. Comme son nom l’indique, PrimeVue recense plus de 80 composants différents déjà intégralement prêt pour être intégrés dans le code. Il ne suffit ainsi qu’à copier-coller les lignes de codes disponibles dans la documentation de l’application pour afficher l’élément en question sur sa page Web. Pour certains composants, il existe même plusieurs modèles comme par exemple l'orientation (verticale ou horizontale) du composant. Evidemment, il est possible de modifier facilement le composant par quelques propriétés CSS. En résumé, PrimeVue permet un accès libre à plus de 80 composants que l’on peut intégrer et modifier aisément dans le code. 
### Conclusion
Ainsi, notre choix concernant le framework utlisé dans le cadre de ce travail de maturité s’est porté sur Vue.js. En effet, son accessibilité ainsi que sa flexibilité sont des atouts majeurs en la faveur de ce Framework. Cette technologie permet notamment d’enrichir le catalogue HTML par le biais de composants, des entités possédant leur propre style et leurs propres fonctionnalités. Cela est utile au codeur pour ajouter un élément complexe dans son projet en quelques minutes seulement sans à devoir cravacher des journées entières pour fabriquer ce qu’il désire. 
## Conclusion
Nous arrivons au terme de ce chapitre consacré aux différentes technologies constituant mon travail de maturité. Nous constatons qu’un nombre conséquent de technologies différentes sont utilisée dans le cadre de ce travail. Comme pour toute application Web, mon projet utilise des 3 technologies de “base” que sont le HTML, le CSS et le JavaScript. Cependant, nous avons décidé de travailler avec le framework VueJs ainsi que la bibliothèque de composants PrimeVue. Effectivement, ces derniers viennent diminuer en conséquence le temps à consacrer à notre projet mais aussi et surtout à se mettre dans la peau d’un développeur professionnel qui, lui, use quotidiennement de frameworks.  
 
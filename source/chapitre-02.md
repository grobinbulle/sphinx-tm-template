# Les technologies utilisées
## Introduction
Ce chapitre découvre et approfondit les technologies utilisées pour le développement de l’outil. Bien que la plupart des technologies comme le HTML, le CSS et le JavaScript ne soient pas méconnues des étudiants, d’autres technologies comme le Vue 3 ainsi que la bibliothèque de composants PrimeVue restent encore étrangères à la plupart des élèves. Ces technologies seront présentées de manière générale, avec un approfondissement pour Vue 3 et PrimeVue. 
## Le HTML
L’HTML (HyperText Markup Language ou langage à balises pour l’hypertexte) constitue la structure de base des pages Web. Cette technologie se charge des éléments “brutes” de la page sans aucune mise en page et sans aucune “décoration”. L’HTML désigne aussi les liens reliant les pages les unes aux autres, une base fondamentale pour la navigation.  

Cette technologie fonctionne par des balises. Ces dernières servent à intégrer un élément à la page ainsi qu’à en indiquer la valeur (paragraphe de texte, image, titre, …). L’élément à intégrer, défini par les balises, est inscrit entre la balise ouvrante et la balise fermante (contenant une barre oblique avant de nommer la balise qui doit être fermée).
Pour produire la page souhaitée à partir du code, ce dernier passe tout d'abord par le DOM (Document Object Model), lequel va permettre aux programmes de lire et de manipuler le contenu de la page. Il fournit une représentation structurée des éléments de la page sous forme d'un arbre.

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

De la ligne 3 à 8 s’étend la balise `head`. Le contenu inséré dans cette partie n’est pas visible directement sur la page. Il vient plutôt donner des informations sur cette dernière comme l’encodage (ici UTF-8) ou le nom de la page. 

Des lignes 9 à 18, on observe le corps de la page, représenté par la balise `body`, laquelle représente la partie visible de la page Web et donc le contenu que l’utilisateur voit lors de la navigation. 

Les différentes balises `h1`, `h2`, `h3`, … expriment pour leur part différentes tailles de titre: plus le nombre est grand, plus le titre est petit. Cette balise permet de mettre directement son contenu en gras sans l’intervention d’une autre balise spécifique 

```{figure} images/html_rendu.png
---
width: 50%
---
Rendu de la page HTML
```

La figure 1 montre le rendu de ce même code. Comme on peut le constater, il s’agit vraiment de la base d’une page Web. Les éléments sont notamment tous alignés à gauche, tous écrits avec la même police et tous en noir. Il ne faut pas s’en cacher, cette page n’est pas du tout esthétique et est encore bien loin d'une page moderne. Pas de souci, ce problème sera réglé par le CSS qui viendra rendre notre page plus agréable et jolie. 


## Le CSS
Le CSS (Cascading Style Sheet ou feuille de style en cascade) est une technologie visant à décrire la présentation des pages HTML. Il est par exemple possible de définir le positionnement d’un élément, de le colorer, de changer ses dimensions, … C'est une multitude de possibilités qui s’offrent ainsi au développeur pour créer la page souhaitée.  

Pour appliquer un style à un élément de la page, il faut sélectionner cet élément par un "sélecteur" pour lui appliquer ensuite les diverses propriétés "style" souhaitées. Ainsi, s'il est voulu de changer la couleur de tous les paragraphes de texte en rouge, il suffit de sélectionner les éléments correspondants et de leur appliquer la propriété `color: red`. Le tout est joué: l’ensemble du texte des paragraphes passent au rouge. 

Voici un exemple de code CSS. 


```{code-block}
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


Considérons le code CSS: on y distingue le sélecteur `div` (venant modifier les `div` de la page). Le sélecteur est suivi de deux accolades qui enferment les différentes propriétés. Ces dernières sont séparées d’un point-virgule pour les distinguer sans ambiguité les unes des autres. 

```{figure} images/css_ex.png
---
width: 50%
---
Rendu de notre page CSS
```
En appliquant le code CSS (voir ci-dessus) à une page HTML quelconque, force est de constater que le fond des deux paragraphes est devenu bleu, que le texte a été centré et qu'une bordure rouge s'est ajoutée en bas des deux paragraphes. Vous l’aurez deviné, ces changements ont été provoqués par l’ajout de notre code CSS. Ainsi, avec quelques notions d’anglais, nous pouvons aisément trouver quelle ligne a provoqué quel changement. Cependant, notre page reste statique. Aucun effet et rien de dynamique. Pour coder une page visant à interagir avec l’utilisateur, le JavaScript va se révéler très utile.  

## Le JavaScript
Le JavaScript (ou JS) est la troisième et dernière base d’une page Web avec le HTML et le CSS. Cette technologie permet notamment de dynamiser une page et de créer une interaction avec l’utilisateur. Le JavaScript est, comme son nom l’indique, un langage de script. Un script Java est une suite d’instructions se reférant à une page. Pour l'appliquer, utilisons un interpréteur (en majorité Chrome) qui viendra appliquer les différentes commandes à la page Web en question.  

Voici un exemple de code très simple en JavaScript. 

```{code-block}
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

Ce code crée deux éléments distincts dans la page. En premier lieu, la commande `alert("Bonjour!")` ouvre une boîte de dialogue lorsqu’on lance la page. L’utilisateur doit alors appuyer sur un bouton pour fermer cette alarme et accéder au contenu de la page. 

En second lieu, on définit une fonction `createParagraph` à l’aide de la commande `function`, qui crée un bouton affichant du texte à chaque clic, cette fonction peut être appelée par la suite. Dans ce code, une variable `para` est créée, ce qui permet d'afficher “Vous avez cliqué!” à chaque clic. 


```{code-block}
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
        <button onclick="createParagraph()">Click me!</button>
    </body> 
</html>

```

Ci-dessus, le code est utilisé directement dans la page HTML. La fonction `createParagraph` est employée dans une balise button. Après chaque clic effectué sur ce bouton, la page Web affiche “Vous avez cliqué !”. 

```{figure} images/alert_javascript.png
---
width: 70%
---
Rendu de l'alerte JavaScript
```
La figure 3 montre l’appel de la fonction `alert`. Comme indiqué précédemment, cette simple ligne de code engendre cette boîte de dialogue en haut de notre page. Cette alerte ne s’enlève que lorsque l’utilisateur clique sur le bouton OK. Après avoir effectué cela, l’utilisateur peut ensuite accéder au contenu de la page Web. 

```{figure} images/java_image.jpg
---
width: 50%
---
Rendu du code JavaScript
```

La figure 4 montre l'effet de la fonction `createParagraph` lorsqu’elle est appelée. En effet, après avoir cliqué trois fois sur le bouton “Cliquez-moi!”, le texte “Vous avez cliqué” apparaît autant de fois. En théorie, ce programme peut s’exécuter à l’infini. 

## VueJs
### Introduction
VueJs (dernière version: Vue 3) est un framework JavaScript front-end open-source. En d’autres termes, VueJs est une bibliothèque libre d’accès permettant la création de composants JavaScript visant la création d’application Web. Utilisé notamment par Nintendo, Alibaba ou encore la plateforme de streaming Netflix, ce framework simplifie le travail d’un développeur front-end lors de la construction de sa page Web. De nombreux frameworks front-ends sont connus des développeurs comme Angular ou encore ReactJs, mais le choix s’est porté sur VueJs. Ce framework étant bien moins connu des étudiants que les technologies abordées précédemment, approfondissons davantage cette dernière afin de comprendre pourquoi les frameworks sont utiles aux développeurs. Voilà pourquoi ma décision s’est portée sur cette technologie. Il faut en expliquer les avantages par rapport à ses concurrents. De plus, le concept de composants VueJs y est abordé. 
### Pourquoi utiliser VueJs ?
Le choix d’un framework dans le cadre d’un travail de maturité n’était pas chose aisée. En effet, on recherchait un framework facile à comprendre et à utiliser. VueJs s’est finalement démarqué des autres frameworks par les nombreux avantages qu’il propose. 

En effet, VueJs est l'un des frameworks les plus légers du marché par son poids avoisinant les 20 Ko.  

De plus, il est très accessible à un développeur débutant: son apprentissage et sa syntaxe sont faciles à comprendre et un résultat probant peut déjà être obtenu en quelques lignes de code seulement. Cet aspect fut primordial lors du choix de cette technologie, car il permet un codage efficace et rapide à un étudiant n’ayant que très peu de bases dans le monde du développement front-end. VueJs utilise le bundler nommé "Webpack". Ce dernier transforme le code VueJs en code Javascript. Cela permet donc à Vue d'avoir des commandes plus complètes et plus faciles à comprendre lors de la lecture.

Autre avantage à ne pas négliger, ce framework a été conçu pour être utilisé de manière incrémentale. De ce fait, il est aisément possible d’ajouter un élément Vue sur une page contenant des éléments provenant de technologies différentes. Ceci n’est pas anodin pour un développeur qui doit utiliser différentes bibliothèques de composants. Par conséquent, VueJs s’adapte aux différents besoins du développeur. 

De plus, Vue utilise le concept de réactivité automatique. Ce méchanisme permet au framework de détecter si les données de la page ont été modifiées ou non. Ainsi, le framework la met automatiquement à jour. VueJs construit un DOM virtuel gardant les traces des modifications Vue pour qu'elles soient lues et mises à jour dans le vrai DOM.

Vue est une technologie très performante. Ce framework est fort efficace. Peu importe qu’il s’agisse d’une simple page ou d’une application multi-pages. Le rendu final est donc rapide, fluide et la synchronisation des données performante. 

Enfin, cette technologie offre la possibilité de créer facilement ses propres directives ou composants que l’on sauvegardera sous des fichiers “.vue” (Single File Component). Ces composants se suffisent à eux-mêmes, possédant leurs propres props et style. En outre, ces derniers ont la propriété de pouvoir être réutilisés ailleurs dans le code et même dans d’autres projets. 

VueJs restait une solution adéquate dans le cadre d’un travail de maturité. Cette technologie peut aisément et rapidement se comprendre et être utilisée par le développeur. Elle s’adapte à ses différents besoins et peut être mêlée facilement à des technologies différentes. 
### Les composants
Des éléments importants apportés par VueJs sont les composants. Ces derniers viennent enrichir le HTML de façon modulaire. En d’autres termes, il est possible de créer un élément codé en HTML avec ses propres fonctionnalités. Il s'intègre alors facilement à notre code par le biais d’une simple balise personnalisée. Le catalogue de fonctionnalités du HTML est limité, mais les composants permettent d’y ajouter de nombreux éléments plus complexes qui peuvent s'avérer très utiles pour le développeur. Observons le fonctionnement de ces fameux composants. 
#### Créer un composant
Tout d’abord, il faut comprendre comment créer un composant très simple. Il s'agit de produire un élément qui, lorsque la balise créée est appelée, contiendra la balise HTML `First component`. 

```{code-block}
---
linenos: true
---
Vue.component('exemple-composant',{ 

template : '<p>First component</p>'' 

}) 

```
Il existe de nombreuses manières de concevoir un composant, mais celle-ci est particulièrement simple à assimiler. La balise que l’on a créée s’appelle `exemple-composant`. Par conséquent, pour utiliser ce composant, il suffit d'utiliser la balise <exemple-composant>. Par la suite, on s'en servira telle une instance Vue créée par la commande JavaScript: 
```{code-block}
---
linenos: true
---
new Vue({  
  el: '#tuto'  
}); 

```
Enfin, notre composant peut être appelé dans le code HTML par sa balise personnalisée insérée dans une div. 

Il est affiché "First component".

De plus, les composants peuvent être utilisés plusieurs fois dans le même code ou dans d’autres pages de code n’ayant pas nécessairement un rapport particulier avec la première page. 
#### Les props
Pour rendre le composant plus intéressant, il est possible d’y ajouter des `props`. 
```{code-block}
---
linenos: true
---
Vue.component('nom', { 
  props: ['nom'], 
  template: '<p>Mon nom est {{nom}}</p>' 
}); 
```
Les `props` sont des propriétés dont le composant attend une valeur. Dans cet exemple, une propriété ‘nom’ n’affichera pas la même valeur selon ce que l’on codera en HTML: 
```html
<div id="tuto"> 
  <nom nom="Toto"></nom> 
</div> 
```
La propriété attendue par le composant sera “Toto”. Par conséquent, le code affichera: 

Mon nom est Toto 

```{figure} images/schema_props.jpg
---
width: 50%
---
Schéma expliquant le fonctionnement du composant 
```
### PrimeVue
Enfin, VueJs est complétée par la bibliothèque de composants PrimeVue. Comme son nom l’indique, PrimeVue recense plus de 80 composants différents déjà prêts à être intégrés dans le code. Rien de plus simple: il suffit pour cela de copier-coller les lignes de codes disponibles dans la documentation de l’application pour afficher l’élément en question sur sa page Web. Pour certains composants, il existe même plusieurs modèles comme l'orientation (verticale ou horizontale) du composant. Evidemment, la possibilité de modifier facilement le composant par quelques propriétés CSS existe.
### Conclusion sur VueJs
Le choix concernant le framework utilisé dans le cadre de ce travail de maturité s’est porté sur VueJs. En effet, son accessibilité ainsi que sa flexibilité sont des atouts majeurs. Cette technologie permet notamment d’enrichir le catalogue HTML par le biais de composants, des entités possédant leur propre style et leurs propres fonctionnalités. Cela est utile au développeur pour ajouter un élément complexe dans son projet sans devoir cravacher des journées entières. 
## Conclusion
Nous arrivons au terme de ce chapitre consacré aux différentes technologies constituant mon travail de maturité. Comme pour toute application Web, mon projet utilise les trois technologies de “base” que sont le HTML, le CSS et le JavaScript. Cependant, nous avons décidé, avec mon professeur, de travailler avec le framework VueJs, ainsi que la bibliothèque de composants PrimeVue. Un choix qui s'est avéré judicieux: ces composants diminuent en conséquence le temps à consacrer au projet, mais aussi et surtout à se mettre dans la peau d’un développeur professionnel qui, lui, utilise quotidiennement les frameworks. 
 
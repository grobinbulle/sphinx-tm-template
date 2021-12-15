# Les Technologies utilisées
{ref}`header_target`
Dans ce chapitre, nous allons découvrir et approfondir les technologies utilisées pour le développement de l’outil. Bien que la plupart des technologies comme le HTML, le CSS et le JavaScript ne soient pas méconnues des étudiants, d’autres technologies comme le Vue 3 ainsi que PrimeVue restent encore inconnues pour la plupart des élèves. Nous allons ainsi développer ces quelques technologies tout en approfondissant davantage ces deux dernières. 
## Le HTML
L’HTML (HyperText Marckup Language ou langage de balise pour l’hypertexte) constitue la structure de base des pages web. Cette technologie se charge des éléments “brutes” de la page sans aucune mise en page et sans aucune “décoration”. Il s’agit du minimum pour le bon fonctionnement de notre page. L’HTML désigne aussi les liens reliant les pages les unes aux autres, une base fondamentale pour la navigation.  

Pour ce faire, cette technologie fonctionne par des balises comme header, p,  title, … Ces balises servent à intégrer un élément à notre page ainsi qu’à en indiquer la valeur (paragraphe de texte, image, titre, …). L’élément à intégrer est inscrit entre la balise ouvrante (p) et la balise fermante (/p). 

Voici un exemple de page HTML. 

```{figure} images/html_exemple.png
---
width: 100%
---
une légende
```
Voici un code HTML, nous n’allons pas examiner chaque ligne dans les moindres détails mais il peut être intéressant d’en regarder quelques-unes. 

De la ligne 3 à la ligne 6 s’étend la balise head, le contenu inséré dans cette partie n’est pas visible directement sur la page, il vient plutôt donner des informations sur cette dernière comme l’encodage (ici UTF-8) ou le nom de la page. 

Des lignes 7 à 16, nous observons le body de notre page, ceci représente la partie visible de la page web et donc le contenu que l’utilisateur rencontrera lors de sa navigation sur le site. 

Les différentes balises <h1>, <h2>, <h3>, … expriment différentes tailles de titre : plus le nombre est grand, plus le titre est petit. Cette balise permet aussi de mettre directement son contenu en gras sans l’intervention d’une autre balise spécifique 

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

```{figure} images/css_exemple.png
---
width: 100%
---
une légende
```

Comme vous le voyez ci-dessus, il s’agit du code CSS que nous allons appliquer à notre page. Nous y distinguons le sélecteur body (venant modifier l’ensemble de la page) ainsi que le sélecteur p (venant modifier tous les paragraphes de texte). Chaque sélecteur et suivi de deux accolades qui enfermeront les différentes instructions. Ces dernières sont séparées d’un point-virgule pour les distinguer clairement les unes des autres. 

```{figure} images/rendu_css.png
---
width: 100%
---
une légende
```
Voici donc ce code appliqué à la page HTML étudiée précédemment. Nous pouvons constater que le fond de la page est devenu gris, que le texte des paragraphes a grossi, est devenu rouge et s’est déplacé vers la gauche. Vous l’aurez deviné, ces changements ont été provoqués par l’ajout de notre code CSS. Ainsi, avec quelques notions d’Anglais, nous pouvons aisément deviner quelle ligne a provoqué quel changement. 

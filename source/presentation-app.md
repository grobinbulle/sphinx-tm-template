# Présentation de l'application
## Introduction
Voici, dans cet ultime chapitre, le rendu final de l’application développée dans le cadre de ce travail de maturité. Ainsi, j’explique les différentes parties des pages du projet et décris en quoi j'estime qu'elles permettent un meilleur apprentissage.  

## Page de cours
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
Deuxième partie de la page de cours
```
En figures 1 et 2 se trouve un modèle de page de cours. Il est évident qu’il n’était pas nécessaire de recréer chaque page de la plateforme d’origine. Celle-ci constitue un exemple qui permettra lors de la création des autres pages d’avoir une idée générale du rendu.  

Si l’on regarde l’ensemble de la page, il est évident que le design de cette dernière est épuré. Il n’y a en effet que peu de couleurs différentes et la page n’est pas trop chargée. Ceci permet à l’utilisateur de consulter la page sans être perturbé par une profusion de détails. Le titre du chapitre est mis en valeur par la bande bleue qui se trouve derrière lui. J’ai choisi de mettre un arrière-plan composé de deux couleurs, afin de rendre la page plus attractive et dynamique. 

Un autre élément facilitant l'apprentissage est la barre latérale observable en figure 2. Cette dernière permet de naviguer facilement à travers l’application sans devoir revenir en arrière. On peut aussi décider de la laisser ouverte lors de la navigation, mais il est possible la fermer afin de mieux apprécier son contenu. Ainsi, ce dernier s’adaptera de manière à occuper l’ensemble de la fenêtre. 

Une autre nouveauté qu’apporte cette page est un espace de notes, visible en figure 2. Cet espace permet à l’étudiant de mentionner ce qu’il trouve important, mais aussi de prendre note des différentes remarques effectuées à l’oral pendant le cours. Réunir toutes les informations sur un seul support facilitera sans aucun doute les révisions. De plus, l'espace de notes offre la possiblité de mettre en forme son texte et de mieux organiser ses notes.

## Page d'accueil

```{figure} images/index_tm.png
---
width: 70%
---
Page d'accueil de l'application
```
La page d’accueil de l’application (figure 3) se veut très simple, car ce n’est pas là que l’utilisateur va passer la plupart de son temps. Elle ne cherche qu’à rediriger vers les pages d’inscription ou de connexion qui permettront par la suite d’accéder aux différents cours. 

## Page d'exercices

```{figure} images/exercice_tm.png
---
width: 70%
---
Page contenant les exercices de l'application
```
Comme on peut le remarquer, les pages d’exercices sont séparées des pages de théorie. En effet, ceci permet que le travail de réflexion vis-à-vis d’une question soit plus efficace: l’étudiant n’est pas tenté d’aller chercher la réponse dans la même page. Il pourra se concentrer davantage sur la question et produira l’effort d’y répondre sans aide, comme dans le cadre d’une évaluation. Néanmoins, si l’étudiant ne trouve pas la réponse, il pourra retourner sur la page pouvant l’aider en cliquant sur le bouton “revenir à la théorie”. 

## Page de sélection du cours

```{figure} images/listcourses.png
---
width: 70%
---
Page permettant de choisir son cours
```
Il est possible d'observer en figure 5 la page de sélection des différents cours. C'est ici que l'utilisateur est redirigé une fois qu'il est connecté à l'application. L'utilisation de cartes permet de bien distinguer les différents cours et leur alignement permet un équilibre dans la page. Le nom des cours est mis en valeur, ce qui permet à l'utilisateur de rapidement distinguer le cours vers lequel il souhaite se diriger.

## Page d'inscription

```{figure} images/signup.png
---
width: 70%
---
Page pour s'inscrire à l'application
```
En figure 6 se trouve la page d’inscription. Cette dernière est un formulaire demandant plusieurs informations à l’utilisateur comme son type de classe, ce qui le redirigera facilement vers les cours de la classe concernée. L’arrière-plan de cette page change des autres, car il est à moitié bleu. Cependant, au cas où cet arrière-plan gênerait, il est possible d'avoir un arrière-plan entièrement gris en changeant le layout de la page. Ceci mettra une note d’originalité et rendra l’application moins monotone. De plus, ce bleu fait référence à la bande de la même couleur contenant le titre des pages de cours. 

## Page de résumé

```{figure} images/resume_tm.png
---
width: 70%
---
Page contenant un résumé du chapitre étudié
```
Enfin, je vous présente en figure 7 la page de résumé. L’application d’origine ne contenant que peu de résumé, il m’a semblé important d’ajouter une page de ce type. Ceci permet, comme on peut s’en douter, de réunir les aspects principaux du chapitre étudié sur quelques lignes. Cela peut agir comme repère lors des révisions, car on comprend ce qui est attendu lors de l’examen qui évaluera cette matière. 

## Remarques générales
Pour finir, il est possible de naviguer à travers les composants grâce au router vue. Ce dernier permet de changer l'URL de la page consultée pour atteindre un autre composant. De plus, pour faciliter la création de nouvelle page, l'application possède différents layouts. Le layout est le modèle d'un type de page. Il ne reste plus qu'à ajouter le contenu et choisir son layout et nous obtiendrons la page souhaitée. 

## Conclusion
Cette nouvelle version de la plateforme de cours se veut moderne et simple. Le but n’est pas de perturber l’étudiant lors de son apprentissage, mais plutôt de lui apporter des outils qui peuvent s’avérer utiles lors de l’étude d’un chapitre ou de la préparation d’un examen. 
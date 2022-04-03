# Le design
## Introduction
Le design constitue un élément primordial lors de la construction d’une application web. Il représente son identité, donne une image moderne à cette dernière, tout en pouvant faciliter la compréhension du contenu. Le design donne à l'utilisateur la première impression d'une page. Il est primordial qu’elle soit travaillée. Cependant, trouver le design optimal n’est pas aussi aisé qu’il n'y paraît. De nombreux critères sont pris en compte pour élaborer une page harmonieuse et efficace. Ainsi, de nombreuses applications proposant un contenu intéressant n’ont pas rencontré le succès escompté notamment à cause d'un design négligé. Par conséquent, le but de ce chapitre est d’aborder les points principaux à développer lorsqu’il s’agit de produire un design attractif. A l'évidence, il est primordial d’effectuer un travail conséquent avant même de commencer à coder l'application pour affiner le rendu souhaité. La finalisation du programme est presque toujours question de détails. 
## Réfléchir à son design
Dans un premier temps, il est nécessaire de réfléchir à l'effet que le site internet devra dégager.  

Rappelons que mon travail de maturité consiste à moderniser une plateforme d’apprentissage. Le design devra donc permettre, en premier lieu, un apprentissage de qualité et agréable. Il incitera peut-être l’utilisateur à poursuivre son travail sur cette plateforme. 

Pour déterminer vers quel type de design se diriger, il n’est pas inutile de naviguer à travers les différentes applications web proposant des services similaires à la page. L'objectif: dégager les éléments qui fonctionnent et ceux qui, en revanche, ne sont pas optimaux. Cette expérience permet de se mettre à la place de l’utilisateur et de comprendre ce qui procurera les meilleures chances de réussite. Dans cet exemple, j’ai remarqué que les nombreux sites d’apprentissage proposaient tous un design minimaliste et simple. Juste: l’utilisateur cherche à assimiler son cours sans devoir être bombardé par de nombreux éléments et couleurs. Le but demeure de mettre en valeur ce dont il a besoin pour étudier. Rien de plus. Ce n'est pas un hasard si ces sites n’ont que très peu de couleurs différentes. Pour naviguer dans les chapitres d'un cours, les sites étudiés proposent une barre verticale à gauche que l’on peut enlever si l’on souhaite se focaliser sur le contenu.
```{figure} images/openclassroom_1.png
---
width: 60%
---
Site web oppenclassroom.com
```
```{figure} images/openclassroom_2.png
---
width: 60%
---
Site web oppenclassroom.com
```
```{figure} images/khan_1.png
---
width: 60%
---
Site web khanacademy.org
```
Après s’être inspiré et avoir laissé germer quelques idées, il est temps de déterminer le design de l'application en dessinant quelques schémas. Ces esquisses permettent de distinguer plus facilement ce qu’il y a à améliorer dans le projet et de bénéficier d'une idée du rendu final. Fonctionner ainsi permet un gain de temps conséquent, car on ne doute plus de l'idée et cela nous évite de partir dans une mauvaise direction et de devoir tout recommencer par la suite. Le but étant d’obtenir une structure générale, le design n’est pas définitif et pourra aisément être modifié par la suite. Une idée générale du produit limite aussi le risque de mauvaises surprises lors du codage. 


```{figure} images/design_vf.png
---
width: 50%
---
Croquis pour la page d'accueil de l'application
```
```{figure} images/design_2.png
---
width: 60%
---
Croquis pour une page de cours de l'application
```
## Pendant le codage
Abordons la partie du codage. Elle représente la concrétisation de l'idée générale. Dans le cas de mon projet, il m'a semblé intéressant d'y ajouter une barre latérale, sous forme d'un menu ouvert sur la gauche de la fenêtre permettant une navigation plus aisée. Même si la ligne est donnée, les réflexions effectuées auparavant ne sont pas définitives et peuvent subir des évolutions pour améliorer le site. 
```{figure} images/sidebar_screen.png
---
width: 70%
---
Barre latérale utilisée dans la page de cours
```

## Après le codage
 Après avoir terminé de coder les éléments principaux de la page, une attention particulière sera portée aux détails qui rendront la page plus professionnelle et agréable à consulter. Il est notamment important de distinguer les éléments les uns des autres. Pour ce faire, les développeurs n’hésitent pas à ajouter des marges intérieures, appelées "padding" (cf. Figure 8) et des marges extérieures, nommées "margin" (cf. Figure 8) aux différents éléments de leur page. Procéder ainsi permet de mettre en évidence le composant, ainsi que de séparer et ainsi de distinguer les éléments les uns des autres. La page gagnera en clarté.
```{figure} images/padding_marg.png
---
width: 55%
---
Illustration des paddings et des margins d'un élément
```
Dans un souci d'harmonisation, il est également important d’avoir un alignement cohérent sur l’ensemble de la page. Un alignement strict donne un aspect professionnel et permet de bien distinguer les éléments les uns des autres.
```{figure} images/alignement_f.png
---
width: 50%
---
Alignement à améliorer
```
Deux autres éléments, bien souvent sous-estimés, sont les contrastes de couleurs et le choix de la police. En effet, les éléments doivent se distinguer les uns des autres par la différence de leur couleur. Il faut cependant porter une attention particulière sur le fait que la page ne doit pas contenir trop de couleurs différentes pour éviter de perturber l’utilisateur. Le choix de la police semble aussi primordial, car il donne en partie l’identité de la page. Un site destiné aux enfants utilisera une police plus fantaisiste, alors qu’un site plus professionel, tel un site de vêtements de luxe, se dotera d’une police plus sérieuse. Il est préférable, comme pour le choix des couleurs, de n'utiliser qu'une, voire deux polices différentes. 
```{figure} images/contraste.png
---
width: 50%
---
Contraste entre les couleurs rouge et noir
```
Les détails peuvent apporter énormément à l'application. Ils permettent notamment de rendre le travail plus agréable à consulter. Bien évidemment, il ne faut pas s’attarder uniquement sur les points abordés dans cette partie, mais ces derniers demeurent essentiels. Le programmeur doit scruter attentivement les éléments de sa page, mais aussi l’harmonie de cette dernière afin de produire le travail le plus professionnel possible. 
## Conclusion
Afin de produire un design efficace, le développeur doit pouvoir examiner son travail dans les moindres détails mais aussi, et surtout, avec une vision d’ensemble. Cela nécessite un travail important avant même le début du codage afin de dicter sa ligne directrice. Cette vision pourra et sera probablement modifiée pendant et même après avoir terminé son code. Développer son projet sur une période de temps importante permet d’imaginer davantage de nouvelles idées à ajouter à son application. Je ne pourrais conclure ce chapitre sans ajouter la dimension forcément subjective d'une telle démarche. Le design est aussi propre à chacun. 
 
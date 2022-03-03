# Annexes
## Code d'une page de cours

```{admonition} Remarque
---
class: attention
---
Suite à des problèmes rencontrés avec la plateforme repl qui m'ont empêché d'avancer, cette version du code du composant CoursePage date du 3 mars 2022 et n'est donc pas la version finale.
```


```{code-block} html
---
linenos: true
---
<template>
  <!-- création du head -->
  <head>
    <title>Page de cours</title>
    <meta charset="UTF-8">
    <meta name="description" content="Bienvenue sur la nouvelle plateforme d'apprentissage du cours d'informatique.">
    <meta name="keywords" content="informatique, apprentissage, plateforme, collège du sud">
  </head>
  <body>
    <!-- div englobant l'intégralité de la page -->
    <div class="page" :class="{'page-shift': visibleLeft, 'page-normal': !visibleLeft}" style="height: 100%;">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <div class="menubar-css">
      <!-- création du menu-haut -->
      <Menubar :model="item" style="margin-top: -65px; width: 100.7%; position: fixed; z-index: 4; margin-left : 1.5%; margin-right: -10%; max-height: 65px;">
        <!-- éléments à gauche du menu -->
        <template #start> 
          <Button>Retour à la page d'accueil</Button>
          <Button icon="pi pi-arrow-right" @click="visibleLeft = true" class="p-mr-2"/>
        </template>
        <!-- élément à doite du menu -->
        <template #end>
          <span class="p-input-icon-left">
              <i class="pi pi-search" />
              <InputText type="text" v-model="value1" placeholder="Search" />
          </span>
          <Button icon="pi pi-user" class="p-button-rounded p-button-info" />
        </template>
      </Menubar>
    </div>
    <div class="toutepage">

    <!-- fin du menu-haut -->
    <!-- intégration du contenu de notre page -->
    <div class="content" style ="width: 100%;"> 
      <h1>2.1 Le monde des robots</h1>
      <!-- appel de la barre latérale -->
      <Sidebar v-model:visible="visibleLeft" :modal="false" :autoZIndex="true">
        <p>Naviguer dans ce chapitre</p>
        <PanelMenu :model="items" />
      </Sidebar>
      <div class="contenu">  
                <!-- ajout du contenu textuel de notre cour -->
      <div class="text" style="margin-top: 0%; z-index: 1; float: none; width: 80%; height : 60%; font-size: 20px; text-align : left; margin-right : auto; margin-left: auto; font-size: 25px;">                 
                        <h3>2.1.1. Introduction </h3>
  Les robots sont des appareils mécaniques contrôlés par ordinateur, capables d’effectuer des tâches automatisées de manière autonome. Cela fait bien longtemps qu’ils jouent un rôle important dans l’industrie, dans la technologie, dans la médecine, dans la recherche et dans les sciences, à savoir dans pratiquement tous les domaines de l’activités humaines. Alors que les premiers robots étaient conçus pour assister les humains dans les tâches monotones et pénibles physiquement, les robots de nouvelle génération sont capables de collecter des données sur leur environnement à l’aide de capteurs, de prendre des décisions pertinentes ou d’adapter leur comportement en fonction de leur environnement (auto-apprentissage). On parle alors de robots auto-apprenants (self-learning robot en anglais).

  Il existe différents types de robots : les robots industriels fixes, les robots mobiles ou les robots humanoïdes. Mais il y a une chose que tous les robots ont en commun : ils doivent tous être programmés. Il faut des humains pour décrire de manière très précise la tâche qu’un robot doit effectuer à l’aide d’une suite d’instructions, à savoir d’un programme informatique.
  <br>    
                </div>
        <!-- ajout de l'image du robot -->
        <img src="../assets/nao.jpg" style="height : 26rem; width: 20rem; margin-right: 0%; margin-top: 2%;"/>
      </div>
    </div>
    <!-- création d'une div englobant les éléments de fin de page -->
    <div class="findepage" style="margin-top: 0px; float: none">
      <Button class="p-button-raised" style="position: center; min-height: 100%;">Mark as complished</Button>
      <Button class="p-button-raised" id="exercice" style="position: center; min-height: 100%;">Vers les exercices</Button>
      <ProgressBar mode="dynamic" value="60" style="width: 50%; margin-left: auto; margin-right: auto; margin-top: 5%;">
      Percent Complete: {{value}}%
      </ProgressBar>
    </div>
    </div>
  </div>
  </body>
</template>

<script>

export default {

  data() {
    return {
      visibleLeft: true,
      items: [
                {
                    label: 'Chapitre 1',
                    items: [
                      {
                          label: 'Chapitre 1.1',
                          items: [
                            {
                                label: 'Chapitre 1.1.1',
                            },
                            {
                                label: 'Chapitre 1.1.2',
                            }
                          ]
                      },
                      {
                          label: 'Chapitre 1.2',
                      },
                      {
                          label: 'Chapitre 1.3',
                      }
                    ]
                },
              ]
		}
	}
}

</script>

<style scoped>
  export default {
}
<style lang="scss" scoped>
::v-deep(.p-scrollpanel) {
    p {
        padding: .5rem;
        line-height: 1.5;
        margin: 0;
    }

    &.custombar1 {
        .p-scrollpanel-wrapper {
            border-right: 9px solid var(--surface-b);
        }

        .p-scrollpanel-bar {
            background-color: var(--primary-color);
            &:hover {
                background-color: #007ad9;
            }
        }
    }

    &.custombar2 {
        .p-scrollpanel-wrapper {
            border-right: 9px solid var(--surface-b);
            border-bottom: 9px solid var(--surface-b);
        }

        .p-scrollpanel-bar {
            background-color: var(--surface-d);
            border-radius: 0;
            opacity: 0;
        }
    }  
}
body{
  height: 105%;
  margin-left: -2%;
  margin-right: -2%;
  margin-top: 0%;
  margin-bottom: -5%;
  padding-bottom: 10%;
  background: linear-gradient(to bottom left, #E1E1E1 50%, #F1F1F1 50%);
}
.toutepage{
  margin-left: 0%;
  margin-right: 0%;
}
/* css du bouton des exercices*/
#exercice{
  background-color: #ff8000;
  border-color: #ff8000;
}
/* css du bouton mark as completed*/
.p-button-raised{
  background-color: limegreen;
  border-color: limegreen;
  margin-bottom: 10px;
  color : white;
}
/* bouton du menu-haut*/
Button{
  margin: 5px;
  background-color : #F9F9F9;
  border-color: #F9F9F9;
  color : grey;
}
navbuttton{
  background-color: #F9F9F9;
  color : grey;
}
.p-button-rounded{
  background-color : #F9F9F9;
}
h1{
  font-size: 40px;
  background-color: #5c7fd4;
  padding-top: 2rem;
  padding-bottom: 2rem;
  color: white;
  width: 110%;
  margin-left: -4%;
  margin-right: auto;
  max-width: 104%;
}
/*css permettant l'adaptation avec la sidebar */
.page-normal {
    margin-left: -10px;
    margin-right: -15px;
    transition-duration: 0.35s;

}
.page-shift {
    margin-left: 19rem;
    transition-duration: 0.35s;
    margin-right: -15px;
}
a {
  color : grey;
}

</style>

``` 
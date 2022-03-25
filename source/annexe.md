# Annexes
## Code du composant ListCourses

```{admonition} Remarque
---
class: attention
---
Suite à des problèmes rencontrés avec la plateforme repl qui m'ont empêché d'avancer, cette version du code du composant ListCourses date du 3 mars 2022 et n'est donc pas la version finale.
```


```{code-block} vue
---
linenos: true
---
<template>
  <html>
    <head>
      <title>Choisissez votre cours</title>
      <meta charset="UTF-8">
      <meta name="description" content="Bienvenue sur la nouvelle plateforme d'apprentissage du cours d'informatique.">
      <meta name="keywords" content="informatique, apprentissage, plateforme, collège du sud">
    </head>
    <body>
      <div class="menubar-css">
        <!-- création du menu-haut -->
        <Menubar :model="item" style="margin-top: -65px; width: 103%; position: fixed; z-index: 4; margin-left : -1%; margin-right: -5%">
          <!-- éléments à gauche du menu -->
          <template #start> 
            <Button>Retour à la page d'accueil</Button>
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
        <div class="content" style ="margin-top : 50px; width: 105%;">
          <h1>Choisissez votre cours</h1>
          <div class="toutecarte"> 
            <Card class="carte">
              <template #header>
              </template>
              <template #title>
                  Cours de programmation
              </template>
              <template #content>
                  Lorem
              </template>
              <template #footer>
                <Button class="Bouton">Aller au cours</Button>
              </template>
            </Card>
            <Card class="carte">
              <template #header>
              </template>
              <template #title>
                  Cours de Web design
              </template>
              <template #content>
                  Lorem
              </template>
              <template #footer>
                <Button class="Bouton">Aller au cours</Button>
              </template>
            </Card>
            <Card class="carte">
              <template #header>
              </template>
              <template #title>
                  Cours de Robotique
              </template>
              <template #content>
                  Lorem
              </template>
              <template #footer>
                <Button class="Bouton">Aller au cours</Button>
              </template>
            </Card>
            <Card class="carte">
              <template #header>
              </template>
              <template #title>
                  L'internet des objets
              </template>
              <template #content>
                  Lorem
              </template>
              <template #footer>
                <Button class="Bouton">Aller au cours</Button>
              </template>
            </Card>
            <Card class="carte">
              <template #header>
              </template>
              <template #title>
                  Les réseaux informatiques
              </template>
              <template #content>
                  Lorem
              </template>
              <template #footer>
                <Button class="Bouton">Aller au cours</Button>
              </template>
            </Card>
            <Card class="carte">
              <template #header>
              </template>
              <template #title>
                  Cours "Listes avancées"
              </template>
              <template #content>
                  Lorem
              </template>
              <template #footer>
                <Button class="Bouton">Aller au cours</Button>
              </template>
            </Card>
          </div>
        </div>
      </div>
    </body>
  </html>
</template>

<!-- éléments du PanelMenu -->
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
p {
  padding: .5rem;
  line-height: 1.5;
  margin: 0;
}
/* bouton de login*/
.loginbutton{
  margin: 5px;
  background-color : #5c7fd4;
  border-color: #5c7fd4;
  color : white;
}
body{
  width: 102%;
  margin-left: -1%;
  margin-right: -1%;
  margin-top: 0%;
  height: 105%;
  margin-bottom: -5%;
  padding-bottom: 10%;
  background: linear-gradient(to bottom left, #E1E1E1 50%, #F1F1F1 50%);
}
/* Autres boutons de la page*/
Button{
  margin: 5px;
  background-color : #F9F9F9;
  border-color: #F9F9F9;
  color : grey;
}
.Bouton{
  background-color: #5c7fd4;
  border-color: #5c7fd4;
  color: white;
}
.carte{
  margin-top: 2%;
  max-width: 25rem;
  max-height: 10%;
  display: inline-block;
  margin-left: 1%;
  margin-right: 1%;
  animation: fadein 1s;    
}
@keyframes fadein {
    from {
        opacity:0;
    }
    to {
        opacity:1;
    }
}
.toutecarte{
  margin-right: auto;
  margin-left: -5%;
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
p-panelmenu{
  width: 60%;
  margin-top: 100px;
}
</style>
``` 
## Déclaration sur l'honneur
```{figure} images/tm_decla.jpg
---
width: 100%
---
```
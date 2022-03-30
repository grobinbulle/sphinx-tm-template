class TMConfig:

    title = u"Modernisation de la plateforme de cours 21Learning avec Vue 3"
    first_name = 'Robin'
    last_name = 'Gachet'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'Avril'
    seminary_title = u'Développement d’outils ou de matériel d’enseignement de l’informatique'
    tutor = u"Robin Gachet"
    release = "Version finale"
    repository_url = "https://github.com/{your-docs-url}"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()
# TD Translator WebApp
The translator is available at [tdtranslator.vercel.app](https://tdtranslator.vercel.app/)\
This project was developed by the English-only group of [Tomorrowdevs](https://www.tomorrowdevs.com/)
in live coding on Monday nights.

### Core Translation Feature
Translations are generated through [*googletrans*](https://pypi.org/project/googletrans/) Python library. 

### Launch with Docker
1) `docker build -t {your_image_ame} .`
2) `docker run -it -p 8001:8001 {your_image_name}`

### Launch with Pytnon:
Two steps:\
`pip install -r requirements.txt` (only once)\
`python manage.py runserver`

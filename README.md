# Mineral Catalog in Django
Miniral Catalog - Django

Website that displays information about various minerals (AKA rocks). The home page of the site contains a list of all of the minerals in a database. Clicking on a mineral’s name opens a page that displays information about the mineral.

Each mineral can have the following attributes. Some minerals will not have all of these attributes.

* name
* image filename
* image caption
* category
* formula
* strunz classification
* color
* crystal system
* unit cell
* crystal symmetry
* cleavage
* mohs scale hardness
* luster
* streak
* diaphaneity
* optical properties
* refractive index
* vcrystal habit
* specific gravity

## Installation

pip3 install -r requirements.txt

python manage.py migrate

### JSON to SQL (Data)
python manage.py json-to-sql

### TESTS
python manage.py test minerals.core.tests


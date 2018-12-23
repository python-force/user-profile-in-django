from django.core.management.base import BaseCommand, CommandError
import json
import os
from pathlib import Path, PurePath
from django.utils.text import slugify

from minerals.core.models import Mineral, Test


class Command(BaseCommand):
    help = 'Json to SQLite'

    def handle(self, *args, **options):
        """JSON file to SQLite"""

        p = Path(__file__).parents[4]
        p = PurePath(p, 'assets/data/minerals.json')
        print(p)

        mineral_bulk = []

        with open(p, 'r') as mineral_list:
            minerals = json.load(mineral_list)
            for mineral in minerals:
                image_filename = "/static/data/images/" + mineral['name'] + ".jpg"
                name = mineral['name']
                # slug = slugify(name)
                # print(slug)

                if 'image caption' in mineral:
                    image_caption = mineral['image caption']
                else:
                    image_caption=None

                if 'category' in mineral:
                    category = mineral['category']
                else:
                    category=None

                if 'formula' in mineral:
                    formula = mineral['formula']
                else:
                    formula=None

                if 'strunz classification' in mineral:
                    strunz_classification = mineral['strunz classification']
                else:
                    strunz_classification=None

                if 'color' in mineral:
                    color = mineral['color']
                else:
                    color=None

                if 'crystal system' in mineral:
                    crystal_system = mineral['crystal system']
                else:
                    crystal_system=None

                if 'unit cell' in mineral:
                    unit_cell = mineral['unit cell']
                else:
                    unit_cell=None

                if 'crystal symmetry' in mineral:
                    crystal_symmetry = mineral['crystal symmetry']
                else:
                    crystal_symmetry=None

                if 'cleavage' in mineral:
                    cleavage = mineral['cleavage']
                else:
                    cleavage=None

                if 'mohs scale hardness' in mineral:
                    mohs_scale_hardness = mineral['mohs scale hardness']
                else:
                    mohs_scale_hardness=None

                if 'luster' in mineral:
                    luster = mineral['luster']
                else:
                    luster=None

                if 'streak' in mineral:
                    streak = mineral['streak']
                else:
                    streak=None

                if 'diaphaneity' in mineral:
                    diaphaneity = mineral['diaphaneity']
                else:
                    diaphaneity=None

                if 'optical properties' in mineral:
                    optical_properties = mineral['optical properties']
                else:
                    optical_properties=None

                if 'refractive index' in mineral:
                    refractive_index = mineral['refractive index']
                else:
                    refractive_index=None

                if 'crystal habit'in mineral:
                    crystal_habit = mineral['crystal habit']
                else:
                    crystal_habit=None

                if 'specific gravity'in mineral:
                    specific_gravity = mineral['specific gravity']
                else:
                    specific_gravity=None

                if 'group' in mineral:
                    group = mineral['group']
                else:
                    group=None
                    
                mineral_bulk.append(
                                    Mineral(name=name,
                                            image_filename=image_filename,
                                            image_caption=image_caption,
                                            category=category,
                                            formula=formula,
                                            strunz_classification=strunz_classification,
                                            color=color,
                                            crystal_system=crystal_system,
                                            unit_cell=unit_cell,
                                            crystal_symmetry=crystal_symmetry,
                                            cleavage=cleavage,
                                            mohs_scale_hardness=mohs_scale_hardness,
                                            luster=luster,
                                            streak=streak,
                                            diaphaneity=diaphaneity,
                                            optical_properties=optical_properties,
                                            refractive_index=refractive_index,
                                            crystal_habit=crystal_habit,
                                            specific_gravity=specific_gravity,
                                            group=group)
                )

        print(mineral_bulk)

        Mineral.objects.bulk_create(mineral_bulk)

        print ("SQL records created. Yay.")

        """Notes"""

        """
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        print(BASE_DIR)

        # uri_videos = Video.objects.all().filter(online=True)

        p = ''
        p = PurePath(p, 'assets/data/minerals.json')
        print(p)

        # p = os.getcwd()
        # p = p + '/config/assets/data/test.txt'
        
        filename = p
        file = open(filename, "r")
        for line in file:
            print (line)
        """
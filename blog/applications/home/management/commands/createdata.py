from random import randint
from django.core.management import BaseCommand

# models
from applications.entrada.models import Entry, Tag
# from applications.home.models import Suscribers

# apps de terceros
from faker import Faker

TAGS = (
    "Blogging",
    "Freelancing",
    "How to Succeed",
    "Income Reports",
    "Internet Marketing",
    "Miscellaneous",
    "Quitting Your Job",
    "Search Engine",
    "Social Media"
)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Tags
        # for tag in TAGS:
        #     Tag.objects.create(
        #         name = tag
        #     )
        
        # Category
        # Faker.seed(0)
        # for _ in range(20):
        #     Category.objects.create(
        #         short_name = fake.slug(),
        #         name=fake.catch_phrase()
        #     )
        
        # sucriptores
        # for _ in range(20):
        #     Suscribers.objects.create(
        #         email=fake.ascii_email()
        #     )
        
        # entradas
        # Faker.seed(0)
        # for _ in range(50):
        #     c = randint(1,20)
                        
        #     entry = Entry(
        #         user_id = 1,
        #         category_id=c,
        #         title=fake.catch_phrase(),
        #         resume=fake.company(),
        #         content=fake.paragraph(nb_sentences=5, variable_nb_sentences=False),
        #         image=fake.image_url(),
        #         public= randint(0,1),
        #         portada= randint(0,1),
        #         in_home= randint(0,1),
        #         slug=fake.slug()
        #     )
        #     entry.save()
            
        #     for _ in range(randint(1,4)):
        #         id = randint(1,9)
        #         entry.tag.add(Tag.objects.get(pk=id))
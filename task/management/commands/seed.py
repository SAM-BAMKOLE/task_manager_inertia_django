from django.core.management.base import BaseCommand
from task.models import Task
from authentication.models import User
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = "Seed the database with sample tasks"

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        title = ['Meetings', 'Shopping', 'Coding', "Workout", "Study Session"]
        description = [
            'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem, laudantium. Labore, exercitationem omnis. Ut alias beatae sapiente.',
            'Ipsum dolor sit amet consectetur adipisicing elit. Vero itaque repudiandae fugiat repellendus dolore? Veritatis non accusantium tempora blanditiis consequuntur vero cupiditate quos.',
            'Dolor sit, amet consectetur adipisicing elit. Obcaecati, suscipit ullam lorem ipsum?',
            'Sit amet consectetur adipisicing elit. Rem necessitatibus accusamus qui nesciunt minus, ipsum dolor!',
            'Amet consectetur adipisicing elit. Aliquam quisquam corrupti delectus deserunt? Lorem ipsum dolor sit',
            'Consectetur adipisicing elit. Fugiat, Lorem ipsum dolor sit amet!'
        ]

        for i in range(50):
            Task.objects.create(
                title=f"{random.choice(title)} #{i+1}",
                description=f"Sample task - {random.choice(description)}",
                owner=random.choice(users),
                due_date=date.today() + timedelta(days=int(random.choice([1,2,3,4,5,6,7,8,9,10])))
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded tasks!'))
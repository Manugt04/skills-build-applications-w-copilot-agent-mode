from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass')

        # Create activities
        Activity.objects.create(name='Run', user='ironman', team='Marvel')
        Activity.objects.create(name='Swim', user='captain', team='Marvel')
        Activity.objects.create(name='Fly', user='superman', team='DC')
        Activity.objects.create(name='Drive', user='batman', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=200)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups', user='ironman')
        Workout.objects.create(name='Situps', description='Do 100 situps', user='captain')
        Workout.objects.create(name='Squats', description='Do 80 squats', user='batman')
        Workout.objects.create(name='Bench Press', description='Bench press 100kg', user='superman')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))

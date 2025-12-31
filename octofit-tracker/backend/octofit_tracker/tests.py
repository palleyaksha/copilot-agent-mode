from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout')
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=10, date='2025-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=50)
        self.workout.suggested_for.set([self.user])

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_activity_str(self):
        self.assertIn('Test Activity', str(self.activity))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

    def test_leaderboard_str(self):
        self.assertIn('Leaderboard for', str(self.leaderboard))

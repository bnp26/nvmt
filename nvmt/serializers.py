'''
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','first_name', 'last_name', 'active', 'tester', 'admin')

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('id', 'x', 'y', 'is_goal', 'created_at', 'clicked_at', 'click_time')

class CardSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Card
        fields = ('id', 'start', 'finish', 'targets')

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        card = Card.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(card=card, **target_data)
        return card

class TrialSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)

    class Meta:
        model = Trial
        fields = ('id', 'trial_num', 'cards')

    def create(self, validated_data):
        cards_data = validated_data.pop('cards')
        trial = Trial.objects.create(**validated_data)
        for card_data in cards_data:
            CardSerializer.create(trial=trial, **cards_data)
        return trial

class TestSerializer(serializers.ModelSerializer):
    trials = TrialSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'created', 'trials')

    def create(self, validated_data):
        trials_data = validated_data.pop('trials')
        test = Test.objects.create(**validated_data)
        for trial_data in trials_data:
            TrialSerializer.create(test=test, **track_data)
        return test

class SubjectSerializer(serializers.ModelSerializer):
    test = TestSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())

    class Meta:
        model = Subject
        fields = ('id', 'age', 'date_of_birth', 'gender', 'education', 'user')

    def create(self, validated_data):
        subject = Subject.objects.create(**validated_data)
        return subject
'''

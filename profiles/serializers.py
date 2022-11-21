from rest_framework import serializers
from profiles import models


class UserProfileSerializer(serializers.ModelSerializer):
    '''serializes the userprofile model'''
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name',
                  'last_name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        '''creates and return a new user'''
        password = validated_data.get('password')
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedModel
        fields = ('id', 'status_text', 'user_profile', 'created_on')

        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }

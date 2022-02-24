from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Document,Transaction,User

def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')

# class GameRecord(serializers.ModelSerializer):
#     score = IntegerField(validators=[required])

#     class Meta:
#         model = Game
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('__all__')

class TranscSerializer(serializers.ModelSerializer):
	documents=DocSerializer(read_only=True,many=True)
	user=UserSerializer(read_only=True)
	description = serializers.CharField(validators=[required])
	class Meta:
		model = Transaction
		fields = ('description','id','user','documents')
		extra_kwargs = {
            'description': {'required': True,'validators':[required]}
        }

        # exclude=['api_id']
class TranscCreateSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[required])
    class Meta:
        model = Transaction
        fields = ('description','id')
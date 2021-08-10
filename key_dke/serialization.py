from rest_framework import serializers

class first (serializers.ModelSerializer):
    class Meta ():
        model= 'ff'
        fields = '__all__'

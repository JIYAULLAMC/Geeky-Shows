from rest_framework import serializers
from django import forms

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=120)
    roll=serializers.IntegerField()

class StudentForm(forms.Form):
    name=forms.CharField(max_length=120)
    roll=forms.IntegerField()
from rest_framework import serializers
from api.models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanyNameSerializer()

    class Meta:
        model = Employee
        fields = '__all__'
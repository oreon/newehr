
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers, viewsets, routers
from .models import  *
from rest_framework import permissions, generics, request
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import filters, pagination

from rest_framework.decorators import action
from hnet.api import * 


class BasePagination(pagination.PageNumberPagination):
    page_size = 40

# class QuoteSerializer(serializers.ModelSerializer):

#     link = serializers.CharField(source='get_link', read_only=True)
#     permission_classes = (IsAuthenticated,)

#     class Meta:
#         model = Post
#         exclude = ('users_like', 'created', 'updated')
#         read_only_fields = ('publish',)



class PatientSerializer(serializers.ModelSerializer):
    

    #permission_classes = (IsAuthenticated,)
    class Meta:
        model = Patient
        fields = '__all__'


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('firstname')
    serializer_class = PatientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^firstname', '^lastname')
    pagination_class = BasePagination

    @action(methods=['get'], detail= True)
    def notes(self, request, pk=None):
        patient = self.get_object()
        qs = patient.notes.all()
        
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = NoteSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = NoteSerializer(qs, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail= True)
    def scripts(self, request, pk=None):
        patient = self.get_object()
        qs = patient.scripts.all()
        
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = ScriptSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ScriptSerializer(qs, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail= True)
    def measurements(self, request, pk=None):
        patient = self.get_object()
        qs = patient.measurements.all()

        serializer = MeasurementSerializer(qs, many=True)
        return Response(serializer.data)



class UserSerializer(serializers.HyperlinkedModelSerializer):

    #permission_classes = (IsAuthenticated,)
    class Meta:
        model = User
        fields = '__all__'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
class NoteSerializer(serializers.ModelSerializer):
    #author = UserSerializer(context={'request': request})
    #permission_classes = (IsAuthenticated,)
    # patient = serializers.StringRelatedField(
    #     read_only=False
    # )

    class Meta:
        model = Note
        fields = '__all__'


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('description', )
    pagination_class = BasePagination

class ScriptItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScriptItem
        exclude = ('script', )

class ScriptSerializer(serializers.ModelSerializer):
    scriptItems = ScriptItemSerializer(many=True)

    def create(self, validated_data):
        scriptItems = validated_data.pop('scriptItems')
        script = Script.objects.create(**validated_data)
        for item in scriptItems:
            ScriptItem.objects.create(script=script, **item)
        return script

    class Meta:
        model = Script
        fields = '__all__'    

class ScriptViewSet(viewsets.ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer




router = routers.SimpleRouter(trailing_slash=False)
router.register(r'patients', PatientViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'users', UserViewSet)
router.register(r'scripts', ScriptViewSet)

    
    
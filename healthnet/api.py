
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers, viewsets, routers
from .models import  *
from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import filters, pagination

from rest_framework.decorators import action



class BasePagination(pagination.PageNumberPagination):
    page_size = 4

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
    queryset = Patient.objects.all()
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

class NoteSerializer(serializers.ModelSerializer):

    #permission_classes = (IsAuthenticated,)
    class Meta:
        model = Note
        fields = '__all__'



class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('description', )
    pagination_class = BasePagination

class UserSerializer(serializers.HyperlinkedModelSerializer):

    #permission_classes = (IsAuthenticated,)
    class Meta:
        model = User
        fields = '__all__'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = NoteSerializer

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'patients', PatientViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'users', UserViewSet)

    
    
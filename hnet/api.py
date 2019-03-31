
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers, viewsets, routers
from .models import  *
from rest_framework import permissions, generics, request
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import filters, pagination

from rest_framework.decorators import action



class BasePagination(pagination.PageNumberPagination):
    page_size = 20

# class QuoteSerializer(serializers.ModelSerializer):

#     link = serializers.CharField(source='get_link', read_only=True)
#     permission_classes = (IsAuthenticated,)

#     class Meta:
#         model = Post
#         exclude = ('users_like', 'created', 'updated')
#         read_only_fields = ('publish',)



class MeasurementTypeSerializer(serializers.ModelSerializer):
    
    #permission_classes = (IsAuthenticated,)
    class Meta:
        model = MeasurementType
        fields = '__all__'


class MeasurementTypeViewSet(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementTypeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', )
    pagination_class = BasePagination

class MeasurementSerializer(serializers.ModelSerializer):
    
    #permission_classes = (IsAuthenticated,)
    class Meta:
        model = Measurement
        fields = '__all__'


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^msmtType__name', )
    pagination_class = BasePagination

   
# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


msmt_router = routers.SimpleRouter(trailing_slash=False)
msmt_router.register(r'measurementTypes', MeasurementTypeViewSet)
msmt_router.register(r'measurements', MeasurementViewSet)
# router.register(r'notes', NoteViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'scripts', ScriptViewSet)

    
    
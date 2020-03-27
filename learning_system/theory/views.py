from rest_framework import viewsets
from dry_rest_permissions.generics import DRYPermissions

from learning_system.theory.models import TheoryCategory, TheoryPost
from learning_system.theory.serializers import TheoryCategoryCreateSerializer, \
    TheoryPostCreateSerializer, \
    TheoryCategorySerializer, \
    TheoryPostSerializer


class TheoryCategoryView(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions, )    
    serializer_class = TheoryCategoryCreateSerializer
    queryset = TheoryCategory.objects.all()


class TheoryPostView(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions, )    
    serializer_class = TheoryPostCreateSerializer
    queryset = TheoryPost.objects.all()

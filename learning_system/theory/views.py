from rest_framework import generics

from learning_system.theory.models import TheoryCategory, TheoryPost
from learning_system.theory.serializers import TheoryCategoryCreateSerializer, \
    TheoryPostCreateSerializer, \
    TheoryCategorySerializer, \
    TheoryPostSerializer


class TheoryCategoryCreateView(generics.CreateAPIView):
    serializer_class = TheoryCategoryCreateSerializer


class TheoryCategoryView(generics.ListAPIView):
    serializer_class = TheoryCategorySerializer
    queryset = TheoryCategory.objects


class TheoryPostCreateView(generics.CreateAPIView):
    serializer_class = TheoryPostCreateSerializer


class TheoryPostView(generics.ListAPIView):
    serializer_class = TheoryPostSerializer
    queryset = TheoryPost.objects

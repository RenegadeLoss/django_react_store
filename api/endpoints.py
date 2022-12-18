from django.shortcuts import render
from catalog.models import Clothings, TypeOfClothes
from .api_serealizers import ClothingsSerializer, TypeOfClothesSerializer
from rest_framework import generics

# Create your views here.


class GetItemsListView(generics.ListAPIView):
    serializer_class = ClothingsSerializer
    queryset = Clothings.objects.all()


class GetFilteredList(generics.ListAPIView):
    serializer_class = ClothingsSerializer

    def get_queryset(self):
        item_type = self.kwargs['filter']
        if item_type != 'all':
            queryset = Clothings.objects.filter(type__exact=item_type)
            return queryset
        else:
            queryset = Clothings.objects.all()
            return queryset


class GetItem(generics.ListAPIView):
    serializer_class = ClothingsSerializer

    def get_queryset(self):
        item_id = self.kwargs['id']
        queryset = Clothings.objects.filter(id__exact=item_id)
        return queryset


class TypeListView(generics.ListAPIView):
    serializer_class = TypeOfClothesSerializer
    queryset = TypeOfClothes.objects.all()


class GetPages(generics.ListAPIView):
    serializer_class = ClothingsSerializer

    def get_queryset(self):
        filter = self.kwargs['filter']
        print('----------',filter,'-------', sep='\n')
        if filter != 'all':
            id_c = TypeOfClothes.objects.get(slug__exact=filter).id
            lst = list(Clothings.objects.filter(type_id=id_c))
            print(lst)
            return lst
        return list(Clothings.objects.all())


class PageItem(generics.ListAPIView):
    serializer_class = ClothingsSerializer

    def get_queryset(self):
        n_page = int(self.kwargs['page'])
        filter = self.kwargs['filter']
        print('----------',filter,'-------', sep='\n')
        if filter != 'all':
            id_c = TypeOfClothes.objects.get(slug__exact=filter).id
            lst = list(Clothings.objects.filter(type_id=id_c))[n_page * 2 - 2:n_page * 2]
            print(lst)
            return lst
        return list(Clothings.objects.all())[n_page*2-2:n_page*2]


class GetCategories(generics.ListAPIView):
    serializer_class = TypeOfClothesSerializer

    def get_queryset(self):
        queryset = list()
        for category in TypeOfClothes.objects.all():
            queryset.append(category)
        return queryset

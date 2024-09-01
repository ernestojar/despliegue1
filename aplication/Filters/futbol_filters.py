import django_filters
from aplication.models import *


class FutbolFilter(django_filters.FilterSet):
    nombre_local = django_filters.CharFilter(method='filter_por_nombre_local')
    nombre_visitante = django_filters.CharFilter(method='filter_por_nombre_visitante')

    class Meta:
        model = futbol
        fields = ['nombre_local', 'nombre_visitante']

    def filter_por_nombre_local(self, queryset, name, value):
        return queryset.filter(equipo_local__nombre__icontains=value)

    def filter_por_nombre_visitante(self, queryset, name, value):
        return queryset.filter(equipo_visitante__nombre__icontains=value)

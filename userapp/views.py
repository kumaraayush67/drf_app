from rest_framework import viewsets, filters
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['first_name','last_name']
    ordering_fields = '__all__'
    ordering = 'id'

    def put(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        return self.partial_update(request, *args, **kwargs)

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Product, ShopList
from .serializers import UserSerializer, ProductSerializer, ShopListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

    @action(detail=True, methods=['post'])
    def add_friend(self, request, pk=None):
        user = self.get_object()
        friend_id = request.data.get('friend_id')

        if friend_id is None:
            return Response({'error': 'Необходимо указать friend_id.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            friend = User.objects.get(pk=friend_id)
        except User.DoesNotExist:
            return Response({'error': 'Друг с указанным id не найден.'}, status=status.HTTP_404_NOT_FOUND)

        user.friends.add(friend)
        return Response({'status': 'Друг успешно добавлен.'})

    @action(detail=True, methods=['post'])
    def del_friend(self, request, pk=None):
        user = self.get_object()
        friend_id = request.data.get('friend_id')

        if friend_id is None:
            return Response({'error': 'Необходимо указать friend_id.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            friend = User.objects.get(pk=friend_id)
        except User.DoesNotExist:
            return Response({'error': 'Друг с указанным id не найден.'}, status=status.HTTP_404_NOT_FOUND)

        user.friends.remove(friend)
        return Response({'status': 'Друг успешно добавлен.'})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

class ShopListViewSet(viewsets.ModelViewSet):
    queryset = ShopList.objects.all()
    serializer_class = ShopListSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    @action(detail=True, methods=['post'])
    def add_participant(self, request, pk=None):
        shoplist = self.get_object()
        participant_id = request.data.get('participant_id')

        if participant_id is None:
            return Response({'error': 'Необходимо указать participant_id.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            participant = User.objects.get(pk=participant_id)
        except User.DoesNotExist:
            return Response({'error': 'Участник с указанным id не найден.'}, status=status.HTTP_404_NOT_FOUND)

        shoplist.participants.add(participant)
        return Response({'status': 'Участник успешно добавлен.'})

    @action(detail=True, methods=['post'])
    def del_participant(self, request, pk=None):
        shoplist = self.get_object()
        participant_id = request.data.get('participant_id')

        if participant_id is None:
            return Response({'error': 'Необходимо указать participant_id.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            participant = User.objects.get(pk=participant_id)
        except User.DoesNotExist:
            return Response({'error': 'Участник с указанным id не найден.'}, status=status.HTTP_404_NOT_FOUND)

        shoplist.participants.remove(participant)
        return Response({'status': 'Участник успешно удален.'})

    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
          shoplist = self.get_object()
          product_id = request.data.get('product_id')

          if product_id is None:
              return Response({'error': 'Необходимо указать product_id'}, status=status.HTTP_400_BAD_REQUEST)
          try:
              product = Product.objects.get(pk = product_id)
          except Product.DoesNotExist:
              return Response({'error': 'Продукт с указанным id не найден'}, status=status.HTTP_404_NOT_FOUND)
          
          shoplist.products.add(product)
          return Response({'status': 'Продукт успешно добавлен'})
    
    @action(detail=True, methods=['post'])
    def del_product(self, request, pk=None):
          shoplist = self.get_object()
          product_id = request.data.get('product_id')

          if product_id is None:
              return Response({'error': 'Необходимо указать product_id'}, status=status.HTTP_400_BAD_REQUEST)
          try:
              product = Product.objects.get(pk = product_id)
          except Product.DoesNotExist:
              return Response({'error': 'Продукт с указанным id не найден'}, status=status.HTTP_404_NOT_FOUND)
          
          shoplist.products.remove(product)
          return Response({'status': 'Продукт успешно удален'})
    
    @action(detail=True, methods=['get'])  
    def get_products(self, request, pk=None):
        shoplist = self.get_object()  
        products = shoplist.products.all() 
        serializer = ProductSerializer(products, many=True) 
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])  
    def get_participants(self, request, pk=None):
        shoplist = self.get_object()  
        participants = shoplist.participants.all() 
        serializer = UserSerializer(participants, many=True) 
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def add_new_product(self, request, pk=None):
        shoplist = self.get_object()  
        product_serializer = ProductSerializer(data=request.data)

        if product_serializer.is_valid():
            product = product_serializer.save()

            shoplist.products.add(product)

            return Response(
                product_serializer.data, 
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


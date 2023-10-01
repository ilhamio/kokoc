from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from charity.models import Charity, CharitySubscription
from charity.serializers import CharitySerializer, CharitySubscriptionSerializer, CreateCharitySubscriptionSerializer


class CharityViewSet(viewsets.ModelViewSet):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer


class CharitySubscriptionViewSet(
                                 mixins.ListModelMixin,
                                 mixins.DestroyModelMixin,
                                 GenericViewSet):
    queryset = CharitySubscription.objects.all()
    serializer_class = CharitySubscriptionSerializer

    def list(self, request, *args, **kwargs):
        instance = self.request.user.subscription
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(method='post', request_body=CreateCharitySubscriptionSerializer,
                         responses={200: "{'result': 'successfully applied'}", 401: "{'error': 'Not authenticated'}"})
    @action(detail=False, methods=['POST'])
    def apply(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'Not authenticated'}, status=401)
        data = request.data
        data['user'] = request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'result': "successfully applied"}, status=200)
#
#
# @api_view(['POST'])
# def transfer_money(request):
#     user = request.user
#     amount = request.data.get('amount')
#     charity_id = request.data.get('charity_id')
#
#     try:
#         user_charity = UserCharity.objects.get(user=user)
#     except UserCharity.DoesNotExist:
#         return Response({'error': 'User has no associated charity'}, status=status.HTTP_400_BAD_REQUEST)
#
#     if user_charity.sum < amount:
#         return Response({'error': 'Not enough funds'}, status=status.HTTP_400_BAD_REQUEST)
#
#     user_charity.sum -= amount
#     user_charity.save()
#
#     try:
#         charity = Charity.objects.get(pk=charity_id)
#     except Charity.DoesNotExist:
#         return Response({'error': 'Charity not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     charity.got_sum += amount
#     charity.save()
#
#     return Response({'message': 'Money transferred successfully'}, status=status.HTTP_200_OK)

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from charity.models import Charity, CharitySubscription, UserCharity
from charity.serializers import CharitySerializer, CharitySubscriptionSerializer

class CharityViewSet(viewsets.ModelViewSet):
    queryset = Charity.objects.all()
    # filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    serializer_class = CharitySerializer
    # ordering_fields = ['name', 'coefficient']
    # ordering = ['name']
    # search_fields = ['name', 'description']

class CharitySubscriptionViewSet(viewsets.ModelViewSet):
    queryset = CharitySubscription.objects.all()
    serializer_class = CharitySubscriptionSerializer

    @action(detail=True, methods=['POST'])
    def apply(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'Not authenticated'}, status=401)
        obj: CharitySubscription = self.get_object()

        if obj.user != request.user:
            return Response({'error': 'You can only create subscriptions for yourself'}, status=403)

        request.user.charity_subscription.add(obj)
        return Response({'result': "successfully applied"}, status=200)


@api_view(['POST'])
def transfer_money(request):
    user = request.user
    amount = request.data.get('amount')
    charity_id = request.data.get('charity_id')

    try:
        user_charity = UserCharity.objects.get(user=user)
    except UserCharity.DoesNotExist:
        return Response({'error': 'User has no associated charity'}, status=status.HTTP_400_BAD_REQUEST)

    if user_charity.sum < amount:
        return Response({'error': 'Not enough funds'}, status=status.HTTP_400_BAD_REQUEST)

    user_charity.sum -= amount
    user_charity.save()

    try:
        charity = Charity.objects.get(pk=charity_id)
    except Charity.DoesNotExist:
        return Response({'error': 'Charity not found'}, status=status.HTTP_404_NOT_FOUND)

    charity.got_sum += amount
    charity.save()

    return Response({'message': 'Money transferred successfully'}, status=status.HTTP_200_OK)

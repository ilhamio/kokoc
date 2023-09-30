from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from charity.models import Charity, CharitySubscription
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



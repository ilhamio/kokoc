from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from .filters import CharityFilterSet

from charity.models import Charity, CharitySubscription, Wallet, Transaction
from charity.serializers import CharitySerializer, CharitySubscriptionSerializer, CreateCharitySubscriptionSerializer, \
    TransactionSerializer


class CharityViewSet(viewsets.ModelViewSet):
    queryset = Charity.objects.filter(is_active=True, approved=True)
    serializer_class = CharitySerializer


class CharitySubscriptionViewSet(viewsets.ModelViewSet):
    queryset = CharitySubscription.objects.all()
    serializer_class = CharitySubscriptionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CharityFilterSet

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


class TransactionViewSet(mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        wallet: Wallet = user.wallet

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        data['user'] = request.user
        activity_id = data['fund']
        del data['fund']
        fund = Charity.objects.filter(pk=activity_id, is_active=True, approved=True)

        if len(fund) == 0:
            return Response({"error": "Fund error"}, status=status.HTTP_400_BAD_REQUEST)
        fund = fund[0]
        if wallet.balance < data['sum']:
            return Response({"error": "Amount error"}, status=status.HTTP_400_BAD_REQUEST)

        wallet -= data['sum']
        wallet.save()
        fund.sum += data['sum']
        fund.save()

        Transaction.objects.create(user_id=request.user.id, fund_id=activity_id, sum=data['sum'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

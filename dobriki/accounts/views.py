from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response

from accounts.serializers import UserDetailsSerializer
from activity.models import Aim
from charity.models import Wallet


class UserDetailAPIView(RetrieveUpdateAPIView):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email

    Returns UserModel fields.
    """
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        """
        return get_user_model().objects.none()

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user_data = request.data
        userprofile_data = user_data.get('userprofile', {})

        # Обновляем поля height, weight и age, если они предоставлены в запросе
        if 'height' in userprofile_data:
            user.userprofile.height = userprofile_data['height']
        if 'weight' in userprofile_data:
            user.userprofile.weight = userprofile_data['weight']
        if 'age' in userprofile_data:
            user.userprofile.age = userprofile_data['age']

        # Сохраняем изменения в UserProfile
        user.userprofile.save()
        return Response(self.get_serializer(user).data)


class RegisterAPIView(RegisterView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)

        if data:
            Aim.objects.create(user=user)
            Wallet.objects.create(user=user)
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

        return response

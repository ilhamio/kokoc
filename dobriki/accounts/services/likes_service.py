from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from feed.models import Like

User = get_user_model()


def apply(obj, user):
    """Подать заявку в команду """
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(content_type=obj_type, object_id=obj.id, user=user)
    return like
from django.conf import settings
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import SlidingToken


from .models import User
from .serializers import RequestLoginSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def request_login_email(request):
    serializer = RequestLoginSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    user_data = serializer.data

    user, created = User.objects.get_or_create(email__iexact=user_data["email"])

    token = SlidingToken.for_user(user)

    # send email to user
    send_mail(
        subject="Your Linkanizer Login Link",
        message=f"Navigate to {settings.FRONTEND_BASE_URL}{token}",
        from_email="No Reply <noreply@tmk.name>",
        recipient_list=[user.email],
    )

    return Response(status=status.HTTP_200_OK)

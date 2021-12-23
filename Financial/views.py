from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from .models import financial
from .serializers import listfinancialSerializer
from rest_framework.generics import ListAPIView


class ViewFinancial(ListAPIView, LoginRequiredMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = listfinancialSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return financial.objects.all()
        else:
            return financial.objects.filter(userRecipientofmoney=self.request.user)

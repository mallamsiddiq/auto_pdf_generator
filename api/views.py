from django.http import HttpResponse
from rest_framework.response import Response
from django.views.generic import View
from rest_framework.views import APIView
from .process import html_to_pdf 
from xhtml2pdf import pisa
from .serializers import DocSerializer,TranscSerializer,TranscCreateSerializer
from .models import Document,Transaction
from .filters import DocFilter
from rest_framework import generics, status
from django.conf import settings
from django.core.files import File
from pathlib import Path
from io import BytesIO
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import datetime
from django.db.models import Count




class DocView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Document.objects.all()
    serializer_class = DocSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DocFilter



class TranscView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    # 
    def get_serializer_class(self):
        if self.request.method == "GET":
            return TranscSerializer
        return TranscCreateSerializer
    # serializer_class = get_serializer_class
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request,format=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user_instance=request.user
        # serializer = self.get_serializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        save_instance=serializer.save(user=user_instance)

        pdf = html_to_pdf('api/transactions.html')
        receipt_file = BytesIO(pdf.content)
        response = HttpResponse(pdf, content_type='application/pdf')
        for i in range(1,11):
            filename = f'transaction_%s_%s_(%s).pdf'% (user_instance,save_instance.id,i)
            new_article = save_instance.documents.create(title="new doc %s"% (i),doc=File(receipt_file, filename))

        # return HttpResponse(pdf, content_type='application/pdf')
        return Response('hurray transaction created with 10 recipts pdf accordindinlly', status=200)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request,):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_auth_data=serializer.data
        return Response('boom success!! Account created for %s'%(user_auth_data['name']))





        
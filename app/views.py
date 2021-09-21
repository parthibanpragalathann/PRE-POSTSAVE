from rest_framework import generics, mixins
from .serializer import *
from .models import *

class CreditView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CreditSerializer
    queryset = CreditAmount.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class CreditModifyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CreditSerializer
    queryset = CreditAmount.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LoanView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = LoanSerializer
    queryset = LoanAmount.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

class LoanDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = LoanSerializer
    queryset = LoanAmount.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DebitView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DebitSerializer
    queryset = DebitAmount.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class DebitModifyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DebitSerializer
    queryset = DebitAmount.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BalanceView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BalanceSerializer
    queryset = BalanceAmount.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

class BalanceDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = BalanceSerializer
    queryset = BalanceAmount.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
from rest_framework import viewsets, permissions
from .models import Supplier, Material, Printer, Part, PrintJob
from .serializers import (
    SupplierSerializer, MaterialSerializer, PrinterSerializer,
    PartSerializer, PrintJobReadSerializer, PrintJobWriteSerializer
)

# ViewSet para Fornecedores
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    # permission_classes = [permissions.IsAuthenticated] # Adicionar permissões depois

# ViewSet para Materiais
class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    # permission_classes = [permissions.IsAuthenticated]

# ViewSet para Impressoras
class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer
    # permission_classes = [permissions.IsAuthenticated]

# ViewSet para Modelos 3D (Peças)
class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # Sobrescrever perform_create para associar o uploader automaticamente
    def perform_create(self, serializer):
        # Assumindo que a autenticação está configurada e o usuário está em self.request.user
        # serializer.save(uploader=self.request.user)
        serializer.save() # Simplificando por enquanto sem autenticação

# ViewSet para Pedidos de Impressão
class PrintJobViewSet(viewsets.ModelViewSet):
    queryset = PrintJob.objects.all().order_by("-request_date")
    # permission_classes = [permissions.IsAuthenticated]

    # Usar serializers diferentes para leitura e escrita
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PrintJobReadSerializer
        return PrintJobWriteSerializer

    # Sobrescrever perform_create para associar o solicitante automaticamente
    def perform_create(self, serializer):
        # Assumindo que a autenticação está configurada e o usuário está em self.request.user
        # serializer.save(requester=self.request.user, status=\'requested\')
        serializer.save(status='requested') # Corrigido: Removido \ e usado aspas simples


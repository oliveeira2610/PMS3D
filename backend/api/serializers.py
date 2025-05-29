from rest_framework import serializers
from .models import Supplier, Material, Printer, Part, PrintJob
from django.contrib.auth.models import User

# Serializer para Fornecedores
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

# Serializer para Materiais
class MaterialSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model = Material
        fields = ['id', 'name', 'type', 'supplier', 'supplier_name', 'cost_per_unit', 'unit_of_measure', 'quantity_on_hand', 'min_stock_level', 'properties_text', 'date_added', 'expiry_date']
        read_only_fields = ['date_added']

# Serializer para Impressoras
class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'
        read_only_fields = ['operational_hours'] # Simplificando, não vamos calcular isso agora

# Serializer para Usuários (simplificado para referência)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

# Serializer para Modelos 3D (Peças)
class PartSerializer(serializers.ModelSerializer):
    uploader_username = serializers.CharField(source='uploader.username', read_only=True)

    class Meta:
        model = Part
        fields = ['id', 'name', 'description', 'version', 'file_path', 'uploader', 'uploader_username', 'upload_date']
        read_only_fields = ['upload_date']

# Serializer para Pedidos de Impressão (Leitura)
class PrintJobReadSerializer(serializers.ModelSerializer):
    part_name = serializers.CharField(source='part.name', read_only=True)
    requester_username = serializers.CharField(source='requester.username', read_only=True)
    printer_name = serializers.CharField(source='printer.name', read_only=True, allow_null=True)
    material_name = serializers.CharField(source='material.name', read_only=True, allow_null=True)

    class Meta:
        model = PrintJob
        fields = [
            'id', 'part', 'part_name', 'requester', 'requester_username',
            'printer', 'printer_name', 'material', 'material_name', 'quantity',
            'priority', 'status', 'estimated_print_time', 'actual_print_time',
            'estimated_material_usage', 'actual_material_usage', 'estimated_cost',
            'actual_cost', 'notes', 'request_date', 'start_time', 'end_time'
        ]
        read_only_fields = [
            'part_name', 'requester_username', 'printer_name', 'material_name',
            'request_date', 'actual_print_time', 'actual_material_usage', 'actual_cost'
        ] # Campos que são calculados ou definidos pelo sistema/relacionamentos

# Serializer para Pedidos de Impressão (Escrita/Criação)
class PrintJobWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintJob
        fields = [
            'part', 'requester', 'printer', 'material', 'quantity',
            'priority', 'status', 'estimated_print_time',
            'estimated_material_usage', 'estimated_cost', 'notes'
        ]
        # Requester será provavelmente definido automaticamente com base no usuário logado na view
        # Status inicial pode ser definido na view também


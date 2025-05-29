from django.db import models
from django.contrib.auth.models import User

# Modelo para Fornecedores
class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome do Fornecedor")
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pessoa de Contato")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telefone")
    address = models.TextField(blank=True, null=True, verbose_name="Endereço")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

# Modelo para Materiais
class Material(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Quilogramas (kg)'),
        ('g', 'Gramas (g)'),
        ('L', 'Litros (L)'),
        ('mL', 'Mililitros (mL)'),
        ('unit', 'Unidade'),
    ]
    TYPE_CHOICES = [
        ('Filament', 'Filamento'),
        ('Resin', 'Resina'),
        ('Powder', 'Pó'),
        ('Other', 'Outro'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nome do Material")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Tipo")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fornecedor")
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Custo por Unidade")
    unit_of_measure = models.CharField(max_length=10, choices=UNIT_CHOICES, verbose_name="Unidade de Medida")
    quantity_on_hand = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, verbose_name="Quantidade em Estoque")
    min_stock_level = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, verbose_name="Nível Mínimo de Estoque")
    # properties = models.JSONField(blank=True, null=True, verbose_name="Propriedades") # Adiar JSONField para simplicidade inicial
    properties_text = models.TextField(blank=True, null=True, verbose_name="Propriedades (Texto)")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Data de Adição")
    expiry_date = models.DateField(blank=True, null=True, verbose_name="Data de Validade")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"

# Modelo para Impressoras
class Printer(models.Model):
    STATUS_CHOICES = [
        ('available', 'Disponível'),
        ('printing', 'Imprimindo'),
        ('maintenance', 'Manutenção'),
        ('offline', 'Offline'),
        ('error', 'Erro'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nome/ID da Impressora")
    model = models.CharField(max_length=255, verbose_name="Modelo")
    manufacturer = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fabricante")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='offline', verbose_name="Status")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Localização")
    # compatible_material_types = models.ManyToManyField(MaterialType) # Simplificar inicialmente
    date_acquired = models.DateField(blank=True, null=True, verbose_name="Data de Aquisição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Impressora"
        verbose_name_plural = "Impressoras"

# Modelo para Modelos 3D (Peças)
class Part(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome do Modelo/Peça")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    version = models.CharField(max_length=50, blank=True, null=True, verbose_name="Versão")
    file_path = models.FileField(upload_to='parts/', blank=True, null=True, verbose_name="Arquivo do Modelo") # Usar FileField
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Uploader")
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="Data do Upload")

    def __str__(self):
        return f"{self.name} (v{self.version})"

    class Meta:
        verbose_name = "Modelo 3D (Peça)"
        verbose_name_plural = "Modelos 3D (Peças)"

# Modelo para Pedidos de Impressão
class PrintJob(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Solicitado'),
        ('approved', 'Aprovado'),
        ('queued', 'Na Fila'),
        ('printing', 'Imprimindo'),
        ('completed', 'Concluído'),
        ('failed', 'Falhou'),
        ('cancelled', 'Cancelado'),
    ]

    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name="Peça")
    requester = models.ForeignKey(User, related_name='requested_jobs', on_delete=models.CASCADE, verbose_name="Solicitante")
    printer = models.ForeignKey(Printer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Impressora Designada")
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Material Utilizado")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantidade")
    priority = models.IntegerField(default=0, verbose_name="Prioridade") # 0 = Normal, >0 = Alta
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='requested', verbose_name="Status")
    estimated_print_time = models.DurationField(blank=True, null=True, verbose_name="Tempo Estimado")
    actual_print_time = models.DurationField(blank=True, null=True, verbose_name="Tempo Real")
    estimated_material_usage = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, verbose_name="Material Estimado") # Em unidades do material
    actual_material_usage = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, verbose_name="Material Real")
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Custo Estimado")
    actual_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Custo Real")
    notes = models.TextField(blank=True, null=True, verbose_name="Observações")
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="Data da Solicitação")
    start_time = models.DateTimeField(blank=True, null=True, verbose_name="Início da Impressão")
    end_time = models.DateTimeField(blank=True, null=True, verbose_name="Fim da Impressão")

    def __str__(self):
        return f"Pedido #{self.id} - {self.part.name}"

    class Meta:
        verbose_name = "Pedido de Impressão"
        verbose_name_plural = "Pedidos de Impressão"
        ordering = ['-request_date']

# Adicionar outros modelos (MaintenanceLog, QualityCheck) posteriormente


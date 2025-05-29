# 03 - Modelagem de Dados

Este documento apresenta o modelo de dados proposto para o Sistema de Gerenciamento de Impressão 3D. Ele detalha as principais entidades (tabelas), seus atributos (campos) e os relacionamentos entre elas, formando a base para a estrutura do banco de dados PostgreSQL.

## Entidades Principais e Relacionamentos

A seguir, descrevemos as entidades centrais do sistema e como elas se conectam:

1.  **Usuarios (Users):** Representa os usuários do sistema.
    *   `id` (PK): Identificador único.
    *   `username`: Nome de usuário para login.
    *   `password_hash`: Hash da senha.
    *   `email`: Endereço de e-mail.
    *   `first_name`: Primeiro nome.
    *   `last_name`: Sobrenome.
    *   `role`: Papel do usuário (ex: 'admin', 'operador', 'solicitante').
    *   `date_joined`: Data de cadastro.
    *   `is_active`: Status do usuário.

2.  **Fornecedores (Suppliers):** Armazena informações sobre os fornecedores de materiais.
    *   `id` (PK): Identificador único.
    *   `name`: Nome do fornecedor.
    *   `contact_person`: Pessoa de contato.
    *   `email`: E-mail de contato.
    *   `phone`: Telefone de contato.
    *   `address`: Endereço.

3.  **Materiais (Materials):** Descreve os materiais de impressão disponíveis.
    *   `id` (PK): Identificador único.
    *   `name`: Nome do material (ex: 'PLA Preto', 'Resina ABS Cinza').
    *   `type`: Tipo de material (ex: 'Filamento', 'Resina', 'Pó').
    *   `supplier_id` (FK -> Suppliers.id): Fornecedor do material.
    *   `cost_per_unit`: Custo por unidade (ex: por kg, por litro).
    *   `unit_of_measure`: Unidade de medida (ex: 'kg', 'g', 'L', 'mL').
    *   `quantity_on_hand`: Quantidade atual em estoque (na unidade de medida).
    *   `min_stock_level`: Nível mínimo de estoque para alerta.
    *   `properties`: Descrição das propriedades técnicas (JSON ou Text).
    *   `safety_info`: Informações de segurança (link ou Text).
    *   `date_added`: Data de adição ao estoque.
    *   `expiry_date`: Data de validade (se aplicável).

4.  **Impressoras (Printers):** Gerencia as impressoras 3D.
    *   `id` (PK): Identificador único.
    *   `name`: Nome ou identificador da impressora (ex: 'Prusa MK3S+ Lab01').
    *   `model`: Modelo da impressora.
    *   `manufacturer`: Fabricante.
    *   `status`: Status atual (ex: 'disponivel', 'imprimindo', 'manutencao', 'offline').
    *   `location`: Localização física da impressora.
    *   `operational_hours`: Horas totais de operação registradas.
    *   `compatible_material_types`: Tipos de materiais compatíveis (lista ou relação ManyToMany).
    *   `date_acquired`: Data de aquisição.

5.  **Modelos3D (Parts):** Biblioteca de modelos digitais para impressão.
    *   `id` (PK): Identificador único.
    *   `name`: Nome do modelo/peça.
    *   `description`: Descrição.
    *   `version`: Versão do modelo.
    *   `file_path`: Caminho para o arquivo do modelo (STL, 3MF, etc.).
    *   `uploader_id` (FK -> Users.id): Usuário que fez o upload.
    *   `upload_date`: Data do upload.
    *   `estimated_print_time_default`: Tempo estimado padrão (pode ser recalculado no pedido).
    *   `estimated_material_usage_default`: Consumo estimado padrão.

6.  **PedidosImpressao (PrintJobs):** Representa um trabalho de impressão solicitado.
    *   `id` (PK): Identificador único.
    *   `part_id` (FK -> Parts.id): Modelo 3D a ser impresso.
    *   `requester_id` (FK -> Users.id): Usuário que solicitou a impressão.
    *   `printer_id` (FK -> Printers.id, nullable=True): Impressora designada (pode ser definida depois).
    *   `material_id` (FK -> Materials.id, nullable=True): Material a ser utilizado.
    *   `quantity`: Quantidade de peças a imprimir.
    *   `priority`: Prioridade do pedido.
    *   `status`: Status do pedido (ex: 'solicitado', 'aprovado', 'na_fila', 'imprimindo', 'concluido', 'falhou', 'cancelado').
    *   `estimated_print_time`: Tempo de impressão estimado para este pedido.
    *   `actual_print_time`: Tempo real de impressão.
    *   `estimated_material_usage`: Consumo de material estimado.
    *   `actual_material_usage`: Consumo real de material.
    *   `estimated_cost`: Custo estimado.
    *   `actual_cost`: Custo real calculado.
    *   `notes`: Observações adicionais.
    *   `request_date`: Data da solicitação.
    *   `start_time`: Data e hora de início da impressão.
    *   `end_time`: Data e hora de conclusão ou falha.

7.  **RegistrosManutencao (MaintenanceLogs):** Histórico de manutenção das impressoras.
    *   `id` (PK): Identificador único.
    *   `printer_id` (FK -> Printers.id): Impressora que recebeu manutenção.
    *   `technician_id` (FK -> Users.id): Técnico responsável.
    *   `maintenance_type`: Tipo de manutenção (ex: 'preventiva', 'corretiva').
    *   `description`: Descrição do serviço realizado.
    *   `date_performed`: Data da manutenção.
    *   `cost`: Custo da manutenção.

8.  **VerificacoesQualidade (QualityChecks):** Registros de inspeção de qualidade das peças impressas.
    *   `id` (PK): Identificador único.
    *   `print_job_id` (FK -> PrintJobs.id): Pedido de impressão associado.
    *   `inspector_id` (FK -> Users.id): Usuário que realizou a inspeção.
    *   `check_date`: Data da inspeção.
    *   `status`: Resultado (ex: 'aprovado', 'reprovado', 'aprovado_com_ressalvas').
    *   `notes`: Observações da inspeção.
    *   `checklist_results`: Resultados de um checklist específico (JSON ou relação com outra tabela).

## Relacionamentos Chave (Resumo)

*   `Usuarios` podem solicitar múltiplos `PedidosImpressao` e fazer upload de múltiplos `Modelos3D`.
*   `Fornecedores` fornecem múltiplos `Materiais`.
*   `Materiais` são usados em múltiplos `PedidosImpressao`.
*   `Impressoras` realizam múltiplos `PedidosImpressao` e possuem múltiplos `RegistrosManutencao`.
*   `Modelos3D` podem ser impressos em múltiplos `PedidosImpressao`.
*   `PedidosImpressao` estão associados a um `Modelo3D`, um `Usuario` solicitante, uma `Impressora` e um `Material`, e podem ter múltiplas `VerificacoesQualidade`.

(Este modelo inicial pode ser refinado. Diagramas Entidade-Relacionamento (DER) serão gerados com base nesta descrição para visualização.)


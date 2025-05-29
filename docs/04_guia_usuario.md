# 04 - Guia do Usuário

Este documento fornecerá instruções sobre como utilizar as funcionalidades do Sistema de Gerenciamento de Impressão 3D assim que a interface do usuário (frontend) for desenvolvida.

**Estado Atual (Protótipo):**

No estágio atual, o foco foi no desenvolvimento do backend e da API RESTful. A interface do usuário (frontend com React/TypeScript) foi inicializada, mas as telas para interação com as funcionalidades ainda não foram implementadas.

**Próximos Passos (Desenvolvimento Frontend):**

O desenvolvimento futuro incluirá a criação de componentes React para:

*   Autenticação de usuários (Login/Logout).
*   Navegação principal pela aplicação.
*   CRUD (Criar, Ler, Atualizar, Deletar) para Materiais, Fornecedores, Impressoras e Peças (Modelos 3D).
*   Criação e acompanhamento de Pedidos de Impressão.
*   Visualização de dashboards com custos e métricas.
*   Gerenciamento de configurações do usuário.

**Interação via API (Desenvolvimento/Teste):**

Atualmente, a interação com o sistema pode ser feita diretamente através da API RESTful exposta pelo backend. Ferramentas como `curl`, Postman ou Insomnia podem ser usadas para testar os endpoints disponíveis em `/api/` (ex: `/api/materials/`, `/api/printers/`, etc.).

(Este guia será atualizado progressivamente conforme o desenvolvimento do frontend avançar.)


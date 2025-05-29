# 01 - Requisitos

Este documento detalha os requisitos funcionais e não funcionais do Sistema de Gerenciamento de Impressão 3D.

## Requisitos Funcionais

Os requisitos funcionais detalhados, incluindo os pilares essenciais e os diferenciais inovadores propostos, estão descritos no documento de Escopo Funcional:
*   `/home/ubuntu/sistema_gerenciamento_impressao_3d_final/escopo_funcional.md`

O protótipo inicial implementou as funcionalidades básicas de cadastro e listagem para Materiais, Impressoras, Peças e Pedidos via API REST.

## Requisitos Não Funcionais

*   **Desempenho:** O sistema deve responder rapidamente às interações do usuário (validado parcialmente na API).
*   **Escalabilidade:** A arquitetura (Django/React) permite o crescimento do número de usuários, impressoras e dados gerenciados.
*   **Usabilidade:** A interface deve ser intuitiva e fácil de usar (a ser desenvolvida e validada no frontend).
*   **Segurança:** O acesso aos dados deve ser controlado por autenticação e autorização (a ser implementado).
*   **Manutenibilidade:** O código deve ser bem documentado e seguir boas práticas para facilitar futuras modificações (estrutura inicial criada).
*   **Confiabilidade:** O sistema deve ser estável e minimizar a ocorrência de erros (protótipo inicial estável).


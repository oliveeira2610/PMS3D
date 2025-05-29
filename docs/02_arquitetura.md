# 02 - Arquitetura do Sistema

Este documento descreve a arquitetura de alto nível do Sistema de Gerenciamento de Impressão 3D, detalhando os principais componentes, suas interações e as tecnologias selecionadas para garantir uma solução robusta, escalável e moderna.

## Visão Geral da Arquitetura

O sistema adotará uma arquitetura de aplicação web monolítica inicialmente, seguindo o padrão Cliente-Servidor. Esta abordagem, utilizando o framework Django, permite um desenvolvimento inicial mais rápido e coeso, ideal para a fase de prototipagem e validação. A comunicação entre o cliente (navegador web) e o servidor será realizada principalmente através de APIs RESTful.

## Componentes Principais

1.  **Frontend (Cliente):**
    *   **Tecnologia:** React com TypeScript.
    *   **Responsabilidade:** Interface do usuário (UI) e experiência do usuário (UX). Renderiza as informações recebidas do backend e envia as requisições do usuário. Será uma Single Page Application (SPA) para proporcionar uma experiência fluida e responsiva.
    *   **Comunicação:** Consome as APIs RESTful expostas pelo backend para buscar e enviar dados.

2.  **Backend (Servidor):**
    *   **Tecnologia:** Python com o framework Django.
    *   **Responsabilidade:** Lógica de negócios principal, processamento de dados, gerenciamento de autenticação e autorização, e exposição das APIs RESTful para o frontend. Orquestra as interações com o banco de dados.
    *   **APIs:** Utilizará o Django REST Framework (DRF) para construir APIs RESTful eficientes e bem documentadas, facilitando a comunicação com o frontend e potenciais integrações futuras.

3.  **Banco de Dados:**
    *   **Tecnologia:** PostgreSQL.
    *   **Responsabilidade:** Persistência dos dados da aplicação, incluindo informações sobre usuários, materiais, impressoras, peças, pedidos, custos, métricas e logs.
    *   **Interação:** O backend (Django ORM) interagirá com o PostgreSQL para realizar operações CRUD (Create, Read, Update, Delete).

## Fluxo de Comunicação

*   O usuário interage com a interface React/TypeScript no navegador.
*   As ações do usuário disparam requisições HTTP (GET, POST, PUT, DELETE) para as APIs RESTful do backend Django.
*   O backend processa a requisição, aplica a lógica de negócios necessária e interage com o banco de dados PostgreSQL através do ORM do Django.
*   O backend retorna uma resposta (geralmente em formato JSON) para o frontend.
*   O frontend atualiza a interface do usuário com base na resposta recebida.

## Considerações Futuras

Embora iniciando como um monolito, a arquitetura será projetada com modularidade em mente. Se a complexidade aumentar significativamente ou requisitos específicos surgirem, a migração para uma arquitetura de microsserviços ou a extração de componentes específicos (como o módulo de análise de dados ou notificações) poderá ser considerada no futuro. A utilização de APIs RESTful desde o início facilita essa evolução.

(Diagramas visuais da arquitetura poderão ser adicionados posteriormente, utilizando ferramentas externas ou representações textuais mais elaboradas, se necessário.)


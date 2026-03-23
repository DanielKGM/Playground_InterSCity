<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://interscity.koyeb.app/">
    <img src="static/icon.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">InterSCity Playground</h3>

  <p align="center">
    Um playground interativo construído em Streamlit para explorar e realizar requisições na API da plataforma InterSCity.
    <br />
    <br />
    <a href="https://interscity.koyeb.app/"><strong>Acessar o Live Demo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DanielKGM/Playground_InterSCity/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/DanielKGM/Playground_InterSCity/issues">Solicitar Feature</a>
  </p>
</div>

<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#arquitetura-e-microsserviços">Arquitetura e Microsserviços</a></li>
        <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#começando">Começando</a>
      <ul>
        <li><a href="#pré-requisitos">Pré-requisitos</a></li>
        <li><a href="#instalação">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#licença">Licença</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

## Sobre o Projeto

Este projeto é uma interface simples (playground) desenvolvida para facilitar a interação com a plataforma **InterSCity**. 

A plataforma InterSCity é um projeto de código aberto (licenciado sob MPL 2.0) criado para apoiar tecnicamente o desenvolvimento de projetos de Cidades Inteligentes (*Smart Cities*). Seu principal objetivo é fornecer serviços e APIs de alto nível para integrar tecnologias fundamentais como IoT, Big Data e Cloud Computing. A plataforma adota uma arquitetura de microsserviços para suportar a integração de uma grande quantidade de dispositivos e dados em escala municipal.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

### Arquitetura e Microsserviços

A arquitetura do InterSCity foi desenhada para abstrair a complexidade da comunicação entre aplicações e dispositivos IoT. Abaixo está o resumo dos principais microsserviços explorados neste playground:

* **Resource Adaptor:** Funciona como um proxy *stateless* que integra dispositivos IoT. Ele permite que serviços externos registrem e atualizem recursos na plataforma, além de enviar dados coletados pelos sensores.
* **Resource Catalog:** Gerencia o registro de todos os recursos da cidade, fornecendo identificadores únicos (UUIDs) e notificando de forma assíncrona a criação de novos recursos para os demais microsserviços.
* **Data Collector:** Armazena os dados dos sensores coletados. Fornece uma API para acessar tanto o contexto atual quanto o histórico de dados dos recursos da cidade, permitindo o uso de um conjunto rico de filtros de busca.
* **Resource Discovery:** Oferece uma API de busca sensível ao contexto. É utilizado por aplicações clientes para descobrir recursos disponíveis combinando filtros como localização, regras de intervalo e metadados.
* **Resource Viewer:** Microsserviço focado em visualização web. Apresenta as informações dos recursos de forma gráfica, incluindo localização, dados em tempo real e gráficos representativos do histórico.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

### Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* [![Python][Python.org]][Python-url]
* [![Streamlit][Streamlit.io]][Streamlit-url]

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Começando

Para rodar o playground localmente na sua máquina, siga os passos abaixo.

### Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. É recomendado o uso de um ambiente virtual (venv).
* Python 3.8+
* pip

### Instalação

1. Clone o repositório
   git clone https://github.com/DanielKGM/Playground_InterSCity.git

2. Entre no diretório do projeto
   cd SEU_REPOSITORIO

3. Instale os pacotes necessários
   pip install -r requirements.txt

4. Execute a aplicação Streamlit
   streamlit run app.py

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Uso

Acesse o **[Live Demo](https://interscity.koyeb.app/)** para testar a aplicação diretamente no seu navegador, sem a necessidade de instalação. Use a interface para construir e disparar requisições contra a API do InterSCity, facilitando a exploração e o entendimento do payload esperado por cada microsserviço.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Licença

Distribuído sob a licença MIT. Veja `LICENSE.txt` para mais informações.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Contato

Daniel Galdez - [LINKEDIN](https://www.linkedin.com/in/daniel-campos-galdez-monteiro/) - danielgaldez10@hotmail.com

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


[contributors-shield]: https://img.shields.io/github/contributors/DanielKGM/Playground_InterSCity.svg?style=for-the-badge
[contributors-url]: https://github.com/DanielKGM/Playground_InterSCity/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DanielKGM/Playground_InterSCity.svg?style=for-the-badge
[forks-url]: https://github.com/DanielKGM/Playground_InterSCity/network/members
[stars-shield]: https://img.shields.io/github/stars/DanielKGM/Playground_InterSCity.svg?style=for-the-badge
[stars-url]: https://github.com/DanielKGM/Playground_InterSCity/stargazers
[issues-shield]: https://img.shields.io/github/issues/DanielKGM/Playground_InterSCity.svg?style=for-the-badge
[issues-url]: https://github.com/DanielKGM/Playground_InterSCity/issues
[license-shield]: https://img.shields.io/github/license/DanielKGM/Playground_InterSCity.svg?style=for-the-badge
[license-url]: https://github.com/DanielKGM/Playground_InterSCity/blob/main/LICENSE.txt
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Streamlit.io]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/

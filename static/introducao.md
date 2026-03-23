<img src="https://interscity.org/wp-content/themes/inct/assets/img/logo/interscity.svg" alt="drawing" width="2000"/>

Plataforma de Cidades Inteligentes

---
## O que é uma cidade inteligente?

> Um lugar onde `soluções digitais` otimizam `serviços e redes tradicionais`, beneficiando seus habitantes e negócios (<a target="_blank" href="https://commission.europa.eu/eu-regional-and-urban-development/topics/cities-and-urban-development/city-initiatives/smart-cities_en">Comissão Européia</a>)
---
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <div style="text-align: top; width: 50%;">
    <h3>Serviço Tradicional: Transporte Público</h3>
    <div style="width: 100%; height: 400px; overflow: hidden;">
      <img src="https://static.portaldaindustria.com.br/portaldaindustria/noticias/media/imagem_plugin/onibus_443znIY.jpg" 
           alt="Serviços Tradicionais" 
           style="width: 100%; height: 100%; object-fit: cover;" />
    </div>
    <p><small>Fonte: <a href="https://noticias.portaldaindustria.com.br/noticias/infraestrutura/reducao-da-tarifa-e-do-tempo-de-espera-incentivariam-uso-do-transporte-publico/">Portal da Industria</a></small></p>
  </div>
  <div style="text-align: top; width: 50%;">
    <h3>Solução Digital: Cobrança Automática</h3>
    <div style="width: 100%; height: 400px; overflow: hidden;">
      <img src="https://static.ric.com.br/uploads/2024/02/cartao-uso-limitado-onibus-8-600x600.jpg" 
           alt="Soluções Digitais" 
           style="width: 100%; height: 100%; object-fit: cover;" />
    </div>
    <p><small>Fonte: <a href="https://ric.com.br/cotidiano/uso-de-cartoes-de-debito-e-credito-para-pagar-passagem-de-onibus-e-limitado/">RIC</a></small></p>
  </div>
</div>
---
<img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/65fd6028d1421fec0e0f6603772cf69ee0cdf6b8/static/presentation_media/cidade_comunicam.svg" alt="cidades_comunicando" width="700"/>

> As futuras cidades inteligentes exigirão uma `infraestrutura de TIC unificada` para compartilhar adequadamente seus recursos, em vez de depender de soluções não integradas (<a target="_blank" href="https://www.researchgate.net/publication/261430626_Civitas_The_Smart_City_Middleware_from_Sensors_to_Big_Data">Villanueva et al., 2013</a>)
---
A plataforma `InterSCity` é um projeto open source que oferece APIs de alto nível para apoiar projetos de Cidades Inteligentes.

<span class="fragment" data-fragment-index="0">Dispositivos IoT e aplicações poderão compartilhar dados e instruções de forma padronizada.</span>
---
## Princípios de Design:

- `Modularidade através de microsserviços:`
<span class="fragment" data-fragment-index="0">Serviços pequenos e independentes que colaboram de forma leve para atingir objetivos em comum;</span>

- `Dados Distribuídos:`
<span class="fragment" data-fragment-index="1">Cada microsserviço gerencia seu próprio banco de dados e modelos;</span>

- `Adoção de Padrões Abertos:`
<span class="fragment" data-fragment-index="2">Uso de padrões abertos para garantir `interoperabilidade` e evitar dependência de fornecedores.</span>
---
## ABSTRAÇÃO DA REALIDADE

- <span class="fragment" data-fragment-index="0">**Recursos:** a entidade física ou espaço da cidade (como carros e semáforos) abstraída em um conceito lógico para o sistema.</span>

- <span class="fragment" data-fragment-index="1">**Capacidades:** as funcionalidades desses recursos, que podem ser sensores (para prover dados) ou atuadores (para receber comandos).</span>

---
## EXEMPLO
> Suponha que cada hospital de São Paulo gere os seguintes dados em tempo real: capacidade atual e número de pacientes.

> Podemos considerar os hospitais como um **recurso** com duas **capacidades**: "capacidade_atual" e "número_de_pacientes"
---
## ARQUITETURA
<img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/refs/heads/main/static/presentation_media/arquitetura.png" alt="drawing" width="700"/>
<p><small>Visão geral da arquitetura. Acesse uma explicação detalhada abaixo.</small></p>
--
## ARQUITETURA
<img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/refs/heads/main/static/presentation_media/arquitetura_cropped_t.png" alt="drawing" width="700"/>

`Resource Catalog`: catálogo central que mantém informações estáticas sobre recursos e capacidades
--
## ARQUITETURA
<img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/refs/heads/main/static/presentation_media/arquitetura_cropped_b.png" alt="drawing" width="700"/>

`Resource Adaptor`: ponto único de contato para os Gateways IoT: envio de dados sensoriais ou assinatura de comandos
--
## ARQUITETURA
<img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/refs/heads/main/static/presentation_media/arquitetura_cropped_t.png" alt="drawing" width="700"/>

`Data Collector`: armazena os dados coletados pelo **adaptor** e os disponibiliza com uma variedade de filtros
--
## ARQUITETURA
<img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/refs/heads/main/static/presentation_media/arquitetura_cropped_t.png" alt="drawing" width="700"/>

`Resource Discovery`: provê filtros para a descoberta de recursos

--
<!-- .slide: data-background-color="#f2f2f2" -->
## Criação de Recursos

<div style="display: flex; align-items: center; justify-content: space-between;">
  <div style="flex: 1; padding-right: 30px; text-align: justify;">
    <p>Os dispositivos físicos conectam-se ao Resource Adaptor, recebem um UUID e têm seus metadados enviados ao Resource Cataloguer para registro efetivo. Após salvar as informações, o Catálogo usa o RabbitMQ para avisar a plataforma sobre o novo dispositivo, notificando os serviços responsáveis por sensores ou atuadores.</p>
  </div>
  <div style="flex: 1; text-align: center;">
    <img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/refs/heads/main/static/presentation_media/resource_creation.png" alt="Arquitetura de Criação de Recursos" style="max-width: 100%; max-height: 400px;">
  </div>
</div>

--
<!-- .slide: data-background-color="#f2f2f2" -->
## Fluxo de Dados

<div style="display: flex; align-items: center; justify-content: space-between;">
  <div style="flex: 1; padding-right: 30px; text-align: justify;">
    <p>As novas leituras dos sensores são recebidas pelo Resource Adaptor, que as publica imediatamente no RabbitMQ. Microsserviços interessados escutam esse fluxo contínuo, como o Data Collector, que captura e salva tudo em um banco de dados histórico.</p>
  </div>
  <div style="flex: 1; text-align: center;">
    <img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/refs/heads/main/static/presentation_media/data_stream.png" alt="Arquitetura de Fluxo de Dados" style="max-width: 100%; max-height: 400px;">
  </div>
</div>

--
<!-- .slide: data-background-color="#f2f2f2" -->
## Descoberta e Visualização

<div style="display: flex; align-items: center; justify-content: space-between;">
  <div style="flex: 1; padding-right: 30px; text-align: justify;">
    <p>Aplicações e administradores usam o Resource Discovery e o Resource Viewer para buscar e monitorar os dispositivos na cidade. Para montar essa visão, essas ferramentas unem os dados estáticos fornecidos pelo Catálogo com as leituras em tempo real entregues pelo Data Collector.</p>
  </div>
  <div style="flex: 1; text-align: center;">
    <img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/refs/heads/main/static/presentation_media/resource_discovery_viewer.png" alt="Arquitetura de Descoberta e Visualização" style="max-width: 100%; max-height: 400px;">
  </div>
</div>
---
Explore e teste os serviços do `InterSCity` nas outras páginas deste site 🙂
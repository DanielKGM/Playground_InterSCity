<img src="https://interscity.org/wp-content/themes/inct/assets/img/logo/interscity.svg" alt="drawing" width="2000"/>

Plataforma de Cidades Inteligentes
---
## O que é uma cidade inteligente?

> Um lugar onde `soluções digitais` otimizam `serviços e redes tradicionais`, beneficiando seus habitantes e negócios (<a target="_blank" href="https://commission.europa.eu/eu-regional-and-urban-development/topics/cities-and-urban-development/city-initiatives/smart-cities_en">Comissão Européia</a>)
--
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <div style="text-align: top; width: 50%;">
    <h3>Serviço: Transportes Públicos</h3>
    <div style="width: 100%; height: 400px; overflow: hidden;">
      <img src="https://static.portaldaindustria.com.br/portaldaindustria/noticias/media/imagem_plugin/onibus_443znIY.jpg" 
           alt="Serviços Tradicionais" 
           style="width: 100%; height: 100%; object-fit: cover;" />
    </div>
    <p><small>Fonte: <a href="https://noticias.portaldaindustria.com.br/noticias/infraestrutura/reducao-da-tarifa-e-do-tempo-de-espera-incentivariam-uso-do-transporte-publico/">Portal da Industria</a></small></p>
  </div>
  <div style="text-align: top; width: 50%;">
    <h3>Solução: Rede Digital Integrada</h3>
    <div style="width: 100%; height: 400px; overflow: hidden;">
      <img src="https://static.ric.com.br/uploads/2024/02/cartao-uso-limitado-onibus-8-600x600.jpg" 
           alt="Soluções Digitais" 
           style="width: 100%; height: 100%; object-fit: cover;" />
    </div>
    <p><small>Fonte: <a href="https://ric.com.br/cotidiano/uso-de-cartoes-de-debito-e-credito-para-pagar-passagem-de-onibus-e-limitado/">RIC</a></small></p>
  </div>
</div>
---
<img src="https://raw.githubusercontent.com/DanielKGM/Playground_InterSCity/2d6dfde6182629502fe5157d20a1d46641f7f875/static/presentation_media/cidade_comunicam.svg" alt="cidades_comunicando" width="700"/>

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
Nas cidades inteligentes, as "coisas" conectadas são modeladas como **recursos** e **capacidades**.

- <span class="fragment" data-fragment-index="0">**Recursos**: Dispositivos ou entidades físicas que fornecem dados ou realizam ações.</span>

- <span class="fragment" data-fragment-index="1">**Capacidades**: Funcionalidades dos recursos, podendo ser sensores (dados) ou atuadores (ações).</span>

---
## EXEMPLO
> Suponha que cada hospital de São Paulo gere os seguintes dados em tempo real: capacidade atual e número de pacientes.

> Podemos considerar os hospitais como um **recurso** com duas **capacidades**: "capacidade_atual" e "número_de_pacientes"
---
## ARQUITETURA
<img src="https://github.com/DanielKGM/Playground_InterSCity/blob/main/static/presentation_media/arquitetura.png?raw=true" alt="drawing" width="700"/>
--
## ARQUITETURA
<img src="https://github.com/DanielKGM/Playground_InterSCity/blob/main/static/presentation_media/arquitetura_cropped_t.png?raw=true" alt="drawing" width="700"/>

`Resource Catalog`: catálogo central que mantém informações estáticas sobre recursos e capacidades
--
## ARQUITETURA
<img src="https://github.com/DanielKGM/Playground_InterSCity/blob/main/static/presentation_media/arquitetura_cropped_b.png?raw=true" alt="drawing" width="700"/>

`Resource Adaptor`: ponto único de contato para os Gateways IoT: envio de dados sensoriais ou assinatura de comandos
--
## ARQUITETURA
<img src="https://github.com/DanielKGM/Playground_InterSCity/blob/main/static/presentation_media/arquitetura_cropped_t.png?raw=true" alt="drawing" width="700"/>

`Data Collector`: armazena os dados sensoriais coletados pelo **adaptor** e os disponibiliza com um variedade de filtros
--
## ARQUITETURA
<img src="https://github.com/DanielKGM/Playground_InterSCity/blob/main/static/presentation_media/arquitetura_cropped_t.png?raw=true" alt="drawing" width="700"/>

`Resource Discovery`: provê filtros para a descoberta de recursos
---
Explore e teste os serviços do `InterSCity` nas outras páginas deste site 🙂
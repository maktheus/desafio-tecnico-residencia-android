# -*- coding: utf-8 -*-
"""
Gerador Completo da Documentação e do PDF Oficial do Desafio Técnico.
Residência Tecnológica em Sistemas Android Avançados, IA & Eficiência Energética.
"""

import os
import subprocess
import pypdf

# -----------------------------------------------------------------------------
# 1. CONTEÚDO HTML COM DESIGN EDITORIAL MODERNO
# -----------------------------------------------------------------------------

HTML_CONTENT = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Desafio Técnico de Admissão - Residência Tecnológica Android</title>
<style>
  @page {
    size: A4 portrait;
    margin: 14mm 12mm 14mm 12mm;
    @bottom-right {
      content: "Página " counter(page) " de " counter(pages);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-size: 8pt;
      color: #64748b;
    }
    @bottom-left {
      content: "Residência Tecnológica Android Avançado &bull; Desafio Técnico Oficial";
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-size: 8pt;
      color: #64748b;
    }
  }

  *, *:before, *:after {
    box-sizing: border-box;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.4;
    font-size: 8.5pt;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }

  /* Capa / Banner Principal */
  .banner {
    background: linear-gradient(135deg, #091325 0%, #172554 50%, #1d4ed8 100%);
    color: #ffffff;
    padding: 12px 18px;
    border-radius: 8px;
    margin-bottom: 8px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  }

  .banner-tag {
    display: inline-block;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: #bfdbfe;
    font-size: 7.2pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 2px 7px;
    border-radius: 4px;
    margin-bottom: 5px;
  }

  .banner h1 {
    font-size: 15pt;
    font-weight: 800;
    line-height: 1.2;
    margin: 0 0 4px 0;
    color: #ffffff;
    border: none;
    padding: 0;
  }

  .banner h1::before {
    display: none;
  }

  .banner-sub {
    font-size: 9.2pt;
    font-weight: 400;
    color: #dbeafe;
    margin: 0 0 8px 0;
    line-height: 1.35;
  }

  .meta-table {
    display: table;
    width: 100%;
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    padding-top: 5px;
    margin-top: 2px;
  }

  .meta-col {
    display: table-cell;
    width: 25%;
    font-size: 7.2pt;
    color: #ffffff;
    vertical-align: top;
  }

  .meta-col strong {
    display: block;
    color: #93c5fd;
    text-transform: uppercase;
    font-size: 6.8pt;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }

  /* Títulos */
  h1 {
    font-size: 11.8pt;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 4px;
    margin-top: 14px;
    margin-bottom: 7px;
    display: flex;
    align-items: center;
    break-after: avoid;
  }

  h1::before {
    content: "";
    display: inline-block;
    width: 5px;
    height: 14px;
    background-color: #2563eb;
    margin-right: 6px;
    border-radius: 2px;
  }

  h2 {
    font-size: 10pt;
    font-weight: 700;
    color: #1e3a8a;
    margin-top: 11px;
    margin-bottom: 4px;
    break-after: avoid;
  }

  h3 {
    font-size: 9pt;
    font-weight: 600;
    color: #334155;
    margin-top: 8px;
    margin-bottom: 3px;
    break-after: avoid;
  }

  p {
    margin-top: 0;
    margin-bottom: 5px;
    text-align: justify;
  }

  ul, ol {
    margin-top: 0;
    margin-bottom: 6px;
    padding-left: 18px;
  }

  li {
    margin-bottom: 2.5px;
  }

  /* Callouts */
  .callout {
    border-radius: 6px;
    padding: 7px 11px;
    margin: 4px 0;
    font-size: 8.2pt;
    break-inside: avoid;
  }

  .callout-info {
    background-color: #eff6ff;
    border-left: 4px solid #2563eb;
    color: #1e40af;
  }

  .callout-success {
    background-color: #f0fdf4;
    border-left: 4px solid #16a34a;
    color: #166534;
  }

  .callout-warning {
    background-color: #fffbeb;
    border-left: 4px solid #d97706;
    color: #92400e;
  }

  .callout-title {
    font-weight: 700;
    margin-bottom: 2px;
    display: block;
    font-size: 8.6pt;
  }

  /* Tabelas */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 4px 0;
    font-size: 7.9pt;
    break-inside: avoid;
  }

  th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    text-align: left;
    padding: 5px 7px;
    border-bottom: 2px solid #cbd5e1;
    border-top: 1px solid #cbd5e1;
  }

  td {
    padding: 4px 7px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
  }

  tr:nth-child(even) td {
    background-color: #f8fafc;
  }

  /* Badges */
  .badge {
    display: inline-block;
    padding: 1.5px 5px;
    font-size: 6.8pt;
    font-weight: 600;
    border-radius: 3px;
    text-transform: uppercase;
  }

  .badge-blue { background: #dbeafe; color: #1e40af; }
  .badge-green { background: #dcfce7; color: #15803d; }
  .badge-purple { background: #f3e8ff; color: #6b21a8; }
  .badge-amber { background: #fef3c7; color: #b45309; }

  /* Códigos */
  code {
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 7.7pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 3px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
  }

  pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 7px 11px;
    border-radius: 5px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 7.4pt;
    line-height: 1.3;
    margin: 5px 0;
    break-inside: avoid;
  }

  pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
    border: none;
  }

  /* Caixas de Trilha */
  .track-box {
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 8px 12px;
    margin-bottom: 8px;
    background: #ffffff;
    break-inside: avoid;
  }

  .track-header {
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
    margin-bottom: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .track-title {
    font-size: 9.6pt;
    font-weight: 700;
    color: #1e3a8a;
    margin: 0;
  }

  .avoid-break {
    break-inside: avoid;
  }

  .page-break {
    break-before: page;
  }

  .diagram-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 5px;
    margin: 4px 0;
    text-align: center;
    font-family: 'Consolas', monospace;
    font-size: 7.4pt;
    color: #334155;
    break-inside: avoid;
    line-height: 1.25;
  }
</style>
</head>
<body>

  <!-- ==================== PÁGINA 1 ==================== -->
  <!-- BANNER PRINCIPAL / CAPA -->
  <div class="banner">
    <div class="banner-tag">Processo Seletivo &bull; Ciclo 2026/2027 &bull; Edital Oficial</div>
    <h1>Programa de Residência Tecnológica em Sistemas Android Avançados</h1>
    <div class="banner-sub">
      Desafio Técnico de Admissão, Nivelamento e Rastreabilidade Experimental<br>
      <strong>Projeto Alvo:</strong> <em>Android Sentinel Core &bull; Telemetria, IA On-Device e Otimização Energética</em>
    </div>
    
    <div class="meta-table">
      <div class="meta-col">
        <strong>Carga Curricular</strong>
        285h (210h Núcleo + 75h Trilha)
      </div>
      <div class="meta-col">
        <strong>Modalidade de Avaliação</strong>
        Código Aberto + Relatório Técnico
      </div>
      <div class="meta-col">
        <strong>Regime de Execução</strong>
        Individual &bull; Autônomo
      </div>
      <div class="meta-col">
        <strong>Pontuação Total</strong>
        100 Pontos (Classificatório)
      </div>
    </div>
  </div>

  <!-- SEÇÃO 1: APRESENTAÇÃO E MATRIZ PEDAGÓGICA -->
  <h1>1. Apresentação do Programa e Alinhamento Pedagógico</h1>
  <p>
    O <strong>Programa de Residência Tecnológica em Sistemas Android Avançados</strong> é uma imersão técnico-científica voltada para a formação de engenheiros e pesquisadores capazes de atuar no estado da arte do sistema operacional Android e do Android Open Source Project (AOSP). O currículo compõe-se de um <strong>Núcleo Comum de 210h</strong> somado a <strong>75h de Formação Especializada</strong> em uma de três trilhas tecnológicas.
  </p>
  <p>
    O objetivo deste desafio técnico é avaliar competências que abrangem desde a arquitetura limpa de código até o rigor de formulação científica e rastreabilidade de evidências. A tabela a seguir estabelece a rastreabilidade direta entre o conteúdo formativo do programa e os itens avaliados neste edital:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 32%;">Disciplina do Programa</th>
        <th style="width: 12%;">Carga</th>
        <th style="width: 26%;">Competência Alvo</th>
        <th>Item Correspondente no Desafio</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Dados, Experimentação e Metodologia Científica</strong></td>
        <td>30h</td>
        <td>Hipóteses, desenho experimental, métricas e evidências.</td>
        <td>Parte 3: Relatório Científico ($H_0$ vs $H_1$, gráficos, tabelas e validade).</td>
      </tr>
      <tr>
        <td><strong>Engenharia de Software, Requisitos e Gestão</strong></td>
        <td>24h</td>
        <td>Requisitos funcionais, ágil, rastreabilidade e Git.</td>
        <td>Parte 1: Commits semânticos, issues, README e modularidade.</td>
      </tr>
      <tr>
        <td><strong>Metodologia de Projetos, Ética e Soft Skills</strong></td>
        <td>30h</td>
        <td>PBL, ética profissional, proteção de dados e transparência.</td>
        <td>Declaração de uso de IA, licenças, conformidade e clareza documental.</td>
      </tr>
      <tr>
        <td><strong>Arquitetura de Software</strong></td>
        <td>18h</td>
        <td>Clean Architecture, SOLID, desacoplamento e testabilidade.</td>
        <td>Parte 1: Camadas <code>domain</code>, <code>data</code>, <code>presentation</code> e DIP.</td>
      </tr>
      <tr>
        <td><strong>Inteligência Artificial: Fundamentos e Frameworks</strong></td>
        <td>36h</td>
        <td>Modelos, métricas, overfitting e inferência on-device.</td>
        <td>Parte 1 (Conceitos) e <strong>Trilha 1</strong> (Pipeline de treino e TFLite).</td>
      </tr>
      <tr>
        <td><strong>Programação Java/Kotlin e Android</strong></td>
        <td>42h</td>
        <td>Kotlin idiomático, Coroutines, Flow, Room e Compose.</td>
        <td>Parte 1: App funcional, observabilidade reativa e banco de dados.</td>
      </tr>
      <tr>
        <td><strong>Testes, Automação, Segurança e CI/CD</strong></td>
        <td>30h</td>
        <td>Testes unitários, automação, GitHub Actions e LGPD.</td>
        <td>Parte 1: Suíte JUnit/MockK, pipeline CI e <strong>Trilha 2</strong> (Segurança).</td>
      </tr>
      <tr>
        <td><strong>Trilhas Especializadas (Módulos 2, 3 ou 4)</strong></td>
        <td>75h</td>
        <td>Aprofundamento em IA, Cibersegurança ou Eficiência.</td>
        <td>Parte 2: Escolha de 1 trilha aplicada correspondente à vaga pretendida.</td>
      </tr>
    </tbody>
  </table>

  <!-- SEÇÃO 2: VISÃO GERAL DO PROJETO -->
  <h1>2. Visão Geral do Desafio: Projeto "Android Sentinel Core"</h1>
  <p>
    Dispositivos móveis modernos operam em ambientes complexos onde múltiplas aplicações concorrem por tempo de CPU, ciclos de GPU/NPU, memória RAM e orçamento energético restrito. O candidato deverá desenvolver o <strong>Android Sentinel Core</strong>, uma solução enxuta que monitora a integridade do dispositivo, detecta anomalias de execução e otimiza o uso de recursos.
  </p>

  <div class="diagram-box">
    [ Sensores de Hardware & AOSP ] &rarr; ( Coletor / Provedor de Telemetria )<br>
    &darr;<br>
    [ Data Layer: Room DB / Cache / Mock Dataset ] &larr; ( Repositório de Telemetria )<br>
    &darr;<br>
    [ Domain Layer: MonitorSystemHealthUseCase & AnomalyEvaluator (Kotlin Puro) ]<br>
    &swarr; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &searr;<br>
    [ Presentation: ViewModels + Jetpack Compose ] &nbsp;&nbsp;&nbsp;&nbsp; [ Módulo Especializado: IA / Sec / Energy ]
  </div>

  <p>O desafio está estruturado em três blocos objetivos de avaliação:</p>
  <ul>
    <li><strong>Parte 1 – Núcleo Comum Obrigatório (50 Pontos):</strong> Engenharia de software, arquitetura limpa em Kotlin, app Android reativo com persistência e pipeline de testes/CI.</li>
    <li><strong>Parte 2 – Módulo Especializado da Trilha Escolhida (30 Pontos):</strong> O candidato seleciona e implementa <strong>apenas uma</strong> das três trilhas (Trilha 1: IA; Trilha 2: Segurança; Trilha 3: Eficiência Energética).</li>
    <li><strong>Parte 3 – Relatório Técnico-Científico e Rastreabilidade (20 Pontos):</strong> Documento experimental obrigatório em formato de artigo técnico com formulação de hipótese e dados empíricos.</li>
  </ul>

  <!-- ==================== PÁGINA 2 ==================== -->
  <div class="page-break"></div>
  <!-- SEÇÃO 3: PARTE 1 - NÚCLEO COMUM -->
  <h1>3. Especificação da Parte 1: Módulo Obrigatório (Núcleo Comum)</h1>
  <p>
    Todos os candidatos devem implementar a aplicação base em Kotlin (Android API 26+), estruturada com foco em manutenibilidade, testabilidade e baixo consumo de recursos computacionais.
  </p>

  <h2>3.1 Arquitetura e Engenharia de Software (15 Pontos)</h2>
  <ul>
    <li><strong>Clean Architecture:</strong> O projeto deve respeitar a separação formal em três camadas:
      <br>&bull; <code>domain</code>: Entidades de negócio (ex.: <code>TelemetrySnapshot</code>) e Casos de Uso (ex.: <code>MonitorSystemHealthUseCase</code>, <code>RecordAnomalyUseCase</code>) totalmente independentes do SDK Android.
      <br>&bull; <code>data</code>: Implementação de repositórios, Data Access Objects (Room DAO) e provedores de leitura de hardware/sensores.
      <br>&bull; <code>presentation</code>: ViewModels gerenciando estados de UI através de <code>StateFlow</code> ou <code>SharedFlow</code>, conectados a uma interface declarativa em <strong>Jetpack Compose</strong> (ou Views tradicionais com ViewBinding).
    </li>
    <li><strong>Inversão de Dependências (DIP):</strong> A camada de apresentação e os casos de uso devem depender exclusivamente de interfaces/abstrações, não de implementações concretas (utilize Hilt, Koin ou injeção manual limpa).</li>
    <li><strong>Concorrência Estruturada:</strong> Utilização idiomática de <strong>Kotlin Coroutines</strong> com despacho correto de threads (<code>Dispatchers.IO</code> para I/O e banco, <code>Dispatchers.Default</code> para processamento e <code>Dispatchers.Main</code> para UI).</li>
  </ul>

  <h2>3.2 Coleta de Telemetria e Persistência Local (15 Pontos)</h2>
  <ul>
    <li><strong>Mecanismo de Coleta em Tempo Real:</strong> Implementar rotina assíncrona periódica (ex.: a cada 5 ou 10 segundos) que capture:
      <br>&bull; <em>Uso de CPU:</em> Carga percentual instantânea (global ou por processo) via <code>/proc/stat</code>, <code>ActivityManager</code> ou dados do Mock Dataset.
      <br>&bull; <em>Memória RAM:</em> Memória utilizada (MB), memória livre (MB) e flag indicativa de pressão de memória (<code>isLowMemory</code>).
      <br>&bull; <em>Bateria & Térmico:</em> Nível da bateria (%), temperatura (&deg;C), voltagem (mV) e status de carregamento via <code>BatteryManager</code>.
      <br>&bull; <em>Rede:</em> Tipo de conexão (Wi-Fi, Dados Móveis) e contadores de tráfego (bytes RX e TX).
    </li>
    <li><strong>Persistência Local:</strong> Armazenamento local com <strong>Room Database</strong> ou <strong>DataStore</strong>, permitindo consultas históricas ordenadas por timestamp e retenção dos últimos 500 registros.</li>
    <li><strong>Modo Dataset Sintético (Offline Mock):</strong> O sistema <strong>deve</strong> conter uma flag ou seletor de fonte de dados permitindo carregar o arquivo <code>starter_kit/mock_telemetry_dataset.json</code> emulando a telemetria, assegurando que o app seja 100% testável em qualquer máquina de avaliação.</li>
  </ul>

  <h2>3.3 Testes Automatizados e Pipeline de CI/CD (20 Pontos)</h2>
  <ul>
    <li><strong>Testes Unitários:</strong> Escrever suíte de testes com <strong>JUnit</strong> e <strong>MockK</strong> cobrindo os UseCases de domínio e repositórios. Devem ser validadas regras de negócio como detecção de limites críticos (ex.: alerta quando CPU > 85% ou temperatura > 40&deg;C) e fluxo correto de exceções.</li>
    <li><strong>Pipeline de Integração Contínua:</strong> Fornecer um arquivo <code>.github/workflows/ci.yml</code> funcional que execute a cada <code>push</code> ou <code>pull_request</code>:
      <br>1. Análise estática de código (ktlint, detekt ou android lint).
      <br>2. Compilação do projeto (<code>./gradlew assembleDebug</code>).
      <br>3. Execução automatizada dos testes unitários (<code>./gradlew testDebugUnitTest</code>) com publicação do relatório de testes.
    </li>
  </ul>

  <div class="callout callout-info">
    <span class="callout-title">Contrato de Código Fornecido</span>
    Consulte o arquivo <code>starter_kit/ArchitectureSample.kt</code> no repositório para inspecionar os contratos recomendados para as entidades de telemetria, Casos de Uso e interfaces das três trilhas especializadas.
  </div>

  <!-- ==================== PÁGINA 3 ==================== -->
  <div class="page-break"></div>
  <!-- SEÇÃO 4: PARTE 2 - TRILHAS ESPECÍFICAS (TRILHA 1 & TRILHA 2) -->
  <h1>4. Especificação da Parte 2: Módulos Especializados (Escolha 1 Trilha)</h1>
  <p>
    O candidato deve optar por <strong>uma única trilha</strong>. Não é necessário implementar as três; a avaliação valoriza profundidade técnica, rigor experimental e qualidade da entrega no escopo selecionado.
  </p>

  <!-- TRILHA 1 -->
  <div class="track-box">
    <div class="track-header">
      <h2 class="track-title">Trilha 1: Inteligência Artificial aplicada à Otimização de Sistemas Android</h2>
      <span class="badge badge-purple">Especialização IA (30 Pts)</span>
    </div>
    <p><strong>Contexto:</strong> O AOSP gera fluxos contínuos de métricas. Identificar comportamentos degenerativos (loops infinitos, vazamentos progressivos de memória e estrangulamento térmico) antes do encerramento forçado do processo exige modelos preditivos ultraleves executados localmente no dispositivo (on-device).</p>
    <p><strong>Entregáveis Objetivos da Trilha:</strong></p>
    <ol>
      <li><strong>Notebook / Script de Treinamento:</strong> Utilizando o script auxiliar <code>starter_kit/baseline_evaluator.py</code> e o dataset fornecido, desenvolva em Python um script ou notebook realizando a normalização dos atributos e o treinamento de um modelo para <strong>Detecção de Anomalias</strong> ou <strong>Classificação de Estado</strong>.</li>
      <li><strong>Estudo Comparativo:</strong> Compare tecnicamente ao menos duas técnicas (ex.: <em>Isolation Forest</em> vs <em>Regressão Logística</em> ou <em>Random Forest</em>). Apresente métricas formais: Matriz de Confusão, Acurácia, Precisão, Recall e F1-Score.</li>
      <li><strong>Otimização On-Device & Quantização:</strong> Exporte o modelo final para o formato <strong>TensorFlow Lite (<code>.tflite</code>)</strong> ou <strong>ONNX Runtime Mobile</strong>. Analise a redução no tamanho do artefato e a estimativa de latência de inferência no dispositivo.</li>
      <li><strong>Integração na Aplicação:</strong> Implemente na camada <code>data/domain</code> do Android Sentinel a classe consumidora do modelo (conforme contrato <code>OnDeviceAnomalyClassifier</code>), emitindo alertas preditivos na interface quando a probabilidade de anomalia superar o limiar estipulado.</li>
    </ol>
  </div>

  <!-- TRILHA 2 -->
  <div class="track-box">
    <div class="track-header">
      <h2 class="track-title">Trilha 2: Segurança de Dispositivos Móveis e Automação de Validações</h2>
      <span class="badge badge-blue">Especialização Segurança (30 Pts)</span>
    </div>
    <p><strong>Contexto:</strong> A arquitetura de segurança do Android apoia-se em sandboxes, permissões declaradas e isolamento de processos (SELinux). Configurações equivocadas no <code>AndroidManifest.xml</code> ou comunicação insegura via Binder/IPC abrem brechas para elevação de privilégios e vazamento de dados.</p>
    <p><strong>Entregáveis Objetivos da Trilha:</strong></p>
    <ol>
      <li><strong>Modelagem de Ameaças (STRIDE & OWASP MASVS):</strong> Elabore uma matriz detalhada de modelagem de ameaças para o aplicativo utilizando as categorias do <strong>STRIDE</strong> (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege) e correlacionando-as aos requisitos do <strong>OWASP MASVS v2.0</strong> (MASVS-STORAGE, MASVS-CRYPTO, MASVS-PLATFORM, MASVS-NETWORK).</li>
      <li><strong>Auditoria de Código & Análise de Vulnerabilidades:</strong> Identifique, documente e apresente código corrigido (hardening) para ao menos <strong>quatro vulnerabilidades clássicas</strong> no ecossistema Android:
        <br>&bull; Componente IPC exposto sem permissão (<code>android:exported="true"</code>).
        <br>&bull; Armazenamento inseguro de dados sensíveis (SharedPreferences em texto claro vs <code>EncryptedSharedPreferences</code>).
        <br>&bull; Falta de validação de canal TLS / Ausência de Certificate Pinning.
        <br>&bull; Emissão de dados sensíveis ou tokens em logs do sistema (Logcat em builds de release).
      </li>
      <li><strong>Script Automatizado de Verificação de Segurança:</strong> Desenvolva um script (em Python, Bash ou teste automatizado Android) que inspecione de forma determinística o APK ou dispositivo via ADB, verificando flags de compilação (<code>android:allowBackup</code>, <code>android:debuggable</code>, permissões concedidas) e emitindo um relatório automatizado com status de conformidade (Pass/Fail).</li>
    </ol>
  </div>

  <!-- ==================== PÁGINA 4 ==================== -->
  <div class="page-break"></div>
  <!-- TRILHA 3 -->
  <div class="track-box">
    <div class="track-header">
      <h2 class="track-title">Trilha 3: Eficiência Energética avaliada por Algoritmos de Otimização</h2>
      <span class="badge badge-amber">Especialização Energia (30 Pts)</span>
    </div>
    <p><strong>Contexto:</strong> A sincronização de dados e o processamento em background respondem pela maior fatia do consumo indesejado de bateria no Android. WakeLocks não liberados e frequências excessivas de polling impedem os núcleos de CPU de entrarem em estados de baixo consumo (Doze Mode / C-States).</p>
    <p><strong>Entregáveis Objetivos da Trilha:</strong></p>
    <ol>
      <li><strong>Protocolo Experimental de Medição Energética:</strong> Formule um protocolo consistente para mensurar o impacto do envio de telemetria sob diferentes cenários de uso (sincronização síncrona a cada 5s vs envio em lotes a cada 5 minutos; Wi-Fi vs Dados Móveis 5G; tela ligada vs Doze Mode).</li>
      <li><strong>Modelagem Matemática do Custo Energético:</strong> Formule analiticamente uma função objetivo multiobjetivo que quantifique o trade-off entre energia, atraso de entrega e risco de perda de telemetria:
        <br><code>Minimizar: Custo(P) = w1 &times; E(Energia_mA) + w2 &times; L(Latencia_s) + w3 &times; D(Perda_%)</code>
        <br>Sujeito a: restrições de nível crítico de bateria (&lt; 15%) e estado de repouso do sistema.
      </li>
      <li><strong>Algoritmo de Otimização Heurística:</strong> Implemente em Kotlin ou Python um algoritmo de busca heurística (ex.: <em>Algoritmo Genético</em>, <em>Simulated Annealing</em> ou <em>Heurística Gulosa Adaptativa</em>) que selecione dinamicamente a melhor janela de transmissão e tamanho de lote com base nas restrições energéticas atuais.</li>
      <li><strong>Validação e Redução Comprovada:</strong> Demonstre numericamente, utilizando as medições do <code>baseline_evaluator.py</code> ou dados via <code>dumpsys batterystats</code>, o ganho percentual de eficiência energética da abordagem otimizada em comparação à abordagem ingênua (unbuffered polling).</li>
    </ol>
  </div>

  <!-- SEÇÃO 5: RELATÓRIO CIENTÍFICO -->
  <h1>5. Especificação da Parte 3: Relatório Técnico-Científico (20 Pontos)</h1>
  <p>
    O relatório técnico-científico consolida o perfil investigativo exigido pelo programa. O candidato deve preencher e entregar o documento no formato do template oficial fornecido em <code>starter_kit/TEMPLATE_RELATORIO_TECNICO.md</code> (2 a 4 páginas de extensão).
  </p>

  <div class="callout callout-info">
    <span class="callout-title">Roteiro Mandatório do Relatório Técnico</span>
    <ol style="margin-bottom: 0;">
      <li><strong>Resumo Executivo (Abstract):</strong> Síntese de 100 a 150 palavras cobrindo motivação, hipótese, metodologia, dados quantitativos e conclusão.</li>
      <li><strong>Formulação de Hipótese:</strong>
        <br>&bull; <em>Hipótese Nula ($H_0$):</em> A intervenção proposta (algoritmo de otimização / modelo de IA / correção de segurança) não altera significativamente o comportamento ou a eficiência do sistema móvel.
        <br>&bull; <em>Hipótese Alternativa ($H_1$):</em> A intervenção produz melhora estatisticamente observável ($\Delta \ge 25\%$) em consumo, latência ou resiliência.
      </li>
      <li><strong>Desenho Experimental:</strong> Definição explícita das variáveis independentes (políticas/configurações testadas), variáveis dependentes (métricas de medição) e variáveis de controle (dispositivo, versão de SO, temperatura ambiente).</li>
      <li><strong>Resultados e Evidências Empíricas:</strong> Tabela comparativa e gráficos demonstrando o comportamento do sistema antes e depois da intervenção (apoiando-se nos valores extraídos pelo <code>baseline_evaluator.py</code>).</li>
      <li><strong>Ameaças à Validade & Limitações:</strong> Identificação honesta de limitações do teste (ruído em emuladores, generalização entre fabricantes de SoC, variações térmicas externas).</li>
      <li><strong>Rastreabilidade de Código:</strong> Apontamento direto dos hashes de commit e arquivos que suportam as conclusões apresentadas.</li>
    </ol>
  </div>

  <!-- ==================== PÁGINA 5 ==================== -->
  <div class="page-break"></div>
  <!-- SEÇÃO 6: MATRIZ DE AVALIAÇÃO -->
  <h1>6. Matriz e Rubrica Detalhada de Avaliação (0 a 100 Pontos)</h1>
  <p>
    A banca examinadora adotará critérios objetivos e pontuações padronizadas conforme a matriz abaixo:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 24%;">Critério Avaliado</th>
        <th style="width: 10%;">Peso</th>
        <th style="width: 36%;">Indicadores de Nível Excelente (Nota Máxima)</th>
        <th style="width: 30%;">Penalidades & Não Conformidades</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Arquitetura & Qualidade de Código</strong></td>
        <td><strong>20 pts</strong></td>
        <td>Separação estrita em camadas (Domain/Data/Presentation); princípios SOLID aplicados com naturalidade; injeção de dependência funcional; tratamento não bloqueante com Coroutines/Flow.</td>
        <td>Lógica de negócio acoplada na View/Activity; dependência de classes Android no Domain; código não formatado (-10 pts).</td>
      </tr>
      <tr>
        <td><strong>2. Implementação Android Core</strong></td>
        <td><strong>20 pts</strong></td>
        <td>Coleta funcional de telemetria (CPU, RAM, bateria, rede); persistência com Room/DataStore; UI declarativa reativa (Compose); alternador para dados sintéticos do Mock Dataset.</td>
        <td>App sofre crash em execução; ausência de persistência local; interface gráfica congela por bloqueio da Main Thread (-12 pts).</td>
      </tr>
      <tr>
        <td><strong>3. Testes Automatizados & CI</strong></td>
        <td><strong>15 pts</strong></td>
        <td>Testes unitários cobrindo casos felizes e cenários de borda dos UseCases e Repositórios; workflow do GitHub Actions rodando lint, build e testes com sucesso.</td>
        <td>Ausência de testes unitários (-10 pts); pipeline de CI ausente ou falhando (-5 pts).</td>
      </tr>
      <tr>
        <td><strong>4. Desafio da Trilha Especializada</strong></td>
        <td><strong>25 pts</strong></td>
        <td>Entrega integral dos requisitos da trilha escolhida (IA: modelo treinado, métricas e on-device; Sec: STRIDE, MASVS e script; Energia: modelo multiobjetivo e algoritmo heurístico).</td>
        <td>Trilha não implementada ou com código meramente ilustrativo sem comprovação prática (-15 a -25 pts).</td>
      </tr>
      <tr>
        <td><strong>5. Relatório Técnico & Rastreabilidade</strong></td>
        <td><strong>20 pts</strong></td>
        <td>Hipótese clara ($H_0$ vs $H_1$); dados quantitativos com gráficos e tabelas; discussão de ameaças à validade; histórico Git semântico com commits rastreáveis.</td>
        <td>Relatório vago sem evidências numéricas (-10 pts); commit único "first commit" demonstrando falta de processo (-8 pts).</td>
      </tr>
    </tbody>
  </table>

  <!-- ==================== PÁGINA 6 ==================== -->
  <div class="page-break"></div>
  <!-- SEÇÃO 7: BASE PARA O CANDIDATO -->
  <h1>7. A Base de Apoio para o Candidato ("Starter Kit" e Recursos)</h1>
  <p>
    Para eliminar barreiras de infraestrutura e garantir produtividade imediata, este repositório disponibiliza uma base completa de artefatos pré-configurados:
  </p>

  <h2>7.1 O Dataset Sintético de Telemetria (<code>starter_kit/mock_telemetry_dataset.json</code>)</h2>
  <p>
    O arquivo JSON fornecido contém 120 leituras temporais amostradas a cada 10 segundos (20 minutos de histórico), cobrindo cinco regimes de estresse do sistema operacional Android:
  </p>
  <ul>
    <li><strong>Amostras 0 a 29 (Baseline Idle):</strong> Funcionamento em repouso com CPU estável entre 4% e 14% e corrente de -150 mA.</li>
    <li><strong>Amostras 30 a 49 (CPU Spike & Aquecimento Térmico):</strong> Carga de CPU sustentada acima de 85% e temperatura elevando-se até 42&deg;C (<em>cenário ideal para modelos preditivos da Trilha 1</em>).</li>
    <li><strong>Amostras 50 a 69 (Wakelock Leak & Tráfego de Rádio):</strong> WakeLock permanente impedindo o sono do dispositivo e tráfego massivo com corrente em -920 mA (<em>cenário ideal para otimização da Trilha 3</em>).</li>
    <li><strong>Amostras 70 a 89 (Inundação IPC & Anomalia de Segurança):</strong> Tentativas repetidas de acesso a componentes internos exportados sem assinatura (<em>cenário ideal para validações da Trilha 2</em>).</li>
    <li><strong>Amostras 90 a 119 (Doze Mode & Deep Sleep):</strong> Recuperação do sistema com transição para sono profundo e corrente contida em -65 mA.</li>
  </ul>

  <h2>7.2 Script Auxiliar de Baseline (<code>starter_kit/baseline_evaluator.py</code>)</h2>
  <p>
    Execute <code>python starter_kit/baseline_evaluator.py</code> para obter instantaneamente:
  </p>
  <pre><code>$ python starter_kit/baseline_evaluator.py
=================================================================
 ANDROID SENTINEL CORE - RELATÓRIO DA LINHA DE BASE (BASELINE)
=================================================================
 Amostras analisadas:      120 leituras | Período: 20.0 minutos
 Uso Médio de CPU:         32.19% (Pico: 99.5%)
 Temperatura Média:        32.75 °C (Pico: 41.5 °C)
 Corrente Média:           399.29 mA | Descarga Acumulada: 133.1 mAh
 Anomalias Registradas:    60 (50.0%)
=================================================================</code></pre>

  <h2>7.3 Diretrizes Éticas e Uso de Inteligência Artificial</h2>
  <div class="callout callout-warning">
    <span class="callout-title">Declaração de Transparência e Honestidade Intelectual</span>
    O uso de ferramentas de assistência baseadas em IA (Copilot, ChatGPT, Claude, Gemini) é <strong>permitido como ferramenta de suporte e produtividade</strong>. É <strong>obrigatório</strong> declarar no <code>README.md</code> quais ferramentas foram utilizadas e em quais etapas. Na etapa de arguição técnica, o candidato será avaliado individualmente quanto ao domínio integral da solução entregue.
  </div>

  <!-- SEÇÃO 8: INSTRUÇÕES DE SUBMISSÃO -->
  <h1>8. Instruções de Submissão e Checklist Final</h1>
  <ol>
    <li><strong>Repositório:</strong> Submeter o link de um repositório no GitHub ou GitLab contendo todo o código-fonte, branches e histórico de desenvolvimento.</li>
    <li><strong>Commits:</strong> Histórico de commits atômicos e descritivos seguindo a convenção <em>Conventional Commits</em> (<code>feat:</code>, <code>fix:</code>, <code>test:</code>, <code>docs:</code>, <code>refactor:</code>).</li>
    <li><strong>Documentação (README.md):</strong> Deve conter instruções claras de compilação, versão da JVM recomendada (Java 17), comandos de teste e a identificação da trilha escolhida.</li>
    <li><strong>Relatório Técnico:</strong> O relatório final (<code>RELATORIO_TECNICO.md</code> ou versão em PDF) deve estar comitado na raiz do repositório, com todas as seções preenchidas.</li>
  </ol>

  <!-- ==================== PÁGINA 7 ==================== -->
  <div class="page-break"></div>
  <!-- SEÇÃO 9: REFERÊNCIAS BIBLIOGRÁFICAS -->
  <h1>9. Bibliografia Canônica e Fontes Oficiais Recomendadas</h1>
  <p>Recomenda-se a fundamentação nas seguintes fontes oficiais consagradas na indústria e na academia:</p>

  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Tema</th>
        <th style="width: 38%;">Referência Canônica</th>
        <th>Endereço Eletrônico Oficial</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Arquitetura Android</strong></td>
        <td>Guide to App Architecture & Jetpack Modern Practices</td>
        <td><code>https://developer.android.com/topic/architecture</code></td>
      </tr>
      <tr>
        <td><strong>AOSP Internals</strong></td>
        <td>Android Open Source Project Architecture & Core Services</td>
        <td><code>https://source.android.com/docs/core</code></td>
      </tr>
      <tr>
        <td><strong>Cibersegurança Móvel</strong></td>
        <td>OWASP Mobile Application Security Verification Standard (MASVS v2.0)</td>
        <td><code>https://mas.owasp.org/MASVS/</code></td>
      </tr>
      <tr>
        <td><strong>Profiling de Desempenho</strong></td>
        <td>Perfetto: Modern System Profiling and Trace Analysis</td>
        <td><code>https://perfetto.dev/docs/</code></td>
      </tr>
      <tr>
        <td><strong>Eficiência Energética</strong></td>
        <td>Android Power Management, Battery Historian & Doze Mode</td>
        <td><code>https://developer.android.com/topic/performance/power</code></td>
      </tr>
      <tr>
        <td><strong>IA On-Device</strong></td>
        <td>TensorFlow Lite & Android Machine Learning Solutions</td>
        <td><code>https://www.tensorflow.org/lite/android</code></td>
      </tr>
      <tr>
        <td><strong>Qualidade de Software</strong></td>
        <td>Martin, Robert C. <em>Clean Architecture: A Craftsman's Guide</em></td>
        <td>Prentice Hall / Pearson Education</td>
      </tr>
    </tbody>
  </table>

  <div style="margin-top: 48px; text-align: center; border-top: 1px solid #cbd5e1; padding-top: 16px; font-size: 8.2pt; color: #64748b;">
    <strong>Coordenação Técnica do Programa de Residência Tecnológica em Sistemas Android Avançados</strong><br>
    Documento oficial de seleção técnica e nivelamento acadêmico &bull; Uso Institucional e de Candidatos &bull; Ciclo 2026/2027
  </div>

</body>
</html>
"""

# -----------------------------------------------------------------------------
# 2. CONTEÚDO EM MARKDOWN PARA O REPOSITÓRIO (DESAFIO_TECNICO.md)
# -----------------------------------------------------------------------------

MARKDOWN_CONTENT = r"""# Desafio Técnico de Admissão e Nivelamento
## Programa de Residência Tecnológica em Sistemas Android Avançados, IA & Eficiência Energética
**Ciclo 2026/2027 • Carga Horária do Programa: 285 Horas (210h Núcleo Comum + 75h Trilha Especializada)**

---

## 1. Apresentação e Contextualização do Programa

O **Programa de Residência Tecnológica em Sistemas Android Avançados** constitui uma jornada de excelência técnica e científica focada no ecossistema Android e no Android Open Source Project (AOSP). O programa visa capacitar desenvolvedores e pesquisadores para solucionar problemas de alto impacto na indústria de dispositivos inteligentes e sistemas embarcados.

A estrutura curricular compreende:
1. **Módulo 1 – Núcleo Comum de Formação (210h):**
   - Dados, Experimentação e Metodologia Científica (30h)
   - Engenharia de Software, Requisitos e Gestão do Desenvolvimento (24h)
   - Metodologia de Projetos, Ética e Habilidades Profissionais (30h)
   - Arquitetura de Software (18h)
   - Inteligência Artificial: Fundamentos, Frameworks e Aplicações (36h)
   - Programação Java/Kotlin e Desenvolvimento de Aplicações Android (42h)
   - Testes, Automação, Segurança e Integração Contínua (30h)
2. **Trilhas Especializadas (75h - Escolha de 1 Trilha):**
   - **Trilha 1:** Inteligência Artificial aplicada à Otimização de Sistemas Android (AOSP, ML/DL, On-Device AI).
   - **Trilha 2:** Segurança de Dispositivos Móveis e Automação de Validações (AOSP Security, Modelagem de Ameaças, Automação de Testes).
   - **Trilha 3:** Eficiência Energética avaliada por Algoritmos de Otimização (AOSP Power Management, Profiling Energético, Otimização Multiobjetivo).

---

## 2. Visão Geral do Desafio: Projeto "Android Sentinel Core"

O desafio consiste no desenvolvimento e experimentação do **Android Sentinel Core**, um framework e aplicação Android para observabilidade, telemetria em tempo real, auditoria de segurança e otimização de recursos de hardware.

### Estrutura da Avaliação (Total: 100 Pontos)
- **Parte 1: Núcleo Comum de Engenharia & Android (50 Pontos) — [Obrigatório para Todos]**
- **Parte 2: Módulo Específico da Trilha Escolhida (30 Pontos) — [Escolha 1 Trilha: IA, Segurança ou Energia]**
- **Parte 3: Relatório Técnico-Científico e Rastreabilidade (20 Pontos) — [Obrigatório para Todos]**

```
+-------------------------------------------------------------------------+
|                       ANDROID SENTINEL CORE ARCHITECTURE               |
+-------------------------------------------------------------------------+
|  [Presentation Layer] ViewModels (StateFlow) + Jetpack Compose UI       |
+-------------------------------------------------------------------------+
|  [Domain Layer] Pure Kotlin UseCases & Entities (Zero Android SDK)       |
|    - MonitorSystemHealthUseCase                                         |
|    - RecordAnomalyUseCase                                               |
+-------------------------------------------------------------------------+
|  [Data Layer] Repositories + Local DB (Room) + Telemetry Providers     |
|    - Real Hardware Metrics / Synthetic Dataset Toggle                   |
+-------------------------------------------------------------------------+
|  [Specialized Track Module]                                             |
|    Trilha 1 (IA): On-Device Anomaly Classifier (TFLite / ONNX)          |
|    Trilha 2 (Sec): STRIDE Threat Model + Automated Security Validator   |
|    Trilha 3 (Energy): Multiobjective Heuristic Task Scheduler           |
+-------------------------------------------------------------------------+
```

---

## 3. Especificação da Parte 1: Núcleo Comum (50 Pontos)

### 3.1 Arquitetura e Engenharia de Software (15 Pontos)
- **Linguagem & Plataforma:** Kotlin (Android API 26+), estruturado com **Clean Architecture** e **MVVM** / **MVI**.
- **Separação de Camadas:**
  - `domain`: Modelos imutáveis e Casos de Uso livres de referências `android.*`.
  - `data`: Repositórios, Room Database e adaptadores de telemetria.
  - `presentation`: ViewModels reativos emitindo `StateFlow` para telas em **Jetpack Compose** (ou Views tradicionais).
- **SOLID & Inversão de Dependência:** Uso de injeção de dependência (Hilt, Koin ou manual bem estruturada).
- **Coroutines & Flow:** Concorrência estruturada com despacho explícito de threads (`Dispatchers.IO`, `Default`, `Main`).

### 3.2 Coleta de Telemetria e Persistência Local (15 Pontos)
- **Coleta de Métricas Periódicas:**
  - *CPU:* Uso percentual estimado.
  - *Memória:* Memória livre, utilizada e flag de pressão (`isLowMemory`).
  - *Bateria & Temperatura:* Nível (%), temperatura (°C), voltagem (mV) via `BatteryManager`.
  - *Rede:* Tipo de conexão ativa e bytes trafegados.
- **Persistência com Room:** Armazenamento local das medições com histórico e limitação aos últimos 500 registros.
- **Modo Mock / Offline:** Suporte a carregar e reproduzir os dados de `starter_kit/mock_telemetry_dataset.json` sem depender de dispositivo físico.

### 3.3 Testes Automatizados e Pipeline de CI/CD (20 Pontos)
- **Testes Unitários:** Suíte JUnit + MockK cobrindo os UseCases de domínio e repositórios.
- **CI com GitHub Actions:** Pipeline em `.github/workflows/ci.yml` executando lint estático, compilação (`assembleDebug`) e testes unitários automatizados.

---

## 4. Especificação da Parte 2: Módulos Especializados (30 Pontos)
*Selecione apenas uma trilha correspondente à sua área de interesse:*

### Trilha 1: Inteligência Artificial aplicada à Otimização de Sistemas Android
1. **Modelagem & Script:** Análise e treinamento de modelo para detecção de anomalias em séries temporais de telemetria em Python (apoiado por `starter_kit/baseline_evaluator.py`).
2. **Comparação de Modelos:** Comparar ao menos duas abordagens (ex.: Isolation Forest vs Regressão Logística ou Random Forest) apresentando métricas quantitativas (F1-Score, Acurácia, Matriz de Confusão).
3. **Conversão On-Device:** Converter para TensorFlow Lite (`.tflite`) ou ONNX Runtime, aplicando quantização (INT8/FP16) e registrando o tamanho e latência estimada.
4. **Integração no Android:** Implementar o contrato `OnDeviceAnomalyClassifier` no app Sentinel disparando alertas em tempo real.

### Trilha 2: Segurança de Dispositivos Móveis e Automação de Validações
1. **Modelagem de Ameaças:** Matriz STRIDE cobrindo o app Android Sentinel e mapeando os controles do **OWASP MASVS v2.0**.
2. **Auditoria & Hardening:** Identificar, documentar e corrigir pelo menos 4 vulnerabilidades clássicas (componentes exportados sem permissão, SharedPreferences em texto claro, falta de SSL pinning, logs sensíveis em Logcat de release).
3. **Script Automatizado de Verificação:** Script executável (Python/Bash/teste Android) que valida determinísticamente as diretivas de segurança do APK/dispositivo e gera relatório pass/fail.

### Trilha 3: Eficiência Energética avaliada por Algoritmos de Otimização
1. **Protocolo Experimental:** Definição de protocolo para mensurar consumo de bateria (mA) sob diferentes taxas de envio e interfaces (Wi-Fi vs 5G vs Doze Mode).
2. **Modelagem Matemática Multiobjetivo:** Formular formalmente a função de custo multiobjetivo ponderando energia, latência e risco de perda de telemetria.
3. **Algoritmo Heurístico:** Implementar em Kotlin ou Python um algoritmo de busca (Genético, Simulated Annealing ou Heurística Gulosa) para escalonar lotes de sincronização respeitando limites térmicos e de bateria.
4. **Comprovação Experimental:** Demonstrar numericamente a redução percentual de consumo em relação ao envio sob demanda, comparando com o baseline do `baseline_evaluator.py`.

---

## 5. Especificação da Parte 3: Relatório Técnico-Científico (20 Pontos)

O candidato deve preencher o template `starter_kit/TEMPLATE_RELATORIO_TECNICO.md`:
- **Resumo Executivo (Abstract)**
- **Formulação de Hipótese Científica ($H_0$ vs $H_1$)**
- **Desenho Experimental (Variáveis Independentes, Dependentes e de Controle)**
- **Resultados e Evidências Numéricas (Tabelas e Gráficos Comparativos)**
- **Ameaças à Validade e Limitações**
- **Rastreabilidade de Decisões e Commits no Git**

---

## 6. Matriz e Rubrica de Avaliação (0 a 100 Pontos)

| Critério | Peso | Nível Excelente (Nota Máxima) | Penalidades Típicas |
| :--- | :---: | :--- | :--- |
| **1. Arquitetura & Código Limpo** | 20 pts | Clean Architecture estrita, SOLID aplicado, Kotlin idiomático, UseCases isolados. | Lógica de negócio na View; código acoplado (-10 pts). |
| **2. Implementação Android Core** | 20 pts | Coleta funcional, persistência Room, UI declarativa reativa, alternador de dataset sintético. | App quebra (crash); bloqueio da Main Thread (-12 pts). |
| **3. Testes Unitários & CI** | 15 pts | Cobertura de UseCases com JUnit/MockK; GitHub Actions executando com sucesso. | Sem testes (-10 pts); CI inexistente ou quebrado (-5 pts). |
| **4. Trilha Especializada** | 25 pts | Implementação completa dos entregáveis da trilha escolhida com resultados comprovados. | Trilha não implementada ou superficial (-15 a -25 pts). |
| **5. Relatório Científico & Git** | 20 pts | Hipótese formal ($H_0/H_1$), evidências quantitativas com gráficos, commits semânticos no Git. | Sem relatório (-12 pts); commit único com todo o código (-8 pts). |

---

## 7. Starter Kit Fornecido no Repositório

Para acelerar o desenvolvimento e nivelar as condições de entrega, utilize os recursos da pasta `starter_kit/`:
- `mock_telemetry_dataset.json`: 120 amostras com 5 cenários operacionais (Idle, CPU Spike, Wakelock Leak, Security Flood, Doze Mode).
- `baseline_evaluator.py`: Script pronto que calcula métricas do baseline e extrai matriz de features para IA.
- `TEMPLATE_RELATORIO_TECNICO.md`: Estrutura pronta do relatório em Markdown.
- `adb_profiling_cheatsheet.md`: Comandos essenciais de profiling no Android (top, dumpsys battery, perfetto).
- `ci_workflow_sample.yml`: Exemplo completo de pipeline GitHub Actions.
- `ArchitectureSample.kt`: Contratos de UseCases, repositórios e interfaces para as 3 trilhas.

---

## 8. Instruções de Submissão

1. Submeta o link do repositório Git (GitHub ou GitLab).
2. Mantenha histórico com commits frequentes e semânticos (Conventional Commits).
3. Forneça instruções completas de execução no `README.md`.
4. Declare transparentemente o uso de ferramentas de Inteligência Artificial no `README.md`.
"""

# -----------------------------------------------------------------------------
# 3. GERAÇÃO DE README.md INSTITUCIONAL
# -----------------------------------------------------------------------------

README_CONTENT = """# Desafio Técnico de Admissão &bull; Residência Tecnológica em Sistemas Android Avançados

Este repositório contém o **Edital Oficial**, a **Base Documental** e o **Starter Kit** do Desafio Técnico de Admissão e Nivelamento para o Programa de Residência Tecnológica em Sistemas Android Avançados, Inteligência Artificial e Eficiência Energética.

## 📄 Documentação Oficial
- 📕 **[PDF Oficial do Desafio Técnico](Desafio_Tecnico_Residencia_Android.pdf)** — Documento oficial formatado pronto para leitura e distribuição.
- 📘 **[Edital Completo em Markdown](DESAFIO_TECNICO.md)** — Versão integral em formato Markdown para consulta online e rastreabilidade no Git.

---

## 🛠️ Conteúdo do Starter Kit (`starter_kit/`)

| Arquivo | Descrição |
| :--- | :--- |
| [`mock_telemetry_dataset.json`](starter_kit/mock_telemetry_dataset.json) | Dataset com 120 pontos cronológicos de telemetria simulando 5 regimes do SO (Idle, CPU Spike, Wakelock Leak, Anomalia de IPC, Doze Mode). |
| [`baseline_evaluator.py`](starter_kit/baseline_evaluator.py) | Script de apoio que processa a telemetria, gera estatísticas da Linha de Base (CPU, bateria, anomalias) e prepara matrizes para ML. |
| [`TEMPLATE_RELATORIO_TECNICO.md`](starter_kit/TEMPLATE_RELATORIO_TECNICO.md) | Estrutura obrigatória em formato artigo/relatório para preenchimento da Parte 3 (Metodologia Científica). |
| [`adb_profiling_cheatsheet.md`](starter_kit/adb_profiling_cheatsheet.md) | Guia prático com comandos ADB para monitoramento de CPU, memória, bateria e gravação de traces com Google Perfetto. |
| [`ci_workflow_sample.yml`](starter_kit/ci_workflow_sample.yml) | Modelo pré-configurado de pipeline de Integração Contínua para GitHub Actions (Lint, Build e Testes). |
| [`ArchitectureSample.kt`](starter_kit/ArchitectureSample.kt) | Contratos de referência em Kotlin demonstrando Clean Architecture, SOLID, Coroutines Flow e interfaces para as 3 trilhas. |

---

## 🎯 Estrutura do Desafio (100 Pontos)
1. **Parte 1 (50 pts) — Núcleo Comum:** Clean Architecture em Kotlin, app Android reativo com Room, Testes Unitários e CI Pipeline.
2. **Parte 2 (30 pts) — Trilha Especializada (Escolher 1):**
   - *Trilha 1:* IA aplicada à Otimização Android (Script/Notebook, comparação de modelos, TFLite on-device).
   - *Trilha 2:* Cibersegurança e Validações (Modelagem STRIDE, mitigação OWASP MASVS, script automatizado).
   - *Trilha 3:* Eficiência Energética (Modelagem matemática multiobjetivo, algoritmo heurístico de otimização).
3. **Parte 3 (20 pts) — Relatório Técnico-Científico:** Hipótese $H_0$ vs $H_1$, desenho experimental, evidências quantitativas e rastreabilidade no Git.

---

## 🚀 Como Compilar o PDF Novamente
Caso sejam realizadas modificações no template, o script gerador automatizado pode ser executado:
```bash
python generate_all.py
```
*Requisitos: Python 3.10+, Microsoft Edge ou Google Chrome instalado.*
"""

def main():
    print("1. Escrevendo DESAFIO_TECNICO.md...")
    with open("DESAFIO_TECNICO.md", "w", encoding="utf-8") as f:
        f.write(MARKDOWN_CONTENT)
        
    print("2. Escrevendo README.md...")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(README_CONTENT)
        
    print("3. Escrevendo Desafio_Tecnico_Residencia_Android.html...")
    with open("Desafio_Tecnico_Residencia_Android.html", "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
        
    print("4. Compilando PDF via Edge headless...")
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        
    html_file = os.path.abspath("Desafio_Tecnico_Residencia_Android.html")
    pdf_file = os.path.abspath("Desafio_Tecnico_Residencia_Android.pdf")
    
    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file}",
        f"file:///{html_file}"
    ]
    subprocess.run(cmd, check=True)
    
    reader = pypdf.PdfReader(pdf_file)
    total_pages = len(reader.pages)
    size_bytes = os.path.getsize(pdf_file)
    
    print(f"\n=======================================================")
    print(f"Sucesso! PDF Gerado: {pdf_file}")
    print(f"Páginas: {total_pages} | Tamanho: {size_bytes:,} bytes")
    print(f"=======================================================")

if __name__ == "__main__":
    main()

# Desafio Técnico de Admissão e Nivelamento
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

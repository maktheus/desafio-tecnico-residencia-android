# Desafio Técnico de Admissão &bull; Residência Tecnológica em Sistemas Android Avançados

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

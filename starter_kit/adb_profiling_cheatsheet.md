# Guia Prático de Profiling Android via ADB (Android Debug Bridge)
**Referência para Candidatos e Residentes**

Este guia consolida os comandos essenciais para coleta de dados de telemetria, diagnóstico de desempenho, inspeção de consumo energético e validação de segurança em dispositivos físicos ou emuladores Android (API 26+).

---

## 1. Conexão e Informações do Dispositivo
```bash
# Listar dispositivos conectados
adb devices -l

# Obter informações do hardware e versão do Android
adb shell getprop ro.build.version.release
adb shell getprop ro.product.model
adb shell getprop ro.board.platform
```

---

## 2. Telemetria e Monitoramento de CPU
```bash
# Monitorar uso de CPU em tempo real (atualização a cada 2 segundos)
adb shell top -m 10 -d 2

# Obter snapshot detalhado de consumo de CPU por processo
adb shell dumpsys cpuinfo | grep -E "sentinel|TOTAL"

# Verificar frequências dos núcleos e governors
adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
adb shell cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

---

## 3. Gestão e Diagnóstico Energético (Battery & Power)
```bash
# Obter status atual da bateria (nível, voltagem, temperatura, status)
adb shell dumpsys battery

# Simular desconexão do carregador (modo bateria pura)
adb shell dumpsys battery unplug

# Resetar estatísticas de consumo de bateria
adb shell dumpsys batterystats --reset

# Exportar histórico detalhado de bateria (compatível com Battery Historian)
adb shell dumpsys batterystats > batterystats_output.txt

# Inspecionar WakeLocks ativos mantidos por aplicativos
adb shell dumpsys power | grep -A 20 "Wake Locks"

# Forçar entrada no modo Doze (Deep Sleep)
adb shell dumpsys deviceidle force-idle
# Retirar do modo Doze
adb shell dumpsys deviceidle unforce
```

---

## 4. Monitoramento de Memória e Processos (Memory Profiling)
```bash
# Resumo de memória do sistema
adb shell dumpsys meminfo

# Inspecionar detalhes de memória de um aplicativo específico (substitua pelo seu package)
adb shell dumpsys meminfo com.example.androidsentinel

# Verificar ocorrências de Low Memory Killer (LMK)
adb shell cat /proc/zoneinfo
adb shell dmesg | grep -i oom
```

---

## 5. Rastreamento Avançado com Perfetto Trace
```bash
# Gravar um trace de sistema de 10 segundos com Perfetto
adb shell perfetto \
  -c - --txt \
  -o /data/misc/perfetto-traces/trace.perfetto-trace <<EOF
buffers: {
    size_kb: 63488
    fill_policy: RING_BUFFER
}
data_sources: {
    config {
        name: "linux.process_stats"
        target_buffer: 0
        process_stats_config {
            scan_all_processes_on_start: true
        }
    }
}
data_sources: {
    config {
        name: "linux.ftrace"
        ftrace_config {
            ftrace_events: "sched/sched_switch"
            ftrace_events: "power/cpu_frequency"
            ftrace_events: "power/cpu_idle"
        }
    }
}
duration_ms: 10000
EOF

# Baixar o trace para análise visual em https://ui.perfetto.dev
adb pull /data/misc/perfetto-traces/trace.perfetto-trace ./trace.perfetto-trace
```

---

## 6. Verificações de Segurança e IPC
```bash
# Inspecionar componentes exportados de um pacote
adb shell dumpsys package com.example.androidsentinel | grep -A 10 -B 2 "Activity|Receiver|Service"

# Disparar um Broadcast Intent via linha de comando
adb shell am broadcast -a com.sentinel.internal.EXPORTED_DIAGNOSTIC_RECEIVER --es "data" "test_payload"

# Inspecionar permissões concedidas e declaradas
adb shell dumpsys package com.example.androidsentinel | grep -A 15 "grantedPermissions"

# Filtrar logs de segurança e erros no Logcat
adb logcat -d -v time *:E | grep -i "sentinel"
```

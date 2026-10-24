#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
ANDROID SENTINEL CORE - SCRIPT AUXILIAR DE BASELINE E TELEMETRIA (STARTER KIT)
===============================================================================
Este script fornece uma base pronta para os candidatos da Residência Tecnológica.
Permite carregar o dataset sintético de telemetria, calcular as estatísticas da
linha de base (baseline) e servir de apoio para as 3 trilhas:
 - Trilha 1: Extração de matriz de features e labels para modelos de IA.
 - Trilha 2: Inspeção de eventos de IPC e anomalias de segurança.
 - Trilha 3: Cálculo do consumo energético acumulado e corrente média.

Uso:
    python starter_kit/baseline_evaluator.py
===============================================================================
"""

import json
import os
import math

def load_telemetry_data(dataset_path="starter_kit/mock_telemetry_dataset.json"):
    if not os.path.exists(dataset_path):
        # Fallback se executado de dentro da pasta starter_kit
        if os.path.exists("mock_telemetry_dataset.json"):
            dataset_path = "mock_telemetry_dataset.json"
        else:
            raise FileNotFoundError(f"Dataset não encontrado em {dataset_path}")

    with open(dataset_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["samples"]

def compute_baseline_metrics(samples):
    total_samples = len(samples)
    cpu_usages = [s["cpu"]["total_usage_percent"] for s in samples]
    temps = [s["battery"]["temperature_celsius"] for s in samples]
    currents_ua = [s["battery"]["current_ua"] for s in samples]
    anomalies = [s["is_anomaly"] for s in samples]
    
    # Consumo médio de corrente em mA (1 mA = 1.000 uA)
    # Valores negativos indicam descarga da bateria
    currents_ma = [abs(c) / 1000.0 for c in currents_ua]
    
    # Energia aproximada consumida em mAh ao longo do período
    # Amostragem a cada 10 segundos: tempo em horas = 10 / 3600 h por amostra
    total_mah = sum(i_ma * (10.0 / 3600.0) for i_ma in currents_ma)
    
    avg_cpu = sum(cpu_usages) / total_samples
    max_cpu = max(cpu_usages)
    avg_temp = sum(temps) / total_samples
    max_temp = max(temps)
    avg_current_ma = sum(currents_ma) / total_samples
    total_anomalies = sum(anomalies)

    return {
        "total_samples": total_samples,
        "duration_minutes": (total_samples * 10) / 60.0,
        "avg_cpu_percent": round(avg_cpu, 2),
        "max_cpu_percent": round(max_cpu, 2),
        "avg_temperature_c": round(avg_temp, 2),
        "max_temperature_c": round(max_temp, 2),
        "avg_current_ma": round(avg_current_ma, 2),
        "total_energy_drain_mah": round(total_mah, 3),
        "anomaly_count": total_anomalies,
        "anomaly_rate_percent": round((total_anomalies / total_samples) * 100.0, 1)
    }

def print_summary(metrics):
    print("=" * 65)
    print(" ANDROID SENTINEL CORE - RELATÓRIO DA LINHA DE BASE (BASELINE)")
    print("=" * 65)
    print(f" Amostras analisadas:      {metrics['total_samples']} leituras")
    print(f" Período total coberto:    {metrics['duration_minutes']} minutos")
    print(f" Uso Médio de CPU:         {metrics['avg_cpu_percent']}% (Pico: {metrics['max_cpu_percent']}%)")
    print(f" Temperatura Média:        {metrics['avg_temperature_c']} °C (Pico: {metrics['max_temperature_c']} °C)")
    print(f" Corrente Média:           {metrics['avg_current_ma']} mA")
    print(f" Descarga Acumulada:       {metrics['total_energy_drain_mah']} mAh")
    print(f" Anomalias Registradas:    {metrics['anomaly_count']} ({metrics['anomaly_rate_percent']}%)")
    print("=" * 65)
    print("\n[Dica Metodológica]")
    print("Utilize estes números como Linha de Base (Baseline) para preencher a")
    print("Seção 4 do seu 'RELATORIO_TECNICO.md' ao comparar com a solução proposta.")
    print("=" * 65)

def export_features_for_ml(samples):
    """
    Função utilitária para candidatos da Trilha 1 (IA):
    Gera matriz X (features) e vetor y (rótulos) para treinamento direto.
    """
    X = []
    y = []
    feature_names = [
        "cpu_usage", "cpu_user", "cpu_sys",
        "battery_temp", "battery_voltage_mv", "current_ua",
        "mem_used_mb", "rx_bytes", "tx_bytes",
        "wakelock_active", "doze_active"
    ]
    for s in samples:
        row = [
            s["cpu"]["total_usage_percent"],
            s["cpu"]["user_percent"],
            s["cpu"]["system_percent"],
            s["battery"]["temperature_celsius"],
            s["battery"]["voltage_mv"],
            s["battery"]["current_ua"],
            s["memory"]["used_mb"],
            s["network"]["rx_bytes_delta"],
            s["network"]["tx_bytes_delta"],
            1.0 if s["system_state"]["wakelock_held"] else 0.0,
            1.0 if s["system_state"]["doze_mode_active"] else 0.0
        ]
        X.append(row)
        y.append(s["is_anomaly"])
    return feature_names, X, y

if __name__ == "__main__":
    samples = load_telemetry_data()
    metrics = compute_baseline_metrics(samples)
    print_summary(metrics)
    feat_names, X, y = export_features_for_ml(samples)
    print(f"\n[Trilha 1 - ML Helper] Matriz de Features pronta:")
    print(f" -> X shape: ({len(X)}, {len(feat_names)}) | y shape: ({len(y)},)")
    print(f" -> Atributos: {', '.join(feat_names)}")

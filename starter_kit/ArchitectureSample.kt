package com.example.androidsentinel.sample

import kotlinx.coroutines.flow.Flow

/**
 * ============================================================================
 * ANDROID SENTINEL CORE - REFERÊNCIA DE ARQUITETURA LIMPA (CLEAN ARCHITECTURE)
 * ============================================================================
 * Este arquivo serve como referência de design de código para os candidatos.
 * Demonstra a separação de responsabilidades (SOLID), inversão de controle,
 * uso de Kotlin Coroutines/Flow e modelagem de domínio pura.
 */

// ----------------------------------------------------------------------------
// 1. CAMADA DE DOMÍNIO (DOMAIN LAYER) - Pura, sem dependências de framework Android
// ----------------------------------------------------------------------------

data class TelemetrySnapshot(
    val timestampMs: Long,
    val cpuUsagePercent: Double,
    val memoryUsedMb: Long,
    val batteryLevelPercent: Double,
    val batteryTemperatureCelsius: Double,
    val isAnomalyDetected: Boolean = false
)

sealed interface TelemetryState {
    object Idle : TelemetryState
    object Collecting : TelemetryState
    data class Success(val snapshot: TelemetrySnapshot) : TelemetryState
    data class Error(val message: String, val throwable: Throwable? = null) : TelemetryState
}

/**
 * Contrato de repositório (Inversão de Dependência - DIP)
 */
interface TelemetryRepository {
    fun observeCurrentTelemetry(): Flow<TelemetrySnapshot>
    suspend fun recordTelemetry(snapshot: TelemetrySnapshot): Result<Unit>
    suspend fun getHistoricalTelemetry(limit: Int = 50): List<TelemetrySnapshot>
}

/**
 * Caso de Uso (Single Responsibility Principle - SRP)
 */
class MonitorSystemHealthUseCase(
    private val telemetryRepository: TelemetryRepository
) {
    operator fun invoke(): Flow<TelemetrySnapshot> {
        return telemetryRepository.observeCurrentTelemetry()
    }
}

class RecordTelemetryAnomalyUseCase(
    private val telemetryRepository: TelemetryRepository
) {
    suspend operator fun invoke(snapshot: TelemetrySnapshot): Result<Unit> {
        // Validação e regra de negócio
        val adjustedSnapshot = if (snapshot.cpuUsagePercent > 80.0 || snapshot.batteryTemperatureCelsius > 42.0) {
            snapshot.copy(isAnomalyDetected = true)
        } else {
            snapshot
        }
        return telemetryRepository.recordTelemetry(adjustedSnapshot)
    }
}

// ----------------------------------------------------------------------------
// 2. CONTRATOS PARA AS TRILHAS ESPECIALIZADAS
// ----------------------------------------------------------------------------

/**
 * [Trilha 1 - IA aplicada à Otimização de Sistemas Android]
 * Contrato para inferência On-Device (ex: TFLite / ONNX Runtime)
 */
interface OnDeviceAnomalyClassifier {
    data class InferenceResult(
        val isAnomaly: Boolean,
        val anomalyConfidence: Float,
        val latencyMs: Long
    )
    suspend fun classify(features: FloatArray): InferenceResult
}

/**
 * [Trilha 2 - Segurança de Dispositivos Móveis e Automação]
 * Contrato para verificação de conformidade e integridade
 */
interface SecurityComplianceValidator {
    data class SecurityFinding(
        val ruleId: String,
        val severity: String, // CRITICAL, HIGH, MEDIUM, LOW
        val description: String,
        val isCompliant: Boolean
    )
    suspend fun evaluateRuntimeSecurity(): List<SecurityFinding>
}

/**
 * [Trilha 3 - Eficiência Energética e Algoritmos de Otimização]
 * Contrato para agendador adaptativo com otimização multiobjetivo
 */
interface AdaptiveTaskScheduler {
    data class SchedulePolicy(
        val batchIntervalSeconds: Int,
        val requireUnmeteredNetwork: Boolean,
        val requireCharging: Boolean,
        val estimatedEnergyCostMah: Double
    )
    fun computeOptimalPolicy(
        currentBatteryPercent: Double,
        pendingPayloadSizeKb: Long,
        isThermalThrottled: Boolean
    ): SchedulePolicy
}

package com.domain.usecase

import com.domain.model.ReservationInfo
import com.domain.util.DomainResult
import kotlinx.coroutines.flow.Flow

interface ReservationListUseCase {
    suspend operator fun invoke(filters: Map<String, String>): Flow<DomainResult<List<ReservationInfo>>>
}
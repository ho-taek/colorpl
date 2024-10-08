package com.data.model.response


import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class ResponsePayResult(
    @SerialName("cancelled_price")
    val cancelledPrice: Int,
    @SerialName("cancelled_tax_free")
    val cancelledTaxFree: Int,
    @SerialName("card_data")
    val cardData: CardData,
    @SerialName("company_name")
    val companyName: String,
    @SerialName("currency")
    val currency: String,
    @SerialName("gateway_url")
    val gatewayUrl: String,
    val http_status: Int,
    @SerialName("metadata")
    val metadata: Metadata,
    @SerialName("method")
    val method: String,
    @SerialName("method_origin")
    val methodOrigin: String,
    @SerialName("method_origin_symbol")
    val methodOriginSymbol: String,
    @SerialName("method_symbol")
    val methodSymbol: String,
    @SerialName("order_id")
    val orderId: String,
    @SerialName("order_name")
    val orderName: String,
    @SerialName("pg")
    val pg: String,
    val price: Int,
    val purchased_at: String?,
    val receipt_id: String?,
    @SerialName("receipt_url")
    val receiptUrl: String,
    @SerialName("requested_at")
    val requestedAt: String,
    @SerialName("sandbox")
    val sandbox: Boolean,
    val scheduleId: Int,
    @SerialName("status")
    val status: Int,
    @SerialName("status_locale")
    val statusLocale: String,
    @SerialName("tax_free")
    val taxFree: Int
) {
    @Serializable
    data class CardData(
        @SerialName("card_approve_no")
        val cardApproveNo: String,
        @SerialName("card_company")
        val cardCompany: String,
        @SerialName("card_company_code")
        val cardCompanyCode: String,
        @SerialName("card_interest")
        val cardInterest: String,
        @SerialName("card_no")
        val cardNo: String,
        @SerialName("card_quota")
        val cardQuota: String,
        @SerialName("card_type")
        val cardType: String,
        @SerialName("complex_payment")
        val complexPayment: Int,
        @SerialName("coupon")
        val coupon: Double,
        @SerialName("point")
        val point: Double,
        @SerialName("receipt_url")
        val receiptUrl: String,
        @SerialName("tid")
        val tid: String
    )

    @Serializable
    data class Metadata(
        @SerialName("selectedSeatList")
        val selectedSeatList: List<SelectedSeat>,
        @SerialName("showDetailId")
        val showDetailId: Int,
        @SerialName("showHallName")
        val showHallName: String,
        @SerialName("showName")
        val showName: String,
        @SerialName("showScheduleId")
        val showScheduleId: Int,
        @SerialName("showTheaterName")
        val showTheaterName: String
    ) {
        @Serializable
        data class SelectedSeat(
            @SerialName("col")
            val col: Int,
            @SerialName("grade")
            val grade: String,
            @SerialName("name")
            val name: String,
            @SerialName("row")
            val row: Int
        )
    }
}
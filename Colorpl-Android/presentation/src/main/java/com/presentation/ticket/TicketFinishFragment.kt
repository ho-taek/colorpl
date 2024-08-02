package com.presentation.ticket

import android.os.Bundle
import androidx.hilt.navigation.fragment.hiltNavGraphViewModels
import androidx.lifecycle.flowWithLifecycle
import androidx.lifecycle.lifecycleScope
import androidx.navigation.fragment.findNavController
import androidx.navigation.fragment.navArgs
import com.bumptech.glide.Glide
import com.colorpl.presentation.R
import com.colorpl.presentation.databinding.FragmentTicketFinishBinding
import com.presentation.base.BaseFragment
import com.presentation.util.ImageProcessingUtil
import com.presentation.util.onBackButtonPressed
import com.presentation.viewmodel.TicketCreateViewModel
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.flow.launchIn
import kotlinx.coroutines.flow.onEach
import timber.log.Timber

@AndroidEntryPoint
class TicketFinishFragment :
    BaseFragment<FragmentTicketFinishBinding>(R.layout.fragment_ticket_finish) {

    private val viewModel: TicketCreateViewModel by hiltNavGraphViewModels(R.id.nav_ticket_graph)
    private val args: TicketFinishFragmentArgs by navArgs()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        requireActivity().onBackButtonPressed(this) {
            findNavController().navigate(R.id.action_fragment_ticket_finish_to_fragment_schedule)
        }
    }

    override fun initView() {
        observeViewModel()
        initUi()
    }

    private fun observeViewModel() {
        viewModel.createResponse.flowWithLifecycle(viewLifecycleOwner.lifecycle)
            .onEach { ticketId ->
                if (ticketId > 0) findNavController().navigate(R.id.action_fragment_ticket_finish_to_fragment_schedule)
            }.launchIn(viewLifecycleOwner.lifecycleScope)
    }

    private fun initUi() {
        Glide.with(binding.root.context).load(args.imageUrl).centerCrop().into(binding.ivPoster)
        val description = viewModel.description.value
        binding.apply {
            tvTitle.text = description?.title
            tvDetail.text = description?.detail
            tvSchedule.text = description?.schedule
            tvSeat.text = description?.seat
            tvConfirm.setOnClickListener {
                Timber.d(
                    "${ImageProcessingUtil(binding.root.context).uriToFile(args.imageUrl!!)!!}  size: ${
                        ImageProcessingUtil(
                            binding.root.context
                        ).uriToFile(args.imageUrl!!)!!.length()
                    }"
                )
                viewModel.createTicket(ImageProcessingUtil(binding.root.context).uriToFile(args.imageUrl!!)!!)
            }
        }
    }
}
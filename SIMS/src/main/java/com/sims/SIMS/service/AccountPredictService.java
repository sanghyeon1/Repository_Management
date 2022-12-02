package com.sims.SIMS.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.sims.SIMS.domain.AccountPredict;
import com.sims.SIMS.domain.Log;
import com.sims.SIMS.repository.AccountPredictRepository;
import com.sims.SIMS.repository.LogRepository;

@Service
public class AccountPredictService {
	private final AccountPredictRepository accountPredictRepository;

	public AccountPredictService(AccountPredictRepository accountPredictRepository) {
		this.accountPredictRepository = accountPredictRepository;
	}

	public List<AccountPredict> findAccountPredict() {
		return accountPredictRepository.findAll();
	}

	public Optional<AccountPredict> findOne(Long accountPredictId) {
		return accountPredictRepository.findById(accountPredictId);
	}
}

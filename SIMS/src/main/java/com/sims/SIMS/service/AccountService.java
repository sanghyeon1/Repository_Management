package com.sims.SIMS.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.sims.SIMS.domain.Account;
import com.sims.SIMS.domain.ProductSales;
import com.sims.SIMS.repository.AccountRepository;
import com.sims.SIMS.repository.ProductSalesRepository;

@Service
public class AccountService {
	private final AccountRepository accountRepository;

	public AccountService(AccountRepository accountRepository) {
		this.accountRepository = accountRepository;
	}

	public List<Account> findAccount() {
		return accountRepository.findAll();
	}

	public List<Account> findRecent10Account() {
		return accountRepository.findRecent10();
	}

	public Optional<Account> findOne(Long accountId) {
		return accountRepository.findById(accountId);
	}
}

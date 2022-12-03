package com.sims.SIMS.service;

import java.util.ArrayList;
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

	public List<Account> findAccount(String tel) {
		return accountRepository.findAll(tel);
	}

	public List<Account> findRecent10Account(String tel) {
		List<Account> accounts = accountRepository.findAll(tel);
		List<Account> result = new ArrayList<>();
		int i = 0;
		for (Account account : accounts) {
			if (i < 10) {
				result.add(account);
			}
			i++;
		}
		return result;
	}

	public Optional<Account> findOne(Long accountId) {
		return accountRepository.findById(accountId);
	}
}

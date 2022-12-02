package com.sims.SIMS.repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.Account;
import com.sims.SIMS.domain.Log;

@Repository
public class AccountRepository {
	private final EntityManager em;

	public AccountRepository(EntityManager em) {
		this.em = em;
	}

	public Optional<Account> findById(Long user_id) {
		Account account = em.find(Account.class, user_id);
		return Optional.ofNullable(account);
	}

	public List<Account> findAll() {
		return em.createQuery("select m from Account m", Account.class)
			.getResultList();
	}

	public List<Account> findRecent10() {
		List<Account> accounts = em.createQuery("select m from Account m order by m.date desc", Account.class).getResultList();
		List<Account> result = new ArrayList<>();
		for (int i = 0; i < 10; i++) {
			result.add(accounts.get(i));
		}
		return result;
	}
}

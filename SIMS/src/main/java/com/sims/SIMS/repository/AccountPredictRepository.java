package com.sims.SIMS.repository;

import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.AccountPredict;
import com.sims.SIMS.domain.Product;

@Repository
public class AccountPredictRepository {
	private final EntityManager em;

	public AccountPredictRepository(EntityManager em) {
		this.em = em;
	}

	public AccountPredict save(AccountPredict accountPredict) {
		em.persist(accountPredict);
		return accountPredict;
	}

	public Optional<AccountPredict> findById(Long id) {
		AccountPredict accountPredict = em.find(AccountPredict.class, id);
		return Optional.ofNullable(accountPredict);
	}

	public Optional<AccountPredict> findByTel(String tel) {
		List<AccountPredict> result = em.createQuery("select m from AccountPredict m where m.tel = :tel", AccountPredict.class)
			.setParameter("tel", tel)
			.getResultList();
		return result.stream().findAny();
	}

	public List<AccountPredict> findAll() {
		return em.createQuery("select m from AccountPredict m", AccountPredict.class)
			.getResultList();
	}
}

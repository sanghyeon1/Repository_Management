package com.sims.SIMS.repository;

import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.Log;
import com.sims.SIMS.domain.Member;

@Repository
public class LogRepository{
	private final EntityManager em;

	public LogRepository(EntityManager em) {
		this.em = em;
	}

	public Log save(Log log) {
		em.persist(log);
		return log;
	}

	public Optional<Log> findById(Long user_id) {
		Log log = em.find(Log.class, user_id);
		return Optional.ofNullable(log);
	}

	public List<Log> findAll(String tel) {
		return em.createQuery("select m from Log m where m.tel = :tel", Log.class)
			.setParameter("tel", tel)
			.getResultList();
	}

	public List<Log> findBuyLogs(String tel) {
		return em.createQuery("select m from Log m where m.tel = :tel and m.type= :type", Log.class)
			.setParameter("tel", tel)
			.setParameter("type", "buy")
			.getResultList();
	}

	public List<Log> findSellLogs(String tel) {
		return em.createQuery("select m from Log m where m.tel = :tel and m.type= :type", Log.class)
			.setParameter("tel", tel)
			.setParameter("type", "sell")
			.getResultList();
	}
}

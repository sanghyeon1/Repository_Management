package com.sims.SIMS.repository;

import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import com.sims.SIMS.domain.Member;

public class JpaMemberRepository implements MemberRepository{
	private final EntityManager em;

	public JpaMemberRepository(EntityManager em) {
		this.em = em;
	}

	public Member save(Member member) {
		em.persist(member);
		return member;
	}

	public Optional<Member> findById(String user_id) {
		Member member = em.find(Member.class, user_id);
		return Optional.ofNullable(member);
	}
	public List<Member> findAll() {
		return em.createQuery("select m from Member m", Member.class)
			.getResultList();
	}

	public Optional<Member> findByName(String name) {
		List<Member> result = em.createQuery("select m from Member m where m.name = :name", Member.class)
			.setParameter("name", name)
			.getResultList();
		return result.stream().findAny();
	}

	@Override
	public Boolean isRightPassword(String id, String password) {
		List<Member> result = em.createQuery("select m from Member m where m.user_id = :id", Member.class)
			.setParameter("id", id)
			.getResultList();
		return result.get(0).getPassword().equals(password);
	}
}

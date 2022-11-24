package com.sims.SIMS.repository;

import java.util.List;
import java.util.Optional;

import com.sims.SIMS.domain.Member;

public interface MemberRepository {
	Member save(Member member);

	Optional<Member> findById(String id);
	Optional<Member> findByName(String name);

	Boolean isRightPassword(String id, String password);
	List<Member> findAll();
}

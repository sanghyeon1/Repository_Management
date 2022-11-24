package com.sims.SIMS.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.sims.SIMS.domain.Member;
import com.sims.SIMS.repository.MemberRepository;

@Service
public class MemberService {
	private final MemberRepository memberRepository;

	public MemberService(MemberRepository memberRepository) {
		this.memberRepository = memberRepository;
	}

	public String join(Member member) {
		validateDuplicateMember(member);
		memberRepository.save(member);
		return member.getId();
	}

	private void validateDuplicateMember(Member member) {
		Optional<Member> result = memberRepository.findById(member.getId());
		result.ifPresent(m-> {
			throw new IllegalStateException("이미 존재하는 회원입니다.");
		});
	}

	public List<Member> findMembers() {
		return memberRepository.findAll();
	}

	public Optional<Member> findOne(String memberId) {
		return memberRepository.findById(memberId);
	}

	public Boolean isCorrectPassword(String id, String password) {
		return memberRepository.isRightPassword(id, password);
	}
}

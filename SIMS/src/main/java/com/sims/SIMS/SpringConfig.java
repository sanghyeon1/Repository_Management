package com.sims.SIMS;

import javax.persistence.EntityManager;
import javax.sql.DataSource;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.sims.SIMS.repository.JpaMemberRepository;
import com.sims.SIMS.repository.MemberRepository;
// import com.sims.SIMS.repository.MemoryMemberRepository;
import com.sims.SIMS.service.MemberService;

@Configuration
public class SpringConfig {
	private final DataSource dataSource;
	private final EntityManager em;
	public SpringConfig(DataSource dataSource, EntityManager em) {
		this.dataSource = dataSource;
		this.em = em;
	}

	@Bean
	public MemberService memberService() {
		return new MemberService(memberRepository());
	}
	@Bean
	public MemberRepository memberRepository() {
		// return new MemoryMemberRepository();
		// return new JdbcMemberRepository(dataSource);
		// return new JdbcTemplateMemberRepository(dataSource);
		return new JpaMemberRepository(em);
	}
}

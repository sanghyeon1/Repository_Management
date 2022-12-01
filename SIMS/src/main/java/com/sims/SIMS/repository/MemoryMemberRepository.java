// package com.sims.SIMS.repository;
//
// import java.util.ArrayList;
// import java.util.HashMap;
// import java.util.List;
// import java.util.Map;
// import java.util.Optional;
//
// import org.springframework.stereotype.Repository;
//
// import com.sims.SIMS.domain.Member;
//
// @Repository
// public class MemoryMemberRepository implements MemberRepository{
// 	private static Map<Long, Member> store = new HashMap<>();
// 	private static long sequence = 0L;
// 	@Override
// 	public Member save(Member member) {
// 		member.setId(++sequence);
// 		store.put(member.getId(), member);
// 		return member;
// 	}
//
// 	@Override
// 	public Optional<Member> findById(String id) {
// 		return Optional.ofNullable(store.get(id));
// 	}
//
// 	@Override
// 	public Optional<Member> findByName(String name) {
// 		return store.values().stream()
// 			.filter(member -> member.getName().equals(name))
// 			.findAny();
// 	}
//
// 	@Override
// 	public Boolean isRightPassword(String id, String password) {
// 		return store.get(id).getPassword().equals(password);
// 	}
//
// 	@Override
// 	public List<Member> findAll() {
// 		return new ArrayList<>(store.values());
// 	}
//
// 	public void clearStore() {
// 		store.clear();
// 	}
// }

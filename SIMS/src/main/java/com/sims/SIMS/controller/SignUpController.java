package com.sims.SIMS.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.sims.SIMS.domain.Member;
import com.sims.SIMS.service.MemberService;

@Controller
public class SignUpController {

	private final MemberService memberService;

	@Autowired
	public SignUpController(MemberService memberService) {
		this.memberService = memberService;
	}

	@GetMapping("/signUp")
	public String accountPage() {
		// 파이썬 프로그램 실행해서 가계부 내용 넣기




		return "signUpPage/SignUpPage";
	}

	@PostMapping("/signUp/new")
	public String signUpNew(SignUpForm form) {
		if (!form.getPassword().equals(form.getPasswordCheck())) {
			return "redirect:/error";
		}
		Member member = new Member();
		member.setName(form.getName());
		member.setUserId(form.getUserId());
		member.setPassword(form.getPassword());
		member.setTel(form.getPhoneNumber());
		System.out.println(memberService.join(member));
		return "redirect:/";
	}
}

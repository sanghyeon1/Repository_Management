package com.sims.SIMS.controller;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.sims.SIMS.domain.Member;
import com.sims.SIMS.service.MemberService;

@Controller
public class MainController {
	private final MemberService memberService;

	@Autowired
	public MainController(MemberService memberService) {
		this.memberService = memberService;
	}

	@GetMapping("/")
	public String mainPage() {
		return "mainPage/MainPage";
	}

	@PostMapping("/signIn")
	public String singIn(SignInForm form) {
		Optional<Member> members = memberService.findOne(form.getId());
		if (members.isEmpty()) {
			return "redirect:/signInError";
		}
		if (!memberService.isCorrectPassword(form.getId(), form.getPassword())) {
			return "redirect:/signInError";
		}
		return "redirect:/";
	}
}

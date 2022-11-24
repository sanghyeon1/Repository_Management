package com.sims.SIMS.controller;

import java.util.List;
import java.util.Optional;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.sims.SIMS.domain.Member;
import com.sims.SIMS.service.MemberService;
import com.sims.SIMS.session.SessionConst;
import com.sims.SIMS.session.SessionManager;

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
	public String singIn(SignInForm form, HttpServletRequest request) {
		Optional<Member> member = memberService.findOne(form.getId());
		if (member.isEmpty()) {
			return "redirect:/signInError";
		}
		if (!memberService.isCorrectPassword(form.getId(), form.getPassword())) {
			return "redirect:/signInError";
		}

		HttpSession session = request.getSession();
		session.setAttribute(SessionConst.LOGIN_MEMBER, member);
		return "redirect:/account";
	}

	@PostMapping("/logout")
	public String logoutV3(HttpServletRequest request) {
		HttpSession session = request.getSession(false);
		if (session != null) {
			session.invalidate();
		}
		return "redirect:/";
	}
}

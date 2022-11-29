package com.sims.SIMS.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AccountController {

	@GetMapping("/account")
	public String accountPage(HttpServletRequest request) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}
		// 쿼리문으로 가계부 데이터를 받아오기

		return "accountPage/AccountPage";
	}

	@GetMapping("/account/add")
	public String accountAddPage(HttpServletRequest request) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}

		return "accountPage/AccountPage";
	}
}

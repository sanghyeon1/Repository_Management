package com.sims.SIMS.controller;

import static com.sims.SIMS.controller.SocketPython.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class InsertController {

	@GetMapping("/insert")
	public String accountPage(HttpServletRequest request) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}
		socketAccess("product," + session.getAttribute("tel"));
		return "insertPage/InsertPage";
	}

	@PostMapping("/insert/income")
	public String accountIncomePage(HttpServletRequest request, IncomeForm form) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}

		return "redirect:/insertPage/InsertPage";
	}
}

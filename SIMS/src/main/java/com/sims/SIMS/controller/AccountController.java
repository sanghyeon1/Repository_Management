package com.sims.SIMS.controller;

import static com.sims.SIMS.controller.SocketPython.*;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.sims.SIMS.domain.Log;
import com.sims.SIMS.service.LogService;

@Controller
public class AccountController {
	private final LogService logService;

	public AccountController(LogService logService) {
		this.logService = logService;
	}

	@GetMapping("/account")
	public String accountPage(HttpServletRequest request) throws Exception{
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}
		// 쿼리문으로 가계부 데이터를 받아오기
		socketAccess("account");
		return "accountPage/AccountPage";
	}

	@GetMapping("/test")
	public String testPage(Model model) {
		List<Log> logs = logService.findLogsOnlyThirty();
		model.addAttribute("logs", logs);
		return "testPage";
	}
}

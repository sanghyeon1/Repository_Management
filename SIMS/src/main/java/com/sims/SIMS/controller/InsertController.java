package com.sims.SIMS.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class InsertController {

	@GetMapping("/insert")
	public String accountPage() {
		return "insertPage/InsertPage";
	}
}

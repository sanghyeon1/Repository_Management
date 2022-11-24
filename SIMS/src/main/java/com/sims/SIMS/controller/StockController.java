package com.sims.SIMS.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class StockController {
	@GetMapping("/stock")
	public String accountPage() {
		return "stockPage/StockPage";
	}
}

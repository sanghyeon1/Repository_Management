package com.sims.SIMS.controller;

import java.util.List;
import java.util.Optional;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.sims.SIMS.domain.Account;
import com.sims.SIMS.domain.AccountPredict;
import com.sims.SIMS.domain.Log;
import com.sims.SIMS.domain.Product;
import com.sims.SIMS.domain.ProductSales;
import com.sims.SIMS.domain.ProductSalesPredict;
import com.sims.SIMS.service.AccountPredictService;
import com.sims.SIMS.service.AccountService;
import com.sims.SIMS.service.LogService;
import com.sims.SIMS.service.ProductSalesPredictService;
import com.sims.SIMS.service.ProductSalesService;
import com.sims.SIMS.service.ProductService;

@Controller
public class TestController {
	private final LogService logService;
	private final ProductService productService;
	private final ProductSalesPredictService productSalesPredictService;
	private final AccountPredictService accountPredictService;
	private final AccountService accountService;
	private final ProductSalesService productSalesService;

	public TestController(LogService logService, ProductService productService,
		ProductSalesPredictService productSalesPredictService, AccountPredictService accountPredictService,
		AccountService accountService, ProductSalesService productSalesService) {
		this.logService = logService;
		this.productService = productService;
		this.productSalesPredictService = productSalesPredictService;
		this.accountPredictService = accountPredictService;
		this.accountService = accountService;
		this.productSalesService = productSalesService;
	}

	@GetMapping("/test")
	public String testPage(Model model, HttpServletRequest request) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}
		String tel = String.valueOf(session.getAttribute("tel"));

		List<Log> logs = logService.findSellLogsOnlyThirty(tel);
		model.addAttribute("logs", logs);

		List<Product> products = productService.findProducts();
		model.addAttribute("products", products);

		Optional<ProductSalesPredict> productSalesPredict = productSalesPredictService.findProductPredictByCode("PEA6_16800_3", tel);
		if (productSalesPredict.isPresent()) {
			model.addAttribute("productSalesPredict", productSalesPredict.get());
		}

		Optional<AccountPredict> accountPredict = accountPredictService.findAccountPredict(tel);
		if (accountPredict.isPresent()) {
			model.addAttribute("accountPredict", accountPredict.get());
		}

		List<Account> accounts = accountService.findRecent10Account(tel);
		model.addAttribute("accounts", accounts);

		List<ProductSales> productSales = productSalesService.findRecent10ProductSales("PEA6_16800_3", tel);
		model.addAttribute("productSales", productSales);

		return "testPage";
	}
}

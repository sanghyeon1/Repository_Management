package com.sims.SIMS.controller;

import java.util.List;

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
	public String testPage(Model model) {
		List<Log> logs = logService.findLogsOnlyThirty();
		List<Product> products = productService.findProducts();
		List<ProductSalesPredict> productSalesPredicts = productSalesPredictService.findProductPredict();
		List<AccountPredict> accountPredicts = accountPredictService.findAccountPredict();
		List<Account> accounts = accountService.findRecent10Account();
		List<ProductSales> productSales = productSalesService.findRecent10ProductSales();
		model.addAttribute("logs", logs);
		model.addAttribute("products", products);
		model.addAttribute("productPredicts", productSalesPredicts);
		model.addAttribute("accountPredicts", accountPredicts);
		model.addAttribute("accounts", accounts);
		model.addAttribute("productSales", productSales);
		return "testPage";
	}
}

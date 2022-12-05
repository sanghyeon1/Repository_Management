package com.sims.SIMS.controller;

import java.util.List;
import java.util.Optional;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.sims.SIMS.domain.Account;
import com.sims.SIMS.domain.AccountPredict;
import com.sims.SIMS.domain.Product;
import com.sims.SIMS.domain.ProductSales;
import com.sims.SIMS.domain.ProductSalesPredict;
import com.sims.SIMS.domain.ProductStock;
import com.sims.SIMS.service.AccountPredictService;
import com.sims.SIMS.service.AccountService;
import com.sims.SIMS.service.ProductSalesPredictService;
import com.sims.SIMS.service.ProductSalesService;
import com.sims.SIMS.service.ProductService;
import com.sims.SIMS.service.ProductStockService;

@Controller
public class StockController {
	private final ProductService productService;
	private final ProductSalesService productSalesService;
	private final ProductSalesPredictService productSalesPredictService;
	private final AccountService accountService;
	private final AccountPredictService accountPredictService;
	private final ProductStockService productStockService;
	private String selectedProductName = "감바스_알_아히요";

	public StockController(ProductService productService, ProductSalesService productSalesService,
		ProductSalesPredictService productSalesPredictService, AccountService accountService, AccountPredictService accountPredictService, ProductStockService productStockService) {
		this.productService = productService;
		this.productSalesService = productSalesService;
		this.productSalesPredictService = productSalesPredictService;
		this.accountService = accountService;
		this.accountPredictService = accountPredictService;
		this.productStockService = productStockService;
	}

	@GetMapping("/stock")
	public String accountPage(HttpServletRequest request, Model model) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}
		String tel = String.valueOf(session.getAttribute("tel"));

		Optional<AccountPredict> accountPredict = accountPredictService.findAccountPredict(tel);
		if (accountPredict.isPresent()) {
			model.addAttribute("accountPredict", accountPredict.get());
		}

		List<Account> accounts = accountService.findRecent10Account(tel);
		model.addAttribute("accounts", accounts);

		List<Product> products = productService.findProducts();
		model.addAttribute("products", products);

		String selectedProductCode = null;
		for (Product product: products) {
			if (product.getName().equals(selectedProductName)) {
				selectedProductCode = product.getProductCode();
				break;
			}
		}
		model.addAttribute("selectedProductName", selectedProductName);
		List<ProductSales> productSales = productSalesService.findRecent10ProductSales(selectedProductCode, tel);
		model.addAttribute("productSales", productSales);
		Optional<ProductSalesPredict> productSalesPredict = productSalesPredictService.findProductPredictByCode(selectedProductCode, tel);
		if (productSalesPredict.isPresent()) {
			model.addAttribute("productSalesPredict", productSalesPredict.get());
		}
		Optional<ProductStock> productStock = productStockService.findByProductCode(selectedProductCode, tel);
		if (productStock.isPresent()) {
			model.addAttribute("productStock", productStock.get());
		}
		return "stockPage/StockPage";
	}

	@PostMapping("/stock/select")
	public String stockSelectPage(HttpServletRequest request, StockForm form) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}
		selectedProductName = form.getProduct();
		return "redirect:/stock";
	}
}

package com.sims.SIMS.controller;

import static com.sims.SIMS.controller.SocketPython.*;

import java.util.List;
import java.util.Optional;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.sims.SIMS.domain.Log;
import com.sims.SIMS.domain.Product;
import com.sims.SIMS.service.LogService;
import com.sims.SIMS.service.ProductService;

@Controller
public class InsertController {
	private final ProductService productService;
	private final LogService logService;

	public InsertController(ProductService productService, LogService logService) {
		this.productService = productService;
		this.logService = logService;
	}

	@GetMapping("/insert")
	public String insertPage(HttpServletRequest request, Model model) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}
		List<Product> products = productService.findProducts();
		model.addAttribute("products", products);
		return "insertPage/InsertPage";
	}

	@PostMapping("/insert/new")
	public String insertIncomePage(HttpServletRequest request, InsertForm form) {
		HttpSession session = request.getSession(false);
		if (session == null) {
			return "/mainPage/MainPage";
		}
		String tel = String.valueOf(session.getAttribute("tel"));

		Optional<Product> product = productService.findProductByProductName(form.getProduct());

		Log log = new Log();
		log.setAmount(form.getAmount());
		log.setDate(form.getDate());
		log.setTel(tel);
		log.setType(form.getType());
		log.setId(null);
		System.out.println(tel);
		if (product.isPresent()) {
			log.setProductCode(product.get().getProductCode());
		}

		logService.join(log);
		socketAccess("updateAccount," + tel);
		socketAccess("account," + tel);
		if (form.getType().equals("sell")) {
			socketAccess("updateProductSales," + tel);
			socketAccess("product," + tel);
		}
		return "redirect:/insert";
	}
}

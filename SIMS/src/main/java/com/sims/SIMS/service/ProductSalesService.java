package com.sims.SIMS.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.sims.SIMS.domain.Log;
import com.sims.SIMS.domain.ProductSales;
import com.sims.SIMS.repository.ProductRepository;
import com.sims.SIMS.repository.ProductSalesRepository;

@Service
public class ProductSalesService {
	private final ProductSalesRepository productSalesRepository;

	public ProductSalesService(ProductSalesRepository productSalesRepository) {
		this.productSalesRepository = productSalesRepository;
	}

	public List<ProductSales> findProductSales() {
		return productSalesRepository.findAll();
	}

	public List<ProductSales> findRecent10ProductSales() {
		return productSalesRepository.findRecent10();
	}

	public Optional<ProductSales> findOne(Long productSalesId) {
		return productSalesRepository.findById(productSalesId);
	}
}

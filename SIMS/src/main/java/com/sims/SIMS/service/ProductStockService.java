package com.sims.SIMS.service;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.sims.SIMS.domain.ProductStock;
import com.sims.SIMS.repository.ProductStockRepository;

@Service
public class ProductStockService {
	private final ProductStockRepository productStockRepository;

	public ProductStockService(ProductStockRepository productStockRepository) {
		this.productStockRepository = productStockRepository;
	}

	public Optional<ProductStock> findByProductCode(String productCode, String tel) {
		return productStockRepository.findByProductCode(productCode, tel);
	}
}

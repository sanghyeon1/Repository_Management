package com.sims.SIMS.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.sims.SIMS.domain.ProductSalesPredict;
import com.sims.SIMS.repository.ProductSalesPredictRepository;

@Service
public class ProductSalesPredictService {
	private final ProductSalesPredictRepository productSalesPredictRepository;

	public ProductSalesPredictService(ProductSalesPredictRepository productSalesPredictRepository) {
		this.productSalesPredictRepository = productSalesPredictRepository;
	}

	public List<ProductSalesPredict> findProductPredict() {
		return productSalesPredictRepository.findAll();
	}

	public Optional<ProductSalesPredict> findProductPredictByCode(String productCode, String tel) {
		return productSalesPredictRepository.findByName(productCode, tel);
	}

	public Optional<ProductSalesPredict> findOne(Long productPredictId) {
		return productSalesPredictRepository.findById(productPredictId);
	}


}

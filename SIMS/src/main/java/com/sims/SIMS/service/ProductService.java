package com.sims.SIMS.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.sims.SIMS.domain.Product;
import com.sims.SIMS.repository.ProductRepository;

@Service
public class ProductService {
	private final ProductRepository productRepository;

	public ProductService(ProductRepository productRepository) {
		this.productRepository = productRepository;
	}

	public Optional<Product> findProductByProductCode(String productCode) {
		return productRepository.findByProductCode(productCode);
	}

	public Optional<Product> findProductByProductName(String productName) {
		return productRepository.findByName(productName);
	}

	public List<Product> findProducts() {
		return productRepository.findAll();
	}

	public Optional<Product> findOne(Long productId) {
		return productRepository.findById(productId);
	}
}

package com.sims.SIMS.repository;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.Product;

@Repository
public class ProductRepository {
	private static Map<Long, Product> store = new HashMap<>();
	private static long sequence = 0l;

	public Product save(Product product) {
		product.setId(++sequence);
		store.put(product.getId(), product);
		return product;
	}

	public Optional<Product> findById(Long id) {
		return Optional.ofNullable(store.get(id));
	}

	public Optional<Product> findByName(String name) {
		return store.values().stream()
			.filter(product -> product.getName().equals(name))
			.findAny();
	}

	public List<Product> findAll() {
		return new ArrayList<>(store.values());
	}

	public void clearStore() {
		store.clear();
	}
}

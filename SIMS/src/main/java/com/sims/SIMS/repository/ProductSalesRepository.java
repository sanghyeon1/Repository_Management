package com.sims.SIMS.repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.Log;
import com.sims.SIMS.domain.ProductSales;

@Repository
public class ProductSalesRepository {
	private final EntityManager em;

	public ProductSalesRepository(EntityManager em) {
		this.em = em;
	}

	public Optional<ProductSales> findById(Long user_id) {
		ProductSales productSales = em.find(ProductSales.class, user_id);
		return Optional.ofNullable(productSales);
	}

	public List<ProductSales> findAll() {
		return em.createQuery("select m from ProductSales m", ProductSales.class)
			.getResultList();
	}

	public List<ProductSales> findRecent10() {
		List<ProductSales> productSales = em.createQuery("select m from ProductSales m order by m.date desc", ProductSales.class)
			.getResultList();
		List<ProductSales> result = new ArrayList<>();
		for (int i = 0; i < 10; i++) {
			result.add(productSales.get(i));
		}
		return result;
	}
}

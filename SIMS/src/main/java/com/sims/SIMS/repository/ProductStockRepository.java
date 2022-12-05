package com.sims.SIMS.repository;

import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.Product;
import com.sims.SIMS.domain.ProductStock;

@Repository
public class ProductStockRepository {
	private final EntityManager em;

	public ProductStockRepository(EntityManager em) {
		this.em = em;
	}

	public Optional<ProductStock> findByProductCode(String productCode, String tel) {
		List<ProductStock> result = em.createQuery("select m from ProductStock m where m.productCode = :productCode and m.tel = :tel", ProductStock.class)
			.setParameter("productCode", productCode)
			.setParameter("tel", tel)
			.getResultList();
		return result.stream().findAny();
	}
}

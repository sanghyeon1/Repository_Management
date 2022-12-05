package com.sims.SIMS.repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.Log;
import com.sims.SIMS.domain.ProductSales;
import com.sims.SIMS.domain.ProductSalesPredict;

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

	public Optional<ProductSales> findByName(String name) {
		List<ProductSales> result = em.createQuery("select m from ProductSales m where m.name = :name", ProductSales.class)
			.setParameter("name", name)
			.getResultList();
		return result.stream().findAny();
	}

	public List<ProductSales> findRecent10(String productCode, String tel) {
		List<ProductSales> productSales = em.createQuery("select m from ProductSales m where m.name = :productCode and m.tel = :tel order by m.date desc", ProductSales.class)
			.setParameter("productCode", productCode)
			.setParameter("tel", tel)
			.getResultList();
		List<ProductSales> result = new ArrayList<>();
		int i = 0;
		for (ProductSales productSale : productSales) {
			if (i < 5) {
				result.add(productSale);
			}
			i++;
		}
		return result;
	}
}

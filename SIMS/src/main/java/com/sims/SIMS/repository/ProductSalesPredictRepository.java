package com.sims.SIMS.repository;

import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.ProductSales;
import com.sims.SIMS.domain.ProductSalesPredict;

@Repository
public class ProductSalesPredictRepository {
	private final EntityManager em;

	public ProductSalesPredictRepository(EntityManager em) {
		this.em = em;
	}

	public ProductSalesPredict save(ProductSalesPredict productSalesPredict) {
		em.persist(productSalesPredict);
		return productSalesPredict;
	}

	public Optional<ProductSalesPredict> findById(Long id) {
		ProductSalesPredict productSalesPredict = em.find(ProductSalesPredict.class, id);
		return Optional.ofNullable(productSalesPredict);
	}

	public Optional<ProductSalesPredict> findByName(String name, String tel) {
		List<ProductSalesPredict> result = em.createQuery("select m from ProductSalesPredict m where m.name = :name and m.tel = :tel", ProductSalesPredict.class)
			.setParameter("name", name)
			.setParameter("tel", tel)
			.getResultList();
		return result.stream().findAny();
	}

	public List<ProductSalesPredict> findAll() {
		return em.createQuery("select m from ProductSalesPredict m", ProductSalesPredict.class)
			.getResultList();
	}
}

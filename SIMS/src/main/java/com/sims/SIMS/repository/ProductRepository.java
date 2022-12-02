package com.sims.SIMS.repository;

import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.springframework.stereotype.Repository;

import com.sims.SIMS.domain.Product;

@Repository
public class ProductRepository {
	private final EntityManager em;

	public ProductRepository(EntityManager em) {
		this.em = em;
	}

	public Product save(Product product) {
		em.persist(product);
		return product;
	}

	public Optional<Product> findById(Long id) {
		Product product = em.find(Product.class, id);
		return Optional.ofNullable(product);
	}

	public Optional<Product> findByName(String name) {
		List<Product> result = em.createQuery("select m from Product m where m.name = :name", Product.class)
			.setParameter("name", name)
			.getResultList();
		return result.stream().findAny();
	}

	public List<Product> findAll() {
		return em.createQuery("select m from Product m", Product.class)
			.getResultList();
	}
}

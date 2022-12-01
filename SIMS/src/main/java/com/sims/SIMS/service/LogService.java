package com.sims.SIMS.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.expression.spel.ast.OpAnd;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.sims.SIMS.domain.Log;
import com.sims.SIMS.repository.LogRepository;

@Service
public class LogService {
	private final LogRepository logRepository;

	public LogService(LogRepository logRepository) {
		this.logRepository = logRepository;
	}

	public Long join(Log log) {
		logRepository.save(log);
		return log.getId();
	}

	public List<Log> findLogs() {
		return logRepository.findAll();
	}

	public List<Log> findLogsOnlyThirty() {
		List<Log> thirtyLogs = new ArrayList<>();
		List<Log> allLogs = logRepository.findAll();
		for (int i = 0; i < 30; i++) {
			thirtyLogs.add(allLogs.get(i));
		}
		return thirtyLogs;
	}

	public Optional<Log> findOne(Long logId) {
		return logRepository.findById(logId);
	}
}

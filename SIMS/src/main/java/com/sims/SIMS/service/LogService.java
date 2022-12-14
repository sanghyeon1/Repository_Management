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
@Transactional
public class LogService {
	private final LogRepository logRepository;

	public LogService(LogRepository logRepository) {
		this.logRepository = logRepository;
	}

	public Long join(Log log) {
		logRepository.save(log);
		return log.getId();
	}

	public List<Log> findLogs(String tel) {
		return logRepository.findAll(tel);
	}

	public List<Log> findBuyLogsOnlyThirty(String tel) {
		List<Log> allLogs = logRepository.findBuyLogs(tel);
		List<Log> thirtyLogs = new ArrayList<>();
		int i = 0;
		for (Log log : allLogs) {
			if (i < 30) {
				thirtyLogs.add(log);
			}
			i++;
		}
		return thirtyLogs;
	}

	public List<Log> findSellLogsOnlyThirty(String tel) {
		List<Log> allLogs = logRepository.findSellLogs(tel);
		List<Log> thirtyLogs = new ArrayList<>();
		int i = 0;
		for (Log log : allLogs) {
			if (i < 30) {
				thirtyLogs.add(log);
			}
			i++;
		}
		return thirtyLogs;
	}

	public Optional<Log> findOne(Long logId) {
		return logRepository.findById(logId);
	}
}

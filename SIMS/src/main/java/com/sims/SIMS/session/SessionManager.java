package com.sims.SIMS.session;

import java.util.Arrays;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class SessionManager {
	private static final String SESSION_COOKIE_NAME = "mySessionId";
	private Map<String, Object> sessionStore = new ConcurrentHashMap<>();

	public void createSession(Object value, HttpServletResponse response) {
		String sessionId = UUID.randomUUID().toString();
		sessionStore.put(sessionId, value);

		Cookie mySessionCookie = new Cookie(SESSION_COOKIE_NAME, sessionId);
		response.addCookie(mySessionCookie);
	}

	//세션 조회
	public Object getSession(HttpServletRequest request) {
		Cookie sessionCookie = findCookie(request, SESSION_COOKIE_NAME);
		if (sessionCookie == null) return null;
		return sessionStore.get(sessionCookie.getValue());
	}

	// 세션 만료
	public void expire(HttpServletRequest request) {
		Cookie sessionCookie = findCookie(request, SESSION_COOKIE_NAME);
		if (sessionCookie != null) {
			sessionStore.remove(sessionCookie.getValue());
		}
	}

	// 쿠키 조회
	public Cookie findCookie(HttpServletRequest request, String cookieName) {
		Cookie[] cookies = request.getCookies();
		if (cookies == null) {
			return null;
		}
		return Arrays.stream(request.getCookies())
			.filter(cookie -> cookie.getName().equals(cookieName))
			.findAny().orElse(null);
	}
}

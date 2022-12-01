package com.sims.SIMS.controller;

import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class SocketPython {

	public static void socketAccess(String message) {
		// 소켓을 선언한다.
		try (Socket client = new Socket()) {
			// 소켓에 접속하기 위한 접속 정보를 선언한다.
			InetSocketAddress ipep = new InetSocketAddress("127.0.0.1", 9999);
			// 소켓 접속!
			client.connect(ipep);
			// 소켓이 접속이 완료되면 inputstream과 outputstream을 받는다.
			try (OutputStream sender = client.getOutputStream(); InputStream receiver = client.getInputStream();) {
				String msg = message;
				byte[] data = msg.getBytes();
				ByteBuffer b = ByteBuffer.allocate(4);
				b.order(ByteOrder.LITTLE_ENDIAN);
				b.putInt(data.length);
				sender.write(b.array(), 0, 4);
				sender.write(data);

				data = new byte[4];
				receiver.read(data, 0, 4);
				b = ByteBuffer.wrap(data);
				b.order(ByteOrder.LITTLE_ENDIAN);
				int length = b.getInt();
				data = new byte[length];
				receiver.read(data, 0, length);

				msg = new String(data, "UTF-8");
				System.out.println(msg);
			}
		} catch (Throwable e) {
			e.printStackTrace();
		}
	}
}

data = [
    {
        "deviceName": "Wildfly#1",
        "type": "Application",
        "vendor": "Jboss",
        "osType": "Wildfly",
        "osVersion": "23.04",
        "command": "server.log",
        "contents": """Caused by: java.net.ConnectException: Connection timed out (Connection timed out)
at java.base/java.net.PlainSocketImpl.socketConnect(Native Method)
at java.base/java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:399)
at java.base/java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:242)
at java.base/java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:224)
at java.base/java.net.SocksSocketImpl.connect(SocksSocketImpl.java:403)
at java.base/java.net.Socket.connect(Socket.java:609)
at org.postgresql.core.PGStream.createSocket(PGStream.java:231)
at org.postgresql.core.PGStream.<init>(PGStream.java:95)
at org.postgresql.core.v3.ConnectionFactoryImpl.openConnectionImpl(ConnectionFactoryImpl.java:183)
... 32 more"""
    }
]
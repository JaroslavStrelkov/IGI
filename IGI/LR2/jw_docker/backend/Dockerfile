FROM tomcat:9.0-jdk11-openjdk-slim

RUN apt-get update && apt-get install -y \ git \ maven \ wget \ && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/tuchg/SimpleJWManageSystem.git /tmp/project

RUN mkdir -p /usr/local/tomcat/webapps/ROOT && \ cp -r /tmp/project/Backend/2_11_JWCSystem/* /usr/local/tomcat/webapps/ROOT/

WORKDIR /usr/local/tomcat/webapps/ROOT

RUN mkdir -p WEB-INF/lib

RUN wget https://repo1.maven.org/maven2/com/google/code/gson/gson/2.8.9/gson-2.8.9.jar -O WEB-INF/lib/gson-2.8.9.jar && \
    wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.33/mysql-connector-java-8.0.33.jar -O WEB-INF/lib/mysql-connector-java-8.0.33.jar || true && \
    if [ ! -f WEB-INF/lib/mysql-connector-java-8.0.33.jar ]; then \
        wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.28/mysql-connector-java-8.0.28.jar -O WEB-INF/lib/mysql-connector-java-8.0.28.jar; \
    fi

RUN find src -name "*.java" > sources.txt && \
    javac -cp "WEB-INF/lib/*:/usr/local/tomcat/lib/*" -d WEB-INF/classes @sources.txt || true
 
RUN if [ ! -f WEB-INF/web.xml ]; then \
    mkdir -p WEB-INF && \
    printf '<?xml version="1.0" encoding="UTF-8"?>\n<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee\n                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"\n         version="4.0">\n    <display-name>JWC System</display-name>\n</web-app>' > WEB-INF/web.xml; \
    fi

CMD ["catalina.sh", "run"]
package cn.wchihc.jwc.dao.base;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseHelper {
    public static final String DATABASE = "JWC";

    static {
        //全局注册驱动
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static Connection getConn() {
        Connection conn = null;
        try {
            // Читаем параметры из переменных окружения (которые передаст Docker)
            String dbHost = System.getenv().getOrDefault("DB_HOST", "localhost");
            String dbPort = System.getenv().getOrDefault("DB_PORT", "3306");
            String dbName = System.getenv().getOrDefault("DB_NAME", "JWC");
            String dbUser = System.getenv().getOrDefault("DB_USER", "root");
            String dbPassword = System.getenv().getOrDefault("DB_PASSWORD", "a123456");
            
            String url = "jdbc:mysql://" + dbHost + ":" + dbPort + "/" + dbName 
                        + "?useUnicode=true&characterEncoding=UTF8&serverTimezone=UTC";
            
            System.out.println("Подключение к БД: " + url); // Для отладки
            conn = DriverManager.getConnection(url, dbUser, dbPassword);
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return conn;
    }
}
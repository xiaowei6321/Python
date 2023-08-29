package com.example.demo.repository;

import java.sql.*;

public class MySQLFramework {
    private Connection connection;
    private String url;
    private String username;
    private String password;

    public MySQLFramework(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    public void connect() throws SQLException {
        connection = DriverManager.getConnection(url, username, password);
    }

    public void disconnect() throws SQLException {
        if (connection != null) {
            connection.close();
        }
    }

    public ResultSet executeQuery(String query) throws SQLException {
        Statement statement = connection.createStatement();
        return statement.executeQuery(query);
    }

    public int executeUpdate(String query) throws SQLException {
        Statement statement = connection.createStatement();
        return statement.executeUpdate(query);
    }

    public static void main(String[] args) {
        MySQLFramework framework = new MySQLFramework("jdbc:mysql://localhost:3306/test", "root", "123456");

        try {
            framework.connect();

            // 执行查询
            String query = "SELECT * FROM users";
            ResultSet resultSet = framework.executeQuery(query);

            // 处理查询结果
            while (resultSet.next()) {
                // 从结果集中获取数据
                int id = resultSet.getInt("userId");
                String name = resultSet.getString("username");
                // ... 其他列

                // 打印数据
                System.out.println("ID: " + id + ", Name: " + name);
            }

//            // 执行更新操作
//            String updateQuery = "UPDATE table_name SET name = 'New Name' WHERE id = 1";
//            int rowsAffected = framework.executeUpdate(updateQuery);
//            System.out.println("Rows affected: " + rowsAffected);

            framework.disconnect();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}


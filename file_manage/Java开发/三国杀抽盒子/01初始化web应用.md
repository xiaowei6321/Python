博客系统

构建maven项目
pom.xml
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <!-- 项目基本信息 -->
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>myproject</artifactId>
    <version>1.0.0</version>

    <!-- 项目描述 -->
    <name>My Project</name>
    <description>This is a sample project.</description>

    <!-- 项目构建配置 -->
    <build>
        <plugins>
            <!-- 插件配置 -->
        </plugins>
    </build>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <!-- <version>2.5.2</version> -->
        <version>2.5.2</version>
    </parent>

    <!-- 项目依赖配置 -->
    <dependencies>
        <!-- 依赖配置 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--        -->


    </dependencies>

</project>


```

src
├── main
│   ├── java
│   │   └── com
│   │       └── example
│   │           └── demo
│   │               ├── controller
│   │               ├── model
│   │               ├── repository
│   │               ├── service
│   │               └── DemoApplication.java
│   └── resources
│       ├── static
│       ├── templates
│       └── application.properties
└── test
    └── java
        └── com
            └── example
                └── demo
                    ├── controller
                    ├── repository
                    └── service

src/main/java/com/example/demo/DemoApplication.java
```java
package com.example.demo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

src/main/resources/application.properties
```properties

```

src/main/java/com/example/demo/controller/HelloController.java
```java
package com.example.demo.controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
public class HelloController {
    @RequestMapping("/hello")
    public String index() {
        return "Hello World";
    }
}
```


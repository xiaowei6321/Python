Spring Boot是一个基于Spring Framework的框架，它可以大大简化Spring应用程序的创建和配置。而Thymeleaf是一个Java模板引擎，用于在Web和独立环境中处理XML/XHTML/HTML5内容。

以下是一些使用Spring Boot和Thymeleaf入门的步骤：

**1. 创建Spring Boot项目**

最简单的方法是使用[Spring Initializr](https://start.spring.io/)在线工具，你只需要选择Web和Thymeleaf的依赖项即可。这个工具会帮助你创建一个包含基础文件和代码的新项目。

**2. 添加Thymeleaf依赖**

如果你没有通过Spring Initializr创建项目，你可以手动在`pom.xml`文件中添加Thymeleaf的依赖：

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

**3. 创建一个Controller**

接下来，你可以创建一个Spring MVC的Controller。Controller是用于处理用户请求的类。以下是一个简单的Controller：

src/main/java/com/example/demo/controller/HelloController.java
```java
package com.example.demo.controller;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {
    @GetMapping("/hello")
    public String sayHello(Model model) {
        model.addAttribute("message", "Hello from Spring Boot and Thymeleaf!");
        return "hello";
    }
}
```

在这个Controller中，我们定义了一个处理`/hello`路径的GET请求的方法`sayHello`。这个方法添加了一个属性到Model对象，然后返回视图名"hello"。

**4. 创建一个Thymeleaf模板**

Thymeleaf模板默认应该放在`src/main/resources/templates`目录下。以下是一个基础的`hello.html`模板：

src/main/resources/templates/hello.html
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Hello</title>
</head>
<body>
    <h1 th:text="${message}">Hello, World!</h1>
</body>
</html>
```

在这个模板中，我们使用Thymeleaf的`th:text`属性来设置h1标签的文本内容为Model中的message属性。

**5. 运行你的应用**

如果你的项目是一个Maven项目，你可以使用以下命令来运行你的应用：

```bash
./mvnw spring-boot:run
```

然后，你可以在浏览器中打开`http://localhost:8080/hello`来看到你的应用。

以上就是使用Spring Boot和Thymeleaf的基础入门。有许多其他的特性和技术你可能想要探索，例如如何使用Spring Boot的自动配置，如何使用Spring Data JPA和Hibernate访问数据库，如何使用Spring Security添加安全和认证，等等。

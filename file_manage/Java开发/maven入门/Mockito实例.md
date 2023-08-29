好的，我将为您提供一个使用Mockito的简单示例。

假设您有一个名为`Calculator`的类，其中包含一个`add()`方法用于将两个数字相加。现在，您想要编写一个单元测试来验证`Calculator`类的行为。由于测试中不依赖于实际的依赖项，您可以使用Mockito来模拟这些依赖项。

首先，让我们看一下`Calculator`类的代码：

src/main/java/com/example/Calculator.java
```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}
```

接下来，我们将使用Mockito来创建一个模拟对象并验证`add()`方法的行为。这里是一个简单的示例：

src/test/java/com/example/CalculatorMockitoTest.java
```java
import org.junit.jupiter.api.Test;
import static org.mockito.Mockito.*;

public class CalculatorTest {
    @Test
    public void testAdd() {
        // 创建 Calculator 的模拟对象
        Calculator calculator = mock(Calculator.class);

        // 定义模拟对象的行为
        when(calculator.add(2, 3)).thenReturn(5);

        // 调用被测试的方法
        int result = calculator.add(2, 3);

        // 验证模拟对象的方法是否按预期被调用
        verify(calculator).add(2, 3);

        // 验证结果是否符合预期
        assertEquals(5, result);
    }
}
```


在这个示例中，我们首先使用`mock()`方法创建了`Calculator`类的模拟对象。然后，我们使用`when().thenReturn()`语法定义了模拟对象的行为，即当调用`add(2, 3)`方法时，应该返回`5`。接下来，我们调用了被测试的方法`calculator.add(2, 3)`，并将结果存储在`result`变量中。

最后，我们使用`verify()`方法验证模拟对象的`add(2, 3)`方法是否按预期被调用，以及使用`assertEquals()`方法验证结果是否符合预期。

使用Mockito，您可以轻松地模拟依赖项的行为，并对其进行验证，从而编写可靠的单元测试。请注意，这只是Mockito的一个简单示例，Mockito还提供了更多功能和灵活性，以满足更复杂的测试需求。

@Test的作用
`@Test` 是一个注解，用于标记测试方法。它是JUnit测试框架中的一个重要注解。

当您在使用JUnit进行单元测试时，可以使用`@Test`注解来标记测试方法。这样，JUnit框架将识别这些被标记的方法，并执行它们作为测试用例。

`@Test`注解的作用如下：

1. 标记测试方法：通过在方法上添加`@Test`注解，将该方法标记为一个测试方法。JUnit框架将会执行被标记的方法作为测试用例。

2. 指定预期异常：可以使用`expected`属性来指定测试方法预期抛出的异常。例如，`@Test(expected = SomeException.class)`表示测试方法期望抛出`SomeException`异常，如果没有抛出该异常，测试将失败。

3. 指定超时时间：可以使用`timeout`属性来指定测试方法的最大执行时间（以毫秒为单位）。如果测试方法执行时间超过指定的超时时间，测试将被视为失败。

4. 支持参数化测试：JUnit 4引入了参数化测试的概念，允许使用不同的参数多次运行同一个测试方法。通过在测试方法上添加`@Test`注解，并结合`@RunWith(Parameterized.class)`注解和`@Parameters`注解，可以实现参数化测试。

总之，`@Test`注解是JUnit测试框架中的关键注解之一，用于标记测试方法，并提供了一些额外的功能，如指定预期异常、超时时间和参数化测试等。它使得编写和执行单元测试变得更加简单和方便。


src/test/java/com/example/CalculatorTest.java
```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class CalculatorTest {

    @Test
    public void testAddition() {
        Calculator calculator = new Calculator();
        int result = calculator.add(2, 3);
        assertEquals(5, result);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testDivisionByZero() {
        Calculator calculator = new Calculator();
        calculator.divide(10, 0);
    }

    @Test(timeout = 1000)
    public void testPerformance() {
        // Perform some time-consuming operations
    }
}

```

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

    <!-- 项目依赖配置 -->
    <dependencies>
        <!-- 依赖配置 -->
        
    </dependencies>

</project>


```


下载地址：[junit.jar](https://repo1.maven.org/maven2/junit/junit/4.12/junit-4.12.jar)、[hamcrest.jar](https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar)
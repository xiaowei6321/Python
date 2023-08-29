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

在这种情况下，我们可以将验证用户名和密码的逻辑抽取到一个单独的服务中，例如一个名为`UserService`的服务。这可以提高代码的可测试性和重用性。以下是如何整合这样一个服务：

**1. 创建UserService**

首先，创建一个名为`UserService`的类，该类包含一个验证用户名和密码的方法：

```java
import org.springframework.stereotype.Service;

@Service
public class UserService {

    public boolean validateUser(String username, String password) {
        // In a real application, this logic should involve fetching user data from a database or another external service
        return "user".equals(username) && "password".equals(password);
    }
}
```

**2. 修改Controller**

然后，你可以在你的`LoginController`中注入`UserService`，并使用它来验证用户名和密码：

```java
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class LoginController {

    private final UserService userService;

    public LoginController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/login")
    public String login() {
        return "login";
    }

    @PostMapping("/login")
    public String login(@RequestParam("username") String username, @RequestParam("password") String password, Model model) {
        if (userService.validateUser(username, password)) {
            return "dashboard";
        } else {
            model.addAttribute("error", "Invalid username or password.");
            return "login";
        }
    }
}
```

现在，验证用户的逻辑已经被移动到`UserService`中，这使得你可以在其他地方复用这个逻辑，例如在其他的Controller或者在单元测试中。

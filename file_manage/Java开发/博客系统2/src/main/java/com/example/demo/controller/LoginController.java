package com.example.demo.controller;
import com.example.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class LoginController {

    private UserService userService;
    @Autowired
    public LoginController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/login")
    public String login() {
        return "login";
    }

//    @PostMapping("/login")
//    public String login(@RequestParam("username") String username, @RequestParam("password") String password, Model model) {
//        if ("user".equals(username) && "password".equals(password)) {
//            return "dashboard";
//        } else {
//            model.addAttribute("error", "Invalid username or password.");
//            return "login";
//        }
//    }

    @PostMapping("/login")
    public String login(@RequestParam("username")String username,@RequestParam("password")String password,Model model) {
        if(userService.validateUser(username,password)) {
            return "dashboard";
        }else {
            model.addAttribute("error","Invalid username or password.");
            return "login";
        }

    }

    @GetMapping("/register")
    public String register() {
        return "register";
    }

    @PostMapping("/register")
    public String register(@RequestParam("username") String username, @RequestParam("password") String password, Model model) {

//        userService.registerUser(username, password);
//        return "login";
        // 检查是否已存在同名用户
        try {
            userService.registerUser(username, password);
            return "login";
        } catch (Exception e) {
            model.addAttribute("error", "User already exists.");
            return "register";
        }

    }
}

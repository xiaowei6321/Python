package com.example.demo.controller;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("title", "Home Page");
        model.addAttribute("message", "Hello, World!");
        return "home";
    }
    
    @GetMapping("/card-drawing")
    public String cardDrawing(Model model) {
        
        
        return "card-drawing";
    }
}


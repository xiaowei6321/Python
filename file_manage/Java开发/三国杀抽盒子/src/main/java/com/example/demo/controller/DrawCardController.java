package com.example.demo.controller;

import com.example.demo.service.CardService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DrawCardController {

    private final CardService cardService;

    public DrawCardController(CardService cardService) {
        this.cardService = cardService;
    }

    @GetMapping("/draw")
    public String drawCard() {
        //调用服务层的抽卡方法，返回结果
        String result = cardService.drawCard();
        return result;
    }
    @GetMapping("/draw50")
    public String drawCard50() {
        //调用服务层的抽卡方法，返回结果
        String result = cardService.drawCard50();
        return result;
    }
}

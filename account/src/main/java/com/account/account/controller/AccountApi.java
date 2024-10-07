package com.account.account.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.account.account.models.AccountBank;
import com.account.account.service.AccountService;

import lombok.AllArgsConstructor;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;




@RestController
@AllArgsConstructor
@RequestMapping("/usuarios")
public class AccountApi {
    
    private AccountService accountService;

    @PostMapping("/new")
    public AccountBank crearAccountBank(
        @RequestParam(value="name")String name,
        @RequestParam(value="apellidos")String apellidos,
        @RequestParam(value="genero")String genero,
        @RequestParam(value="email")String email){
            if (genero.equals("F") || genero.equals("M")) {
            AccountBank accountBank = new AccountBank(null, null, null,name, apellidos, genero, email);
            return accountService.createAccount(accountBank);
        }
            return null;
    }

    @PutMapping("/{id}")
    public AccountBank putAccountBank (@PathVariable("id") Long id,
        @RequestParam(value="name") String name,
        @RequestParam(value="apellidos")String apellidos,
        @RequestParam(value="genero")String genero,
        @RequestParam(value="email")String email){
            if (genero.equals("F") || genero.equals("M")) {
            AccountBank accountBank = new AccountBank(null, null, null, name, apellidos, genero, email);
            accountBank.setId(id);
            return accountService.updateAccount(accountBank);
        }
            return null;
        
        }

    @GetMapping("")
    public List<AccountBank> verCuentas (){
        return accountService.showAll();
    }   
    
    @DeleteMapping("/{id}")
    public void eliminarAccount(@PathVariable("id")Long id){
        accountService.deleteAccount(id);
    }


}
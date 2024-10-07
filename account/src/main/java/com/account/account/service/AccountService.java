package com.account.account.service;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.account.account.models.AccountBank;
import com.account.account.repository.AccountRepository;

@Service
public class AccountService {

    private final AccountRepository accountRepository;

    public AccountService(AccountRepository accountRepository) {
        this.accountRepository = accountRepository;
    }

    //see all the list

    public List<AccountBank> showAll(){
        return accountRepository.findAll();
    }

    //see an account by id

    public AccountBank findAccount (Long id){
        return accountRepository.findById(id).orElse(null);
    }

    //see by genre

    public List<AccountBank> findGenre(String genero){
        return accountRepository.findByGenero(genero);
    }

    //create a new account

    public AccountBank createAccount(AccountBank accountBank){
        return accountRepository.save(accountBank);
    }

    //update an accountBank

    public AccountBank updateAccount (AccountBank accountBank){
        return accountRepository.save(accountBank);
    }

    //delete an accountBank

    public void deleteAccount (Long id){
        accountRepository.deleteById(id);
    }
    
}

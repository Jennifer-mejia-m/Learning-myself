package com.account.account.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.account.account.models.AccountBank;

@Repository
public interface AccountRepository extends CrudRepository<AccountBank, Long>{

    List<AccountBank>findAll();
    Optional<AccountBank>findById(Long id);
    List<AccountBank> findByGenero(String genero);
    
}

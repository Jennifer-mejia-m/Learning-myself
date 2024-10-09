package com.example.demo.Repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.example.demo.models.Producto;

@Repository
public interface ProductoRepository extends JpaRepository<Producto,Long>{

    List<Producto>findAll();

    @Query("SELECT p FROM Producto p WHERE p.id = :id")
  Optional<Producto> findById(@Param("id")Long id);

    @Query("SELECT p FROM Producto p WHERE p.nombre LIKE %:a")
  List<Producto> findByTerminal(@Param("a")String a);
 
}

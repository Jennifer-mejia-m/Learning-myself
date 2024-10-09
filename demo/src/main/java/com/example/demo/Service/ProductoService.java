package com.example.demo.Service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.example.demo.Repository.ProductoRepository;
import com.example.demo.models.Producto;

@Service
public class ProductoService {

    private final ProductoRepository productoRepository;

    public ProductoService(ProductoRepository productoRepository){
        this.productoRepository = productoRepository;
    }

    //see all the producto list

    public List<Producto> showAll(){
        return productoRepository.findAll();
    }

    //see a product by id

    public Producto findById(Long id){
        return productoRepository.findById(id).orElse(null);
    }

    //create a new product

    public Producto createProducto(Producto producto){
        return productoRepository.save(producto);
    }

    //update a product created

    public Producto updateProducto(Producto producto){
        return productoRepository.save(producto);
    }

    public Optional<Producto> productosTerminal(String a){
        return productoRepository.findByTerminal(a);
    }


    //eliminate a producto

    public void deleteProducto(Long id){
        productoRepository.deleteById(id);
    }
    
}

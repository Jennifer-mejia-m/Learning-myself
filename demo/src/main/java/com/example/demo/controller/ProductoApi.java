package com.example.demo.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.Service.ProductoService;
import com.example.demo.models.Producto;

import lombok.AllArgsConstructor;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;




@RestController
@AllArgsConstructor
@RequestMapping("/productos")
public class ProductoApi {
     
    private ProductoService productoService;

    //create a new product
    @PostMapping("/new")
    public Producto creaProducto(
        @RequestParam(value="nombre")String nombre,
        @RequestParam(value="descripcion")String descripcion,
        @RequestParam(value="precio")Double precio,
        @RequestParam(value="stock")int stock){
            if (precio > 0 && stock > 0) {
                Producto producto = new Producto(null,nombre, descripcion, precio, stock, null,null);
                return productoService.createProducto(producto); 
            }
                return null;
    }

    //update a product
    @PutMapping("/{id}")
    public Producto updateProducto(@PathVariable("id")Long id,
    @RequestParam(value="nombre")String nombre,
        @RequestParam(value="descripcion")String descripcion,
        @RequestParam(value="precio")Double precio,
        @RequestParam(value="stock")int stock){
            if (precio > 0 && stock > 0){
                Producto producto = new Producto(null,nombre, descripcion, precio, stock, null,null);
                producto.setId(id);
                return productoService.createProducto(producto);   
            }
                return null;
    }

    //see all the products
    @GetMapping("")
    public List<Producto> viewAllProducto() {
        return productoService.showAll();
    }

    //see a product by Id

    @GetMapping("/{id}")
    public Producto getProducto(@PathVariable("id")Long id) {
        return productoService.findById(id);
    }
    
    //delete a product

    @DeleteMapping("/{id}")
    public void deleteProduct(@PathVariable("id")Long id){
        productoService.deleteProducto(id);
    }

}

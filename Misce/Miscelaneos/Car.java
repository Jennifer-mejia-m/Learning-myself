package Miscelaneos;

public class Car {
    
    private String make;
    private String model;
    private int year;

    public Car(String make, String model, int year){
        if (make == null || make.isEmpty()) {
            this.make = "unknown make";
        } else {
            this.make = make;
        }
        this.model= (model==null || model.isEmpty()) ? "unknown model": model;
        this.year = (year <= 0) ? 2000:year;
    }

    public static void main(String[] args) {
        
        Car car1 = new Car(null," ",2003);
        System.out.println(car1.make+" "+car1.model+" "+car1.year);
    }

}

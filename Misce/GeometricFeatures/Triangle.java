package GeometricFeatures;

public class Triangle implements Shape{

    private double base;
    private double heigth;

    public Triangle(double base, double heigth){
        this.base=base;
        this.heigth=heigth;
    }

    @Override
    public double getArea() {
        return Math.round((0.5*base*heigth)*100d)/100d;
    }
    
}

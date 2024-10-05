package GeometricFeatures;

public class Circle implements Shape{

    private double radius;

    public Circle(double radius){
        this.radius=radius;
    }

    @Override
    public double getArea() {
        return Math.round((Math.PI*radius*radius)*100d)/100d;
    }
    
}

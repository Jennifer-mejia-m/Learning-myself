package GeometricFeatures;

public class Main {
    
    public static void main(String[] args) {
        
        Rectangle rectangle1 = new Rectangle(8.2, 3);
        Circle circle1 = new Circle(5.5);
        Triangle triangle1 = new Triangle(12.8, 9.4);

        System.out.println("El área del rectángulo es: "+rectangle1.getArea());
        System.out.println(circle1.getArea());
        System.out.println(triangle1.getArea());
    }
}

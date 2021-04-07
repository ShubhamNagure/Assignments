public class ProductManager extends Shop{
	
	
	public Product proFood() {
		return new Food();
	}
	
	public Product proDrink() {
		return new Drink();
	}
  
}

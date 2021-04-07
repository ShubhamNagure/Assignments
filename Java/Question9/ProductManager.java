public class ProductManager extends Shop{
	
	
	public Product proFood() {
		return new Food();
	}
	
	public Product proDrink() {
		return new Drink();
	}
	//this method is subject of 10 question only : is has nothing to do with q9
	public Review rateAndReview(String r) {
		Review rev = null;
		if (r=="X") {
			new Review().oneStar();
		} else if (r=="XX") {
			new Review().twoStar();
		} else if (r=="XXX") {
			new Review().threeStar();
		} else if (r== "XXXX") {
			new Review().fourStar();
		}else if (r == "XXXXX") {
			new Review().fiveStar();
		}else {
			System.out.println("Please rate now !");
		}
		
		
		return null;
	}
  
}

package exception_handling;

import java.util.Scanner;

public class User {

	static double amount= 1000;
	
	public static void main(String[] args) {
		User u =new User();
		Scanner scan =new Scanner(System.in);
		System.out.println("Please enter an amount :");
		double amt =scan.nextDouble();
		try {
			if (amt>amount) {
				throw new InsufficientFundException();
			}else {
				double d = amount- amt;
				System.out.println("Successfully withdraw "+amt +"Rs. available current balance is " +d);
			}
		}catch (InsufficientFundException e) {
			e.printStackTrace();
			System.out.println("amount is not enough to withdraw, available balance is :"+amount);
		}
	}
}

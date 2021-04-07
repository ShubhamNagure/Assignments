import java.util.Scanner;

public class Sports_accessories {
	
	/*Create class called sports_accessories with attributes Accessory_id, description, 
	*quantity, rate, used_in_game. Accept details of 10 accessories from user(5 records), 
	*store it in array of objects. Display details of all accessories used in game cricket.**/
	int Accessory_id, quantity ;
	String description;
	float rate;
	boolean used_in_game;

	public Sports_accessories(int accessory_id, int quantity, String description, float rate, boolean used_in_game) {
		Accessory_id = accessory_id;
		this.quantity = quantity;
		this.description = description;
		this.rate = rate;
		this.used_in_game = used_in_game;
	}

	public static void main(String[] args) {
				
		Sports_accessories [] sa_array ;
		sa_array = new Sports_accessories[5];
		System.out.println("***************You can enter maximum 5 records***************");
		Scanner sc = new Scanner(System.in);
		int j =0;
		while (j<=4) {
			
			System.out.println("Enter Id: \n");
			int A_id = sc.nextInt();
			System.out.println("Enter Quantity: \n");
			int quant = sc.nextInt();
			System.out.println("Enter description: \n");
			String desc = sc.next();
			System.out.println("Enter Rate :\n");
			float rate = sc.nextFloat();
			System.out.println("Enter used/not_used as true/false :\n");
			boolean used_in_game = sc.nextBoolean();
			
			sa_array[j]= new Sports_accessories(A_id, quant, desc, rate, used_in_game);
			j++;
		}
		
		// for loop to iterate over array in order to print it.
		for (int i=0; i < sa_array.length; i++) {
		System.out.println("Accessory_id : " +sa_array[i].Accessory_id + " quantity : " 
			+sa_array[i].quantity + " description : " + sa_array[i].description + 
			" rate : " + sa_array[i].rate + 
			" used_in_game :" + sa_array[i].used_in_game);
		}
		
	}

}

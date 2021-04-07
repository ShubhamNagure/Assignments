public class SeniorCitizens {
	String name;
	
	public static void main(String[] args) {
		SeniorCitizens sc =new SeniorCitizens();
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter Name :");
		
		String name =scan.next();
		System.out.println("Please enter a age :");
		
		int age=scan.nextInt();
	
		try {
			if (age<=60) {
				throw new InvalidAgeException();
			}
		} catch (InvalidAgeException e) {
			e.printStackTrace();
			System.out.println("Age is not valid");
		}
	}
	
}

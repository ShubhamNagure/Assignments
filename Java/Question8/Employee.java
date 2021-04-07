package static_ass;

public class Employee {
	
	/*Define Employee class (name, designation, salary). Define a default and parameterized constructor. 
	*Override the toString method. Keep a count of objects created. Create objects using parameterized constructor 
	*and display the object count after each object is created. (Use static member and method). 
	*Also display the contents of each object.*/
	String name;
	String designation;
	double salary;
	static int objCount =0;
	
	Employee(){
	}

	
	public Employee(String name, String designation, double salary) {
		this.name = name;
		this.designation = designation;
		this.salary = salary;	
	}
	
	{
		objCount++;
	}
	@Override
	public String toString() {
		return "Employee [name=" + name + ", designation=" + designation + ", salary=" + salary + "]";
	}

	public static void main(String[] args) {
		Employee e1= new Employee("Alice", "Analyst", 30000);
		Employee e2= new Employee("Bob", "developer", 45000);
		Employee e3= new Employee("Charlie", "line manager", 75000);
		System.out.println("No of Objects created is : "+objCount);
	}
	
	
	
}

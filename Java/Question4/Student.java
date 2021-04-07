package one;

import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;
/*Create class called sports_accessories with attributes Accessory_id, description, 
 *quantity, rate, used_in_game. 
 *Accept details of 10 accessories from user(5 records), store it in array of objects.
 *Display details of all accessories used in game cricket*/


public class Student {
	int roll_no;
	String Name;
	String sclass;
	int[] marks;
	double per;
	
	public Student(int roll_no, String name, String sclass, int[] marks) {
		this.roll_no = roll_no;
		Name = name;
		this.sclass = sclass;
		this.marks = marks;
	}

	public void per() {
		int tmarks=0;
		
		for (int i=0;i<marks.length;i++){
			tmarks+=marks[i];
		}
		per=tmarks/6;
		
	}
	
	static void sortStudent(Student[] s ) {
	//TODO:implement sorting algorithm here
		
	}

	@Override
	public String toString() {
		return "Student [roll_no=" + roll_no + ", Name=" + Name + ", sclass=" + sclass + ", marks="
				+ Arrays.toString(marks) + ", per=" + per + "]";
	}

	public static void main(String[] args)throws IOException {
		Student s[] = new Student[5];
		int[] marks=new int[6];
		
		
		Scanner sc= new Scanner(System.in);
		for (int i=0; i<1; i++) {
//			System.out.println("Enter roll no of "+ (i+1) + " :");
			System.out.println("Enter roll no of  :");
			int roll =sc.nextInt();
			
			System.out.println("Enter  Student name :");
			String sname=sc.next();
			
			System.out.println("Enter class :");
			String sclass =sc.next();
			
			for(int j=0; j<2; j++) {
				System.out.println("Enter  Marks :" );
				marks[j] =sc.nextInt();
			}
			
			s[i]= new Student(roll,sname,sclass,marks);
			s[i].per();
			
			System.out.println(s[i]);
			
			
			
		}
		
	}
}

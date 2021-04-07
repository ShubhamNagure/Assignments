import mcai.MCAIMarks;
import mcaii.MCAIIMarks;

public class Student {
	int rollNumber;
	String name;
	MCAIMarks mcaimarks;
	MCAIIMarks mcaiimarks;
	

	public Student(int rollNumber, String name, MCAIMarks mcaimarks, MCAIIMarks mcaiimarks) {
		this.rollNumber = rollNumber;
		this.name = name;
		this.mcaimarks = mcaimarks;
		this.mcaiimarks = mcaiimarks;
	}

	public String calGrade(int total) {
		int per= total/4;
		
		if (per>=70) {
			return "A";
		} else if (per<=60 && per>=49) {
			return "B";
		}else if (per<=50 && per>=39) {
			return "C";
		}else if (per<=40) {
			return "FAIL";
		}
		return "Grade not found";
	}
	
	public static void main(String[] args) {
		MCAIMarks mcaimarks=new MCAIMarks(40, 40);
		MCAIIMarks mcaiimarks=new MCAIIMarks(50, 60);	
		
		Student s = new Student(1, "Alice", mcaimarks, mcaiimarks);
		
		int I = mcaimarks.totalMarksI();
		int II = mcaiimarks.totalMarksII();
		
		int total = I+II;
		String grade=s.calGrade(total);
		
		System.out.println("RollNo of Student is "+s.rollNumber+"\n" );
		System.out.println("Name of Student is "+s.name +"\n");
		System.out.println("Grade is: "+grade);	
	}
}

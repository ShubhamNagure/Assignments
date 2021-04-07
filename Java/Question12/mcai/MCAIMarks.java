package mcai;

public class MCAIMarks {
	int SemITotal;
	int SemIITotal;
	
	
	
	public MCAIMarks(int semITotal, int semIITotal) {
		SemITotal = semITotal;
		SemIITotal = semIITotal;
	}



	@Override
	public String toString() {
		return "MCAIMarks [SemITotal=" + SemITotal + ", SemIITotal=" + SemIITotal + "]";
	}
	
	
	public int totalMarksI() {
		int totalMarksI = SemITotal+ SemIITotal;
		return totalMarksI;
	}
	
}

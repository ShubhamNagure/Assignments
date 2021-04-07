package mcaii;

public class MCAIIMarks {
	int SemITotal;
	int SemIITotal;
	
	public MCAIIMarks(int semITotal, int semIITotal) {
		SemITotal = semITotal;
		SemIITotal = semIITotal;
	}

	@Override
	public String toString() {
		return "MCAIIMarks [SemITotal=" + SemITotal + ", SemIITotal=" + SemIITotal + "]";
	}
	
	
	public int totalMarksII() {
		int totalMarksII = SemITotal+ SemIITotal;
		return totalMarksII;
	}
}

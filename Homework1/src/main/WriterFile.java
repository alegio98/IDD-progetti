package main;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Map;

import struttura.Cell;
import struttura.Table;

public class WriterFile {
	
	public void writeOnFile(int querySize, long timeTopKMin, long timeTopKMax, int sizeSet2Count, int matching) {
		try {
			FileWriter myWriter = new FileWriter("provaTmp.txt", true);
			myWriter.write(querySize + ";" + timeTopKMin/(1000F) + ";" + timeTopKMax/(1000F) + ";" + sizeSet2Count + ";" + matching + "\n" );
			myWriter.close();
		}
		catch (IOException e) {
			System.out.println("error");
			e.printStackTrace();
		}
	}
	
	
	public void writeOnFileQuery(int numRows, int k) {
		try {
			FileWriter myWriter = new FileWriter("prova.txt", true);
			myWriter.write("prova: " + "\n query con " + numRows + " righe, con k=" + k + ": \n");
			myWriter.close();
		}
		catch (IOException e) {
			System.out.println("error");
			e.printStackTrace();
		}
	}
	
	
	public void writeOnFileMergedMap(Map<Integer,Integer> orderedSet2count) {
		try {
			FileWriter myWriter = new FileWriter("prova.txt", true);
			for (Integer i : orderedSet2count.keySet()) {
				myWriter.write(i + " = " + orderedSet2count.get(i) + "\n");
			}
			myWriter.close();
		}
		catch (IOException e) {
			System.out.println("error.");
			e.printStackTrace();
		}
	}
	
	/*
	public void writeOnFileTable(Table table, Integer docId) {
		try {
			FileWriter myWriter = new FileWriter("tjn.txt", true);
			myWriter.write("ID del documento: " + docId + "\n");
			for (Integer i : table.getColumnsMap().keySet()) {
				for (Cell c : table.getColumnsMap().get(i)) {
					myWriter.write(c.getCleanedText() + ";");
				}
				myWriter.write("\n");
			}
			myWriter.write("\n");
			myWriter.close();
		}
		catch (IOException e) {
			System.out.println("error");
			e.printStackTrace();
		}
	}
	
	*/
}
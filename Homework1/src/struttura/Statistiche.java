package struttura;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

import org.codehaus.jackson.JsonFactory;
import org.codehaus.jackson.JsonParser;
import org.codehaus.jackson.JsonToken;
import org.codehaus.jackson.annotate.JsonProperty;
import org.codehaus.jackson.map.ObjectMapper;
import org.codehaus.jackson.map.type.TypeFactory;
import org.codehaus.jackson.type.TypeReference;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Statistiche {
	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws Exception {

		BufferedReader br = null;
		JSONParser parser = new JSONParser();

		try {

			// current line of the json file
			String sCurrentLine;

			br = new BufferedReader(new FileReader("/home/alessandro/Scrivania/HW1/tables.json"));

			// mapper to deserialize a json Object to a Java Object
			ObjectMapper objectMapper = new ObjectMapper();

			int numeroTabelle = 0;
			
			int numeroMedioRighe = 0;
			int numeroMedieColonne = 0;
			int numeriNulli =0;
			int numeriValoriDistinti =0;
			
			while((sCurrentLine = br.readLine()) ==null) {
				numeriNulli++;
			}

			
			while ((sCurrentLine = br.readLine()) != null) {

				numeroTabelle++;
				
				Object obj;
				try {
					
					// parser
					obj = parser.parse(sCurrentLine);

					
					Table table = objectMapper.readValue(sCurrentLine, Table.class);
					
					Collection<Cell> cells = objectMapper.readValue(sCurrentLine, new TypeReference<Cell>() {
					});

					table.setCollectionCells(cells);
					
					
					numeroMedieColonne += table.getMaxDimension().getColumn();
					
					numeroMedioRighe += table.getMaxDimension().getRow();


				} catch (ParseException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			 System.out.println("numero di tabelle: " + numeroTabelle);
			 System.out.println("numero totale righe: " + numeroMedioRighe);
			 System.out.println("numero medio righe: " +
			  (int)(numeroMedioRighe/numeroTabelle));
			  
			 System.out.println("numero totale colonne: " + numeroMedieColonne);
			 System.out.println("numero medio colonne: " +
			  (int)(numeroMedieColonne/numeroTabelle));
			 

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)
					br.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
}
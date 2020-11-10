package problems;
import java.util.*;
public class Examquestion {
	static boolean search(String sample,String a[]) {
		int count=0;
			for(String i :a) {
				if(sample.equals(i)) {
					count++;
				}
			}
		if(count>=2)
			return false;
		else 
			return true;
	}
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in)	;// TODO Auto-generated method stub
		Map<String,Integer> counts=new HashMap<String,Integer>();
		int test_case=sc.nextInt();
		int numberOfTweets,max=0,size=0;
		String result_name[]=new String[10];
		int result_value[]=new int[10];
		for(int i=0;i<test_case;i++) {
			numberOfTweets=sc.nextInt();
			String tweets[]=new String[numberOfTweets];
			String substr[]=new String[numberOfTweets];
			//sc.useDelimiter("\n");
			for(int j=0;j<numberOfTweets;j++) {				
				tweets[j]=sc.next();
				substr[j]=tweets[j].substring(0,tweets[j].indexOf("_"));	
				if(search(substr[j],substr)) {
					counts.put(substr[j], 1);
				}
				else {
					for(Map.Entry<String,Integer> name :counts.entrySet()) {
						int k=0;
						if(substr[j].equals(name.getKey())) {
							k=name.getValue();
							k++;
							counts.replace(substr[j], k);
						}
						if (max<name.getValue()) {
							max=name.getValue();
						}
					}
				}
			}
			for(Map.Entry<String,Integer> name :counts.entrySet()) {
				if(max==name.getValue()) {
					for(int z=size;z<numberOfTweets;) {
						result_name[z]=name.getKey();
						result_value[z]=name.getValue();
						size++;
						break;
					}
				}
			}
		
		}
		for(int i=0;i<size;i++) {
			System.out.println(result_name[i] +" "+result_value[i]);
		}
		sc.close();
	}
}
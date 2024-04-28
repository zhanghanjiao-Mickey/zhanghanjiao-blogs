import java.util.ArrayList;
import java.util.List;

public class Exercise{
    public static void main(String[] args){
        List<Integer> nums = new ArrayList<>();
        nums.add(2);
        for(int i = 0; i < nums.size();i++){
            System.out.println(nums.get(i));
        }
    }
}
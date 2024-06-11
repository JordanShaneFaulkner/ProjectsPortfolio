package droid;

public class Droid {
    int batteryLevel;
    String name;
    public Droid(String DroidName){
        name = DroidName;
        batteryLevel = 100;
    }
    public void performTask(String task){
        System.out.println(name + " Is performing the task: "+task);
        batteryLevel -= 10;
        System.out.println("Remaining battery level: "+batteryLevel);
    }
    public void chargeBattery(){
        if(batteryLevel>=100){
            System.out.print("Battery fully charged!");

        }
        else{
            batteryLevel+=10;
            System.out.println("Battery Level is: " + batteryLevel);
        }
    }
    public static void main(String[] args){
        Droid codey = new Droid("Codey");
        System.out.println(codey.name);
        System.out.println(codey.batteryLevel);
        codey.performTask("Cleaning Carpet");
        codey.performTask("Dancing");
        codey.performTask("Washing clothes");
        codey.chargeBattery();
        codey.chargeBattery();
        codey.chargeBattery();
        codey.chargeBattery();
        codey.chargeBattery();
        System.out.println(codey.batteryLevel);
        System.out.println(codey.batteryLevel);
        



    }
}

public class MyClass {
    public static void main(String args[]) {
        //if b2 unknown
        byte v1=(byte)(0xBC);
        byte v3=(byte)(0x31);
        for(int i=0x00;i<0xff;i++){
            byte res=(byte)(v1 ^ i * 7 ^ ~v3 + 13);
            System.out.printf("0x%02x 0x%02x\n",i,res);
        }
      
    }
}
public class MyClass {
    public static void main(String args[]) {
        //if b1 unknown
        byte res=(byte)(0xBC ^ 0x6e * 7 ^ ~0x31 + 13);
        System.out.println(String.format("0x%02X", res));
        
        //if b3 unknown
        byte res2=(byte)~((0x30 ^ 0x30 * 7 ^ 0xB9)-13);
        System.out.println(String.format("0x%02X", res2));
    }
}


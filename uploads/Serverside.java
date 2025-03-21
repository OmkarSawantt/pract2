import java.io.*;
import java.net.*;
public class Serverside {
public static void main(String[] args) {
try {
int port =5555 ;
ServerSocket ss=new ServerSocket (port);
System.out.println("Waiting for connection");
Socket s= ss.accept();
System.out.println("Connection is done...");

BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));

}
catch (Exception e)
{
System.out.println("Error : " + e);
}
}}

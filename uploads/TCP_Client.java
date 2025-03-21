import java.io.*;
import java.net.*;
public class TCP_Client {
public static void main(String[] args) {
try {
int port = 5555;
InetAddress addr = InetAddress.getLocalHost();
Socket s = new Socket(addr,port);
System.out.println("Connection is done ...");
BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));
System.out.println("Enter The Number :");
int num = Integer.parseInt(br1.readLine());
PrintWriter pw = new PrintWriter(new OutputStreamWriter(s.getOutputStream()));
pw.println(num);
pw.flush();
BufferedReader br2 = new BufferedReader(new InputStreamReader(s.getInputStream()));
int ans = Integer.parseInt(br2.readLine());
System.out.println("Response From Server =" + ans);
}
catch (Exception e)
{
System.out.println("Error : " + e);
}
}
}

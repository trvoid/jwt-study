/******************************************************************************
 * Create a JWT token                                                         *
 ******************************************************************************/
 
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.crypto.Mac;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.binary.Base64;

public class JwtTokenCreator {
    
    private static String readFile(String path, Charset encoding) throws IOException {
        return Files.readString(Paths.get(path), encoding);
    }
    
    private static String create(String header_obj_str, String payload_obj_str, String secret) throws Exception {
        byte[] header_bytes = Base64.encodeBase64URLSafe(header_obj_str.getBytes(StandardCharsets.UTF_8));
        byte[] payload_bytes = Base64.encodeBase64URLSafe(payload_obj_str.getBytes(StandardCharsets.UTF_8));
        String header = new String(header_bytes, StandardCharsets.UTF_8);
        String payload = new String(payload_bytes, StandardCharsets.UTF_8);
        String header_plus_payload = header + "." + payload;
        
        SecretKey key = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");
        
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(key);
        mac.update(header_plus_payload.getBytes(StandardCharsets.UTF_8));
        byte[] result = mac.doFinal();
        
        byte[] b64data = Base64.encodeBase64URLSafe(result);
        String signature = new String(b64data, StandardCharsets.UTF_8);
        
        String token = header_plus_payload + "." + signature;
        
        return token;
    }
    
    private static void printUsage() {
        System.out.println("java JwtTokenCreator <header_file> <payload_file> <secret>");
    }
    
    public static void main(String[] args) {
        if (args.length != 3) {
            printUsage();
            System.exit(-1);
        }
        
        try {
            String header_file = args[0];
            String payload_file = args[1];
            String secret = args[2];
            
            String header_obj_str = readFile(header_file, StandardCharsets.UTF_8);
            String payload_obj_str = readFile(payload_file, StandardCharsets.UTF_8);
            
            String token = create(header_obj_str, payload_obj_str, secret);
            
            System.out.println("** JWT token **");
            System.out.println(token);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
    
}

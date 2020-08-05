/******************************************************************************
 * Validate a JWT token                                                       *
 ******************************************************************************/
 
import java.nio.charset.StandardCharsets;
import javax.crypto.Mac;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.binary.Base64;

public class JwtTokenValidator {
    
    private static boolean validate(String token, String secret) throws Exception {
        int pos = token.lastIndexOf('.');
        if (pos < 0) {
            return false;
        }
        String header_plus_payload = token.substring(0, pos);
        String signature = token.substring(pos + 1);
        
        SecretKey key = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");
        
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(key);
        mac.update(header_plus_payload.getBytes(StandardCharsets.UTF_8));
        byte[] result = mac.doFinal();
        
        byte[] b64data = Base64.encodeBase64URLSafe(result);
        String signatureDerived = new String(b64data, StandardCharsets.UTF_8);
        System.out.println(signatureDerived);
        
        return signatureDerived.equals(signature);
    }
    
    private static void printUsage() {
        System.out.println("java JwtTokenValidator <token> <secret>");
    }
    
    public static void main(String[] args) {
        if (args.length != 2) {
            printUsage();
            System.exit(-1);
        }
        
        try {
            String token = args[0];
            String secret = args[1];
            
            boolean is_valid = validate(token, secret);
            
            System.out.println("** is_valid: " + is_valid + " **");
            if (is_valid) {
                int pos = token.lastIndexOf('.');
                String header_plus_payload = token.substring(0, pos);
                int pos2 = header_plus_payload.lastIndexOf('.');
                String header = header_plus_payload.substring(0, pos2);
                String payload = header_plus_payload.substring(pos2 + 1);
                System.out.println(header);
                System.out.println(payload);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
    
}

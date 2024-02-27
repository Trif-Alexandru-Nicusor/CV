package com.example.application.views.main;

import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import java.util.Properties;

public class universalFunctions {
    public static void sendEmail(String sendTo , String subject , String message2){
        Properties properties3 = new Properties();
        properties3.put("mail.smtp.auth", "true");
        properties3.put("mail.smtp.starttls.enable", "true");
        properties3.put("mail.smtp.host", "smtp.gmail.com");
        properties3.put("mail.smtp.port", "587");
        Session session = Session.getInstance(properties3, new javax.mail.Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication("", "");
            }
        });
        try {
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(""));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(sendTo));
            message.setSubject(subject);
            message.setText(message2);
            Transport.send(message);
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }
    }
}

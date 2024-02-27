package com.example.application.views.main;
import com.vaadin.flow.component.Key;
import com.vaadin.flow.component.Text;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.EmailField;
import com.vaadin.flow.component.textfield.PasswordField;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import jakarta.validation.constraints.Email;
import com.example.application.views.main.MainView;
import com.example.application.views.main.universalFunctions.*;
import java.sql.*;
import java.util.Random;

@PageTitle("Recupereaza Parola")
@Route(value = "recoverPassword")
public class recoverPasswordPage extends VerticalLayout {
    private Text recoverText;
    private TextField userRecover ;
    private EmailField emailRecover ;
    private Button recoverPassword ;
    private Button buttonBackToLoginPage ;
    public recoverPasswordPage() {
        recoverText = new Text("Recupereaza Parola");
        userRecover = new TextField("Utilizator");
        emailRecover = new EmailField("Email");
        recoverPassword = new Button("Recupereaza parola");
        buttonBackToLoginPage = new Button("Inapoi");
        userRecover.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        emailRecover.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        recoverPassword.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        recoverPassword.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        recoverPassword.addClickShortcut(Key.ENTER);
        buttonBackToLoginPage.addClickListener(e -> {
            getUI().ifPresent(ui -> ui.navigate(MainView.class));
        });
        recoverPassword.addClickListener(e -> {
            if(!userRecover.getValue().isEmpty() && !emailRecover.getValue().isEmpty()) {
                String JDBC_URL = "jdbc:mysql://localhost:3306/";
                String JDBC_USER = "";
                String JDBC_PASSWORD = "";
                try (Connection connection = DriverManager.getConnection(JDBC_URL, JDBC_USER, JDBC_PASSWORD)) {
                    String query = "SELECT * FROM loginData WHERE User = ? AND Email = ?";
                    try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
                        preparedStatement.setString(1, userRecover.getValue());
                        preparedStatement.setString(2, emailRecover.getValue());
                        try (ResultSet resultSet = preparedStatement.executeQuery()) {
                            if (resultSet.next()) {
                                String newPassword = generateRandomString();
                                String updateQuery = "UPDATE loginData SET Password = ? WHERE User = ? AND Email = ?";
                                try (PreparedStatement updateStatement = connection.prepareStatement(updateQuery)) {
                                    updateStatement.setString(1, newPassword);
                                    updateStatement.setString(2, userRecover.getValue());
                                    updateStatement.setString(3, emailRecover.getValue());
                                    updateStatement.executeUpdate();
                                }
                                com.example.application.views.main.universalFunctions.sendEmail(emailRecover.getValue() , "Resetare parola" , "Parola pentru contul : " + userRecover.getValue() + " a fost resetata.\n" + "Noua parola este : " + newPassword);
                                userRecover.setValue("");
                                emailRecover.setValue("");
                                Notification.show("Parola a fost schimbata . Ati primit un email cu noua parola ." , 3000 , Notification.Position.TOP_CENTER);
                            } else {
                                Notification.show("Utilizator sau parola incorecte ." , 3000 , Notification.Position.TOP_CENTER);
                            }
                        }catch (SQLException e1){
                            e1.printStackTrace();
                        }
                    }catch (SQLException e1){
                        e1.printStackTrace();
                    }
                }catch (SQLException e1){
                    e1.printStackTrace();
                }
            }else{
                Notification.show("Trebuie completate campurile ." , 3000 , Notification.Position.TOP_CENTER);
            }
        });
        VerticalLayout recoverPasswordV = new VerticalLayout(recoverText , userRecover, emailRecover);
        HorizontalLayout recoverPasswordH = new HorizontalLayout(recoverPassword, buttonBackToLoginPage);
        recoverPasswordV.setAlignItems(Alignment.CENTER);
        recoverPasswordH.setAlignItems(Alignment.CENTER);
        add(recoverPasswordV, recoverPasswordH);
        setAlignItems(Alignment.CENTER);
        setSpacing(true);
    }
    private static String generateRandomString() {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        StringBuilder randomString = new StringBuilder();
        Random random = new Random();

        for (int i = 0; i < 8; i++) {
            randomString.append(characters.charAt(random.nextInt(characters.length())));
        }

        return randomString.toString();
    }
}

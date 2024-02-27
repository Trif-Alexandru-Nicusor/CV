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
import com.example.application.views.main.universalFunctions.*;
import com.example.application.views.main.MainView;
import java.sql.*;

@PageTitle("Creaaza Cont")
@Route(value = "createAccount")
public class createAccountPage extends VerticalLayout {
    private Text textCreate;
    private TextField userCreate;
    private EmailField emailCreate;
    private PasswordField passwordCreate;
    private Button buttonCreateAccount;
    private Button buttonBackToLoginPage;

    public createAccountPage() {
        textCreate = new Text("Creeaza cont");
        userCreate = new TextField("Utilizator");
        emailCreate = new EmailField("Email");
        passwordCreate = new PasswordField("Parola");
        buttonCreateAccount = new Button("Creeaza cont");
        buttonBackToLoginPage = new Button("Inapoi");
        userCreate.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        emailCreate.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        passwordCreate.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        buttonCreateAccount.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        buttonBackToLoginPage.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        buttonCreateAccount.addClickShortcut(Key.ENTER);
        buttonCreateAccount.addClickListener(e -> {
            String username = userCreate.getValue();
            String email = emailCreate.getValue();
            String password = passwordCreate.getValue();
            if (username.isEmpty() || email.isEmpty() || password.isEmpty()) {
                Notification.show("Trebuie completate toate campurile ." , 3000 , Notification.Position.TOP_CENTER);
                return ;
            }
            try {
                Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/", "", "");
                PreparedStatement checkUserStatement = connection.prepareStatement("SELECT * FROM loginData WHERE User = ?");
                checkUserStatement.setString(1, username);
                ResultSet resultSet = checkUserStatement.executeQuery();

                if (resultSet.next()) {
                    Notification.show("User deja existent .", 3000, Notification.Position.TOP_CENTER);
                } else {
                    PreparedStatement insertUserStatement = connection.prepareStatement("INSERT INTO loginData (User, Email, Password) VALUES (?, ?, ?)");
                    insertUserStatement.setString(1, username);
                    insertUserStatement.setString(2, email);
                    insertUserStatement.setString(3, password);
                    insertUserStatement.executeUpdate();
                    com.example.application.views.main.universalFunctions.sendEmail(emailCreate.getValue() , "Contul a fost creeat" , "Contul cu utilizatorul : +" + userCreate.getValue() + " a fost creat cu parola : " + passwordCreate.getValue());
                    userCreate.setValue("");
                    emailCreate.setValue("");
                    passwordCreate.setValue("");
                    Notification.show("Cont creat . Ai primit un mail de confirmare cu datele .", 3000, Notification.Position.TOP_CENTER);
                }
                resultSet.close();
                checkUserStatement.close();
                connection.close();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        });
        buttonBackToLoginPage.addClickListener(e -> {
            getUI().ifPresent(ui -> ui.navigate(MainView.class));
        });
        VerticalLayout createAccountV = new VerticalLayout(textCreate, userCreate, emailCreate, passwordCreate);
        HorizontalLayout createAccountH = new HorizontalLayout(buttonCreateAccount, buttonBackToLoginPage);
        createAccountV.setAlignItems(Alignment.CENTER);
        createAccountH.setAlignItems(Alignment.CENTER);
        add(createAccountV, createAccountH);
        setAlignItems(Alignment.CENTER);
    }
}

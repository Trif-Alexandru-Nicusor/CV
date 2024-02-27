package com.example.application.views.main;
import com.vaadin.flow.component.Key;
import com.vaadin.flow.component.Text;
import com.vaadin.flow.component.applayout.AppLayout;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.PasswordField;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import com.example.application.views.main.createAccountPage;
import com.example.application.views.main.recoverPasswordPage;
import com.example.application.views.main.userWindow;
import java.sql.*;

@PageTitle("Logheaza-te")
@Route(value = "" , layout =  AppLayout.class)
public class MainView extends VerticalLayout {
    private Text loginText;
    public static TextField userLogin;
    public static PasswordField passwordLogin;
    private Button loginButton;
    private Button createAccountButton;
    private Button recoverPasswordButton;
    public MainView() {
        loginText = new Text("Logare");
        userLogin = new TextField("Utilizator");
        passwordLogin = new PasswordField("Parola");
        loginButton = new Button("Logheaza-te");
        createAccountButton = new Button("Creeaza cont");
        recoverPasswordButton = new Button("Recupereaza parola");
        userLogin.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        passwordLogin.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        loginButton.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        createAccountButton.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        recoverPasswordButton.getStyle().set("font", "30px Times New Roman").set("color", "Black");
        loginButton.addClickListener(e -> {
            try {
                Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/", "", "");
                PreparedStatement checkUserStatement = connection.prepareStatement("SELECT * FROM loginData WHERE User = ? AND Password = ?");
                checkUserStatement.setString(1, userLogin.getValue());
                checkUserStatement.setString(2, passwordLogin.getValue());
                ResultSet resultSet = checkUserStatement.executeQuery();
                if (resultSet.next()) {
                    getUI().ifPresent(ui -> ui.navigate(userWindow.class));
                } else {

                    Notification.show("Cont gresit .", 3000, Notification.Position.TOP_CENTER);
                }
                resultSet.close();
                checkUserStatement.close();
                connection.close();
            } catch (SQLException ex) {
                Notification.show("Eroare baza de date .", 3000, Notification.Position.TOP_CENTER);
                ex.printStackTrace();
            }
        });
        createAccountButton.addClickListener(e -> {
            getUI().ifPresent(ui -> ui.navigate(createAccountPage.class));
        });
        recoverPasswordButton.addClickListener(e -> {
            getUI().ifPresent(ui -> ui.navigate(recoverPasswordPage.class));
        });
        loginButton.addClickShortcut(Key.ENTER);
        VerticalLayout loginLayoutV = new VerticalLayout(loginText , userLogin, passwordLogin, loginButton);
        HorizontalLayout loginLayoutH = new HorizontalLayout(createAccountButton, recoverPasswordButton);
        loginLayoutV.setAlignItems(Alignment.CENTER);
        loginLayoutH.setAlignItems(Alignment.CENTER);
        add(loginLayoutV, loginLayoutH);
        setAlignItems(Alignment.CENTER);
        setSpacing(true);
    }
}

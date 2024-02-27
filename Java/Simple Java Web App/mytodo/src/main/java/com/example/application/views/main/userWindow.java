package com.example.application.views.main;

import com.vaadin.collaborationengine.SystemUserInfo;
import com.vaadin.flow.component.Text;
import com.vaadin.flow.component.UI;
import com.vaadin.flow.component.applayout.AppLayout;
import com.vaadin.flow.component.applayout.DrawerToggle;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.charts.model.Select;
import com.vaadin.flow.component.combobox.ComboBox;
import com.vaadin.flow.component.combobox.MultiSelectComboBox;
import com.vaadin.flow.component.dialog.Dialog;
import com.vaadin.flow.component.html.Div;
import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.page.Push;
import com.vaadin.flow.component.textfield.NumberField;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.router.PageTitle;
import com.vaadin.flow.router.Route;
import com.example.application.views.main.userProfile;
import java.sql.*;
import java.util.concurrent.*;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

@PageTitle("Utilizator")
@Route(value = "userWindow")
public class userWindow extends AppLayout {
    private Button dialogAddCarButton;
    private TextField licensePlate ;
    private NumberField howMuchTime ;
    private ComboBox<String> listWithAddedCars ;
    private List<String> carsAddedInPark  = new ArrayList<String>();
    private NumberField carLeftTime ;
    private TextField car1 , car2 , car3 , car4 , car5 , car6 , car7 , car8 , car9 , car10;
    private NumberField carLefTime1 , carLefTime2 ,carLefTime3 ,carLefTime4 ,carLefTime5 ,carLefTime6 ,carLefTime7 ,carLefTime8 ,carLefTime9 ,carLefTime10 ;
    public <carsAddedInPark> userWindow() {
        //Div loggedAsText = new Div(new Text("Logat ca si : " + MainView.userLogin.getValue()));
        addToNavbar(new DrawerToggle());
        Div userProfileButton = new Div(new Text("Profil utilizator"));
        userProfileButton.getStyle().set("font", "20px Times New Roman");
        Div addPaymentMethodButton = new Div(new Text("Adauga metoda de plata"));
        addPaymentMethodButton.getStyle().set("font", "20px Times New Roman");
        Div addCars = new Div(new Text("Masini"));
        addCars.getStyle().set("font", "20px Times New Roman");
        Button addCarButton = new Button("Adauga masina");
        Button deleteCarButton = new Button("Sterge Masina");
        car1 = new TextField("Numar de inmatriculare");
        car1.setEnabled(false);
        car2 = new TextField("Numar de inmatriculare");
        car2.setEnabled(false);
        car3 = new TextField("Numar de inmatriculare");
        car3.setEnabled(false);
        car4 = new TextField("Numar de inmatriculare");
        car4.setEnabled(false);
        car5 = new TextField("Numar de inmatriculare");
        car5.setEnabled(false);
        car6 = new TextField("Numar de inmatriculare");
        car6.setEnabled(false);
        car7 = new TextField("Numar de inmatriculare");
        car7.setEnabled(false);
        car8 = new TextField("Numar de inmatriculare");
        car8.setEnabled(false);
        car9 = new TextField("Numar de inmatriculare");
        car9.setEnabled(false);
        car10 = new TextField("Numar de inmatriculare");
        car10.setEnabled(false);
        VerticalLayout viewAddedCarsLicensePlatesV = new VerticalLayout(addCarButton, car1, car2, car3, car4, car5, car6, car7, car8, car9, car10);
        carLefTime1 = new NumberField("Timp ramas");
        carLefTime1.setEnabled(false);
        carLefTime2 = new NumberField("Timp ramas");
        carLefTime2.setEnabled(false);
        carLefTime3 = new NumberField("Timp ramas");
        carLefTime3.setEnabled(false);
        carLefTime4 = new NumberField("Timp ramas");
        carLefTime4.setEnabled(false);
        carLefTime5 = new NumberField("Timp ramas");
        carLefTime5.setEnabled(false);
        carLefTime6 = new NumberField("Timp ramas");
        carLefTime6.setEnabled(false);
        carLefTime7 = new NumberField("Timp ramas");
        carLefTime7.setEnabled(false);
        carLefTime8 = new NumberField("Timp ramas");
        carLefTime8.setEnabled(false);
        carLefTime9 = new NumberField("Timp ramas");
        carLefTime9.setEnabled(false);
        carLefTime10 = new NumberField("Timp ramas");
        carLefTime10.setEnabled(false);
        VerticalLayout viewAddedCarsLeftTimeV = new VerticalLayout(deleteCarButton, carLefTime1, carLefTime2, carLefTime3, carLefTime4, carLefTime5, carLefTime6, carLefTime7, carLefTime8, carLefTime9, carLefTime10);
        viewAddedCarsLeftTimeV.getStyle().set("position", "relative");
        viewAddedCarsLeftTimeV.getStyle().set("left", "-500px");
        userProfileButton.addClickListener(event -> {
            getUI().ifPresent(ui -> ui.navigate(userProfile.class));
        });
        addPaymentMethodButton.addClickListener(event -> {
        });
        addCars.addClickListener(event -> {
            setContent(new HorizontalLayout(viewAddedCarsLicensePlatesV, viewAddedCarsLeftTimeV));
        });
        addCarButton.addClickListener(event -> {
            Dialog addCarDialog = new Dialog();
            addCarDialog.setHeaderTitle("Adauga masina");
            TextField licensePlate = new TextField("Numar de inmatriculare");
            howMuchTime = new NumberField();
            howMuchTime.setLabel("Cat timp stai (secunde)");
            Button dialogAddCarButton = new Button("Adauga masina");
            Button closeDialogAddCar = new Button("Inchide", e -> addCarDialog.close());
            VerticalLayout addCarDialogLayoutV = new VerticalLayout(licensePlate, howMuchTime, dialogAddCarButton, closeDialogAddCar);
            addCarDialog.add(addCarDialogLayoutV);
            addCarDialog.open();
            dialogAddCarButton.addClickListener(dialogEvent -> {
                if (!licensePlate.isEmpty()) {
                    TextField[] carLicensePlate = {car1, car2, car3, car4, car5, car6, car7, car8, car9, car10};
                    NumberField[] carLeftTime = {carLefTime1, carLefTime2, carLefTime3, carLefTime4, carLefTime5, carLefTime6, carLefTime7, carLefTime8, carLefTime9, carLefTime10};
                    for (int i = 0; i < carLicensePlate.length; i++) {
                        if (carLicensePlate[i].isEmpty() && carLeftTime[i].isEmpty()) {
                            carLicensePlate[i].setValue(licensePlate.getValue());
                            carLeftTime[i].setValue(Double.valueOf(howMuchTime.getValue()));
                            carsAddedInPark.add(licensePlate.getValue());
                            Notification.show("Masina adaugata.", 3000, Notification.Position.MIDDLE);
                            final int I = i;
                            long startTime = System.currentTimeMillis();
                            UI ui = UI.getCurrent();
                            if (ui != null) {
                                new Thread(() -> {
                                    while (true) {
                                        if (!carLeftTime[I].isEmpty() && carLeftTime[I].getValue() >= 1 && !carLicensePlate[I].isEmpty())
                                        {
                                            try {
                                                Thread.sleep(1000);
                                                ui.access(() -> {
                                                    System.out.println("Updating GUI - Time left: " + carLeftTime[I].getValue());
                                                    carLeftTime[I].setValue(Double.valueOf(carLeftTime[I].getValue()) - 1);
                                                });

                                            } catch (InterruptedException e) {
                                                e.printStackTrace();
                                            }
                                    } else{
                                            long endTime = System.currentTimeMillis();
                                            long elapsedTime = endTime - startTime;
                                            long timeP = elapsedTime / 1000;
                                            int priceP = 0;
                                            if (timeP <= 10){
                                                priceP = 1;
                                            } else if(timeP >= 10  && timeP >=20){
                                                priceP = 2;
                                            }else if(timeP >= 20 && timeP <= 30){
                                                priceP = 3;
                                            }else if(timeP >= 30){
                                                priceP = 5;
                                            }
                                            try {
                                                Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/", "", "");
                                                PreparedStatement checkUserStatement = connection.prepareStatement("SELECT * FROM loginData WHERE User = ? AND Password = ?");
                                                checkUserStatement.setString(1, MainView.userLogin.getValue());
                                                checkUserStatement.setString(2, MainView.passwordLogin.getValue());
                                                ResultSet resultSet = checkUserStatement.executeQuery();
                                                if (resultSet.next()) {
                                                    String email = resultSet.getString("Email");
                                                    universalFunctions.sendEmail(email , "Factura parcare" , "Timpul a expirat aveti de plata : "+ priceP);
                                                }
                                                resultSet.close();
                                                checkUserStatement.close();
                                                connection.close();
                                            } catch (SQLException ex) {
                                                ex.printStackTrace();
                                            }
                                            break;
                                        }
                                    }
                                }).start();
                            } else {
                                System.out.println("UI is not available.");
                            }
                            break;
                        }
                    }
                }
            });
        });
        deleteCarButton.addClickListener(event -> {
            Dialog deleteCarDialog = new Dialog();
            deleteCarDialog.setHeaderTitle("Sterge Masina");
            listWithAddedCars = new ComboBox<String>("Masini adaugate");
            listWithAddedCars.setItems(carsAddedInPark);
            Button dialogRemoveCarButton = new Button("Sterge masina");
            Button closeRemoveCarButtonDialog = new Button("Inchide" , e -> deleteCarDialog.close());
            VerticalLayout addCarDialogLayoutV = new VerticalLayout(listWithAddedCars , dialogRemoveCarButton , closeRemoveCarButtonDialog);
            deleteCarDialog.add(addCarDialogLayoutV);
            deleteCarDialog.open();
            dialogRemoveCarButton.addClickListener(dialogEvent -> {
                if(!listWithAddedCars.isEmpty()) {
                    TextField[] carLicensePlate = {car1, car2, car3, car4, car5, car6, car7, car8, car9, car10};
                    NumberField[] carLeftTime = {carLefTime1, carLefTime2, carLefTime3, carLefTime4, carLefTime5, carLefTime6, carLefTime7, carLefTime8, carLefTime9, carLefTime10};
                    boolean carRemoved = false;
                    for (int i = 0; i < carLicensePlate.length; i++) {
                        if (listWithAddedCars.getValue().equals(carLicensePlate[i].getValue())) {
                            carLicensePlate[i].setValue("");
                            carLeftTime[i].clear();
                            carsAddedInPark.remove(String.valueOf(listWithAddedCars.getValue()));
                            listWithAddedCars.setItems(carsAddedInPark);
                            Notification.show("Masina stearsa ." , 3000, Notification.Position.TOP_CENTER);
                            carRemoved = true;
                            break;
                        }
                        if (!carRemoved) {
                            Notification.show("Masina nu exista ." , 3000, Notification.Position.TOP_CENTER);
                        }
                    }
                }

            });
        });
        addToDrawer(userProfileButton , addPaymentMethodButton , addCars);
        }
    }
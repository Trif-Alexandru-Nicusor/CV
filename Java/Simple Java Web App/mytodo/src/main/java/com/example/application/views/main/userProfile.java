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
@PageTitle("Profil")
@Route(value = "profileWindow")
public class userProfile extends AppLayout{
    public userProfile(){
    //Div loggedAsText = new Div(new Text("Logat ca si : " + MainView.userLogin.getValue()));
    addToNavbar(new DrawerToggle());
    Div userProfileButton = new Div(new Text("Profil utilizator"));
    Div addPaymentMethodButton = new Div(new Text("Adauga metoda de plata"));
    Div addCars = new Div(new Text("Masini"));
    }
}

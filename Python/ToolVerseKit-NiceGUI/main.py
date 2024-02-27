from nicegui import ui , events
from io import StringIO
import os , csv
import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load
import numpy as np
from Functions import loginPageFunctions , passwordManagerPageFunctions , createAccountPageFunctions , recoverPasswordPageFunctions , universalFunctions , youTubeMusicDownloaderPageFunctions , solarPanelProductionPredictionFunctions
folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Functions')
@ui.page('/home')
def homePage():
    ui.page_title('ToolVerseKit Home')
    ui.add_body_html('''
                        <style>
                            #c31{
                                visibility : hidden ;
                            }
                        </style>
                     ''')
    with ui.header().style('background-color : white'):
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'login' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Login' , target = loginPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'person_add' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Create Account' , target = createAccountPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
    ui.label('Home').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center')
@ui.page('/homeLogged')
def homeLoggedPage():
    ui.page_title('ToolVerseKit Home')
    with ui.header().style('background-color : white'):
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager' , target = passwordManagerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader' , target = youTubeMusicDownloaderPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger' , target = pdfsMergerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction' , target = solarPanelProductionPredictionPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        with ui.row():
            with ui.button(icon='menu' , color ='black'):
                with ui.menu() as menu:
                    with ui.row():
                        ui.icon(name = 'account_circle' , size = '40px')
                        ui.menu_item('Profile' , on_click = lambda : universalFunctions.goToPage(page = 'profile')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'credit_card' , size = '40px')
                        ui.menu_item('Payment Methods' , on_click = lambda : universalFunctions.goToPage(page = 'paymentMethods')).style('font-family : "Times New Roman" ; font-size : 20px')
                    ui.separator()
                    with ui.row():
                        ui.icon(name = 'logout' , size = '40px')
                        ui.menu_item('Logout', on_click = lambda : universalFunctions.goToPage(page = 'home')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'close' , size = '40px')
                        ui.menu_item('Close', on_click = menu.close).style('font-family : "Times New Roman" ; font-size : 20px')
    ui.label('Home').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center')
@ui.page('/login')
def loginPage():
    ui.page_title('ToolVerseKit Login')
    global userLogin
    ui.add_body_html('''
                    <style>
                        .loginPageCard{
                            align-self : center ;
                        }
                    </style>
                 ''')
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homePage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'person_add' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Create Account' , target = createAccountPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.run(dark = True , title = "Home")
    with ui.card().classes('loginPageCard'):
        ui.label('Login').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center')
        userLogin = ui.input(placeholder = 'User')
        userLogin.style('font-family : "Times New Roman" ; font-size : 30px')
        passwordLogin = ui.input(placeholder = 'Password' , password = True , password_toggle_button = True)
        passwordLogin.style('font-family : "Times New Roman" ; font-size : 30px')
        with ui.row():
            loginButton = ui.button(text = 'Login' , on_click = lambda : loginPageFunctions.login(user = userLogin.value , password = passwordLogin.value) , icon = 'login')
            loginButton.style('font-family : "Times New Roman" ; font-size : 20px')
            loginButton.tailwind.text_transform('normal-case').background_color('white').text_color('black')
            recoverAccount = ui.button(text = 'Recover Password' , on_click = lambda : universalFunctions.goToPage(page = 'recoverPassword') , icon = 'undo')
            recoverAccount.style('font-family : "Times New Roman" ; font-size : 20px ; position : relative ; right : -35px ;')
            recoverAccount.tailwind.text_transform('normal-case').background_color('white').text_color('black')
@ui.page('/createAccount')
def createAccountPage():
    ui.page_title('ToolVerseKit Create Account')
    ui.add_body_html('''
                    <style>
                        .createAccountPageCard{
                            align-self : center ;
                        }
                    </style>
                 ''')
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homePage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'login' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Login' , target = loginPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
    with ui.card().classes('createAccountPageCard'):
        ui.label('Create Account').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center')
        with ui.column():
            userCreate = ui.input(placeholder = 'User')
            userCreate.style('font-family : "Times New Roman" ; font-size : 30px')
            emailCreate = ui.input(placeholder = 'Email')
            emailCreate.style('font-family : "Times New Roman" ; font-size : 30px')
            passwordCreate = ui.input(placeholder = "Password" , password = True , password_toggle_button = True)
            passwordCreate.style('font-family : "Times New Roman" ; font-size : 30px')
            createAccountButton = ui.button(text = 'Create account' , on_click = lambda : createAccountPageFunctions.addAccount(user = userCreate , email = emailCreate , password = passwordCreate) , icon = 'person_add')
            createAccountButton.style('font-family : "Times New Roman" ; font-size : 20px ; align-self : center')
            createAccountButton.tailwind.text_transform('normal-case').background_color('white').text_color('black')
@ui.page('/recoverPassword')
def recoverPasswordPage():
    ui.page_title('ToolVerseKit Recover Password')
    ui.add_body_html('''
                    <style>
                        .recoverAccountPageCard{
                            align-self : center ;
                        }
                    </style>
                 ''')
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homePage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'person_add' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Create Account' , target = createAccountPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'login' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Login' , target = loginPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
    with ui.card().classes('recoverAccountPageCard'):
        ui.label('Recover Password').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center')
        with ui.column():
            userRecover = ui.input(placeholder = 'User')
            userRecover.style('font-family : "Times New Roman" ; font-size : 30px')
            emailRecover = ui.input(placeholder = 'Email')
            emailRecover.style('font-family : "Times New Roman" ; font-size : 30px')
            recoverAccountButton = ui.button(text = 'Recover Password' , on_click = lambda : recoverPasswordPageFunctions.resetPassword(email = emailRecover , user = userRecover) , icon = 'undo')
            recoverAccountButton.style('font-family : "Times New Roman" ; font-size : 20px ; align-self : center')
            recoverAccountButton.tailwind.text_transform('normal-case').background_color('white').text_color('black')
@ui.page('/profile')
def profilePage():
    ui.page_title('ToolVerseKit Profile')
    ui.add_body_html('''
                        <style>
                            .profilePageCard{
                                align-self : center ;
                            }
                        </style>
                     ''')
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homeLoggedPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager' , target = passwordManagerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader' , target = youTubeMusicDownloaderPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger' , target = pdfsMergerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction' , target = solarPanelProductionPredictionPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        with ui.row():
            with ui.button(icon='menu' , color ='black'):
                with ui.menu() as menu:
                    with ui.row():
                        ui.icon(name = 'account_circle' , size = '40px')
                        ui.menu_item('Profile' , on_click = lambda : universalFunctions.goToPage(page = 'profile')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'credit_card' , size = '40px')
                        ui.menu_item('Payment Methods' , on_click = lambda : universalFunctions.goToPage(page = 'paymentMethods')).style('font-family : "Times New Roman" ; font-size : 20px')
                    ui.separator()
                    with ui.row():
                        ui.icon(name = 'logout' , size = '40px')
                        ui.menu_item('Logout', on_click = lambda : universalFunctions.goToPage(page = 'home')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'close' , size = '40px')
                        ui.menu_item('Close', on_click = menu.close).style('font-family : "Times New Roman" ; font-size : 20px')
    with ui.card().classes('profilePageCard'):
        userProfile = ui.input(label = 'User' , value = '')
        userProfile.style('font-family : "Times New Roman" ; font-size : 30px')
        userProfile.set_value(userLogin.value)
        emailProfile = ui.input(label = 'Email' , value = '')
        emailProfile.style('font-family : "Times New Roman" ; font-size : 30px')
        emailProfile.set_value(universalFunctions.checkUserEmail(userLogin.value))
        passwordProfile = ui.input(label = 'Password' , value = '' , password = True , password_toggle_button = '')
        passwordProfile.style('font-family : "Times New Roman" ; font-size : 30px')
        paymentMethod = ui.select(options = [''] , label = 'Payment Method' )
        paymentMethod.style('font-family : "Times New Roman" ; font-size : 30px ; width : 370px')
        buttonChangeProfileData = ui.button(text = 'Update Profile')
        buttonChangeProfileData.style('font-family : "Times New Roman" ; font-size : 20px')
        buttonChangeProfileData.tailwind.text_transform('normal-case').background_color('white').text_color('black').align_self('center')
@ui.page('/paymentMethods')
def paymentMethodsPage():
    ui.page_title('ToolVerseKit Payment Methods')
    ui.add_body_html('''
                        <style>
                            .paymentMethodsPageCard{
                                align-self : center ;
                            }
                        </style>
                     ''')
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homeLoggedPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager' , target = passwordManagerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader' , target = youTubeMusicDownloaderPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger' , target = pdfsMergerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction' , target = solarPanelProductionPredictionPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        with ui.row():
            with ui.button(icon='menu' , color ='black'):
                with ui.menu() as menu:
                    with ui.row():
                        ui.icon(name = 'account_circle' , size = '40px')
                        ui.menu_item('Profile' , on_click = lambda : universalFunctions.goToPage(page = 'profile')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'credit_card' , size = '40px')
                        ui.menu_item('Payment Methods' , on_click = lambda : universalFunctions.goToPage(page = 'paymentMethods')).style('font-family : "Times New Roman" ; font-size : 20px')
                    ui.separator()
                    with ui.row():
                        ui.icon(name = 'logout' , size = '40px')
                        ui.menu_item('Logout', on_click = lambda : universalFunctions.goToPage(page = 'home')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'close' , size = '40px')
                        ui.menu_item('Close', on_click = menu.close).style('font-family : "Times New Roman" ; font-size : 20px')
    with ui.card().classes('paymentMethodsPageCard'):
        ui.label(text = 'Chose your payment method .').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center')
        with ui.expansion(text = 'PayPal').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center'):
            namePaypal = ui.input(label = 'Surname and Name')
            namePaypal.style('font-family : "Times New Roman" ; font-size : 30px')
            emailPaypal = ui.input(label = 'Email')
            emailPaypal.style('font-family : "Times New Roman" ; font-size : 30px')
            countryPaypal = ui.input(label = 'Country')
            countryPaypal.style('font-family : "Times New Roman" ; font-size : 30px')
            cityPaypal = ui.input(label = 'City')
            cityPaypal.style('font-family : "Times New Roman" ; font-size : 30px')
            addressPaypal = ui.input(label = 'Address')
            addressPaypal.style('font-family : "Times New Roman" ; font-size : 30px')
        with ui.expansion(text = 'Card').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center'):
            nameCard = ui.input(label = 'Name from the card')
            nameCard.style('font-family : "Times New Roman" ; font-size : 30px')
            numberCard = ui.input(label = 'Number from the card')
            numberCard.style('font-family : "Times New Roman" ; font-size : 30px')
            countryCard = ui.input(label = 'Country')
            countryCard.style('font-family : "Times New Roman" ; font-size : 30px')
            cityCard = ui.input(label = 'City')
            cityCard.style('font-family : "Times New Roman" ; font-size : 30px')
            addressCard = ui.input(label = 'Address')
            addressCard.style('font-family : "Times New Roman" ; font-size : 30px')
        savePaymentData = ui.button(text = 'Save' , icon = 'save')
        savePaymentData.style('font-family : "Times New Roman" ; font-size : 20px')
        savePaymentData.tailwind.text_transform('normal-case').background_color('white').text_color('black').align_self('center')
@ui.page('/passwordManager')
def passwordManagerPage():
    ui.page_title('ToolVerseKit Password Manager')
    columns = [
        {'name' : 'ID', 'label' : 'ID' , 'field' : 'ID' },
        {'name' : 'Site/App' , 'label' : 'Site/App' , 'field' : 'Site/App' , 'align' : 'center'},
        {'name' : 'User' , 'label' : 'User' , 'field' : 'User' , 'align' : 'center'},
        {'name' : 'Password' , 'label' : 'Password' , 'field' : 'Password' , 'align' : 'center'},
    ]
    rows = []
    rows_passwords_unhidden = []
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homeLoggedPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader' , target = youTubeMusicDownloaderPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger' , target = pdfsMergerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction' , target = solarPanelProductionPredictionPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        with ui.row():
            with ui.button(icon='menu' , color ='black'):
                with ui.menu() as menu:
                    with ui.row():
                        ui.icon(name = 'account_circle' , size = '40px')
                        ui.menu_item('Profile' , on_click = lambda : universalFunctions.goToPage(page = 'profile')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'credit_card' , size = '40px')
                        ui.menu_item('Payment Methods' , on_click = lambda : universalFunctions.goToPage(page = 'paymentMethods')).style('font-family : "Times New Roman" ; font-size : 20px')
                    ui.separator()
                    with ui.row():
                        ui.icon(name = 'logout' , size = '40px')
                        ui.menu_item('Logout', on_click = lambda : universalFunctions.goToPage(page = 'home')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'close' , size = '40px')
                        ui.menu_item('Close', on_click = menu.close).style('font-family : "Times New Roman" ; font-size : 20px')
    with ui.column().classes('column1'):
        ui.add_body_html('''
                            <style>
                                .column1{
                                    position : relative;
                                    align-self : center;
                                }
                            </style>
                        ''')
        with ui.card().classes('card1'):
            ui.add_body_html('''
                                <style>
                                    .card1{
                                        position : relative;
                                        align-self : center;
                                        min-width : 1300px ;
                                    }
                                </style>
                            ''')
            ui.label('Password Manager').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center')
            table1 = ui.table(columns = columns , rows = rows ,  row_key = 'ID' , selection = 'multiple').classes('table1').props('v-slot:body')
            ui.add_head_html('''
                                <style>
                                    .table1 tbody td{
                                        font-size : 30px;
                                        font-family : 'Times New Roman';
                                        max-width: 1300px;
                                        white-space: pre-wrap;
                                        word-wrap: break-word;
                                    }
                                    .table1 th{
                                        font-size : 30px;
                                        font-family : 'Times New Roman';
                                    }
                                    .table1{
                                        width : 100%;
                                        max-height:276px;
                                    }
                                    .table1 tbody td:last-child,.table1 th:last-child {
                                        display: none;
                                    }
                                </style>
                            ''')
            with ui.row():
                newSiteApp = ui.input('Site/App')
                newSiteApp.style('font-family : "Times New Roman" ; font-size : 30px')
                newUser = ui.input('User')
                newUser.style('position : relative ; right : -55px ; font-family : "Times New Roman" ; font-size : 30px')
                newPassword = ui.input('Password' , password = True , password_toggle_button = True)
                newPassword.style('position : relative ; right : -115px ; font-family : "Times New Roman" ; font-size : 30px')
            with ui.row():
                addAccountButton = ui.button('Add Account' , on_click = lambda : passwordManagerPageFunctions.addAccount(rows_passwords_unhidden = rows_passwords_unhidden , siteApp = newSiteApp , user = newUser , password = newPassword , table = table1) , icon = 'person_add')
                addAccountButton.tailwind.text_transform('normal-case').background_color('white').text_color('black').font_size('xl')
                addAccountButton.style('position : relative ; right : -80px ; font-family : "Times New Roman"')
                removeAccountButton = ui.button('Remove Account', on_click = lambda : passwordManagerPageFunctions.removeAccount(table = table1 ,rows_passwords_unhidden = rows_passwords_unhidden) , icon = 'delete')
                removeAccountButton.tailwind.text_transform('normal-case').background_color('white').text_color('black').font_size('xl')
                removeAccountButton.style('position : relative ; right : -300px ; font-family : "Times New Roman"')
                showHidePasswordsButton = ui.button('Show Passwords' , on_click = lambda : passwordManagerPageFunctions.showHidePasswords(button = showHidePasswordsButton) , icon = 'visibility')
                showHidePasswordsButton.tailwind.text_transform('normal-case').background_color('white').text_color('black').font_size('xl')
                showHidePasswordsButton.style('position : relative ; right : -520px ; font-family : "Times New Roman"')
@ui.page('/youTubeMusicDownloader')
def youTubeMusicDownloaderPage():
    ui.page_title('ToolVerseKit Youtube Music Downloader')
    ui.add_body_html('''
                        <style>
                            .youTubeMusicDownloader{
                                font-family : "Times New Roman" ;
                                align-self : center ;
                            }
                        </style>
                     ''')
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homeLoggedPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager' , target = passwordManagerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger' , target = pdfsMergerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction' , target = solarPanelProductionPredictionPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        with ui.row():
            with ui.button(icon='menu' , color ='black'):
                with ui.menu() as menu:
                    with ui.row():
                        ui.icon(name = 'account_circle' , size = '40px')
                        ui.menu_item('Profile' , on_click = lambda : universalFunctions.goToPage(page = 'profile')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'credit_card' , size = '40px')
                        ui.menu_item('Payment Methods' , on_click = lambda : universalFunctions.goToPage(page = 'paymentMethods')).style('font-family : "Times New Roman" ; font-size : 20px')
                    ui.separator()
                    with ui.row():
                        ui.icon(name = 'logout' , size = '40px')
                        ui.menu_item('Logout', on_click = lambda : universalFunctions.goToPage(page = 'home')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'close' , size = '40px')
                        ui.menu_item('Close', on_click = menu.close).style('font-family : "Times New Roman" ; font-size : 20px')
    with ui.card().classes('youTubeMusicDownloader'):
        ui.label('Youtube Music Download').style('font-family : "Times New Roman" ; font-size : 30px ; align-self : center')
        linkYt = ui.input(label = 'Link')
        linkYt.style('font-family : "Times New Roman" ; font-size : 30px')
        downloadButton = ui.button(text = 'Download' , on_click = lambda : youTubeMusicDownloaderPageFunctions.downlaodMusic(link = linkYt.value) , icon = 'download')
        downloadButton.style('font-family : "Times New Roman" ; font-size : 20px')
        downloadButton.tailwind.text_transform('normal-case').background_color('white').text_color('black').align_self('center')
@ui.page('/pdfMerger')
def pdfsMergerPage():
    ui.page_title('ToolVerseKit PDFs Merger')
    ui.add_body_html('''
                        <style>
                            .youTubeMusicDownloader{
                                font-family : "Times New Roman" ;
                                align-self : center ;
                            }
                        </style>
                     ''')
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homeLoggedPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager' , target = passwordManagerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader' , target = youTubeMusicDownloaderPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'solar_power' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Solar Panels Production Prediction' , target = solarPanelProductionPredictionPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        with ui.row():
            with ui.button(icon='menu' , color ='black'):
                with ui.menu() as menu:
                    with ui.row():
                        ui.icon(name = 'account_circle' , size = '40px')
                        ui.menu_item('Profile' , on_click = lambda : universalFunctions.goToPage(page = 'profile')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'credit_card' , size = '40px')
                        ui.menu_item('Payment Methods' , on_click = lambda : universalFunctions.goToPage(page = 'paymentMethods')).style('font-family : "Times New Roman" ; font-size : 20px')
                    ui.separator()
                    with ui.row():
                        ui.icon(name = 'logout' , size = '40px')
                        ui.menu_item('Logout', on_click = lambda : universalFunctions.goToPage(page = 'home')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'close' , size = '40px')
                        ui.menu_item('Close', on_click = menu.close).style('font-family : "Times New Roman" ; font-size : 20px')
@ui.page('/solarPanelProductionPrediction')
def solarPanelProductionPredictionPage():
    def csvtotable(e:events.UploadEventArguments):
        with StringIO(e.content.read().decode('utf-8')) as f:
            df = pd.read_csv(f)
            df.to_csv(rf"{folder}\A se prezice.csv" , index = False)# Seteaza calea catre fisierul CSV cu datele noi
        new_data_path = rf"{folder}\A se prezice.csv"
        # Incarca datele noi intr-un DataFrame
        new_data = pd.read_csv(new_data_path)
        # Adauga o coloana 'Kw' initializata cu NaN (sau o valoare implicita)
        new_data['Kw'] = np.nan
        # Pregatește datele pentru predictie
        X_new = new_data.drop("Kw", axis=1)  # Excludem coloana de iesire ("Kw") din datele noi
        # Bariabilele categorice in variabile one-hot (dacă exista)
        if 'Sezon' in X_new.columns:
            X_new_encoded = pd.get_dummies(X_new, columns=["Sezon"])
        else:
            X_new_encoded = X_new
        # Incarcă modelul antrenat
        model_filename = rf"{folder}\Modele\trained_model.joblib"
        model = load(model_filename)
        # Incarcă si scaler-ul folosit în timpul antrenarii
        scaler_filename = rf"{folder}\Modele\trained_scaler.joblib"
        scaler = load(scaler_filename)
        # Utilizeaza scaler-ul pentru a normaliza datele noi
        X_new_scaled = scaler.transform(X_new_encoded)
        # Realizeaza predictii pe datele noi
        y_pred_new = model.predict(X_new_scaled)
        # Actualizeaza coloana 'Kw' cu valorile prezise
        output_csv_path = rf"{folder}\Prezicerea\Rezultat.csv"
        new_data['Kw'] = y_pred_new
        new_data.to_csv(output_csv_path, index=False)
        table1.rows = []
        table1.update
        csv_file_path = f'{folder}\Prezicerea\Rezultat.csv'
        data_list = []
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_dict = {
                            'Sezon': row['Sezon'],
                            'Ora': row['Ora'],
                            'Temperatura': row['Temperatura'],
                            'Umbra': row['Umbra'],
                            'Radiatia Solara': row['Radiatia Solara'],
                            'Kw' : row['Kw']
                        }
                data_list.append(data_dict)
            for data_dict in data_list:
                table1.add_rows(data_dict)
    ui.page_title('ToolVerseKit Solar Panel Production Prediction')
    with ui.header().style('background-color : white'):
        ui.link(text = 'Home' , target = homeLoggedPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'password' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'Password Manager' , target = passwordManagerPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'music_note' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'YouTube Music Downloader' , target = youTubeMusicDownloaderPage).style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        ui.icon(name = 'picture_as_pdf' , color = 'black').tailwind.font_size('3xl')
        ui.link(text = 'PDFs Merger').style('text-decoration : none ; color : black ; font-family : "Times New Roman" ; font-size : 20px ;')
        with ui.row():
            with ui.button(icon='menu' , color ='black'):
                with ui.menu() as menu:
                    with ui.row():
                        ui.icon(name = 'account_circle' , size = '40px')
                        ui.menu_item('Profile' , on_click = lambda : universalFunctions.goToPage(page = 'profile')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'credit_card' , size = '40px')
                        ui.menu_item('Payment Methods' , on_click = lambda : universalFunctions.goToPage(page = 'paymentMethods')).style('font-family : "Times New Roman" ; font-size : 20px')
                        ui.separator()
                    with ui.row():
                        ui.icon(name = 'logout' , size = '40px')
                        ui.menu_item('Logout', on_click = lambda : universalFunctions.goToPage(page = 'home')).style('font-family : "Times New Roman" ; font-size : 20px')
                    with ui.row():
                        ui.icon(name = 'close' , size = '40px')
                        ui.menu_item('Close', on_click = menu.close).style('font-family : "Times New Roman" ; font-size : 20px')
    with ui.tabs().classes('w-full') as tabs:
        addTab = ui.tab('Add data')
        uploadTab = ui.tab('Upload data')
    with ui.tab_panels(tabs, value=uploadTab).classes('w-full'):
        with ui.tab_panel(addTab):
            with ui.row():
                columns = [{'name' : 'Sezon' , 'label' : 'Sezon' , 'field' : 'Sezon' , 'align' : 'center'},
                            {'name' : 'Ora' , 'label' : 'Ora' , 'field' : 'Ora' , 'align' : 'center'},
                            {'name' : 'Temperatura' , 'label' : 'Temperatura' , 'field' : 'Temperatura' , 'align' : 'center'},
                            {'name' : 'Umbra' , 'label' : 'Umbra' , 'field' : 'Umbra' , 'align' : 'center'},
                            {'name' : 'Radiatia Solara' , 'label' : 'Radiatia Solara' , 'field' : 'Radiatia Solara' , 'align' : 'center'},
                            {'name' : 'Kw' , 'label' : 'Kw' , 'field' : 'Kw' , 'align' : 'center'},
                        ]
                table = ui.table(columns = columns , rows = [] , row_key = 'id').classes('table1')
                with ui.column():
                    with ui.row():
                        ui.label('Sezon :')
                        sezonSelect = ui.select(['' , 'Iarna' , 'Primavara' , 'Vara' , 'Toamna'])
                        sezonSelect.classes('selecturi')
                    with ui.row():
                        ui.label('Ora :')
                        oraSelect = ui.select(['' , *map(str,range(8 , 17))])
                        oraSelect.classes('selecturi')
                    with ui.row():
                        ui.label('Temperatura :')
                        temperaturaSelect = ui.select(['' , *map(str,range(-20 , 41))])
                        temperaturaSelect.classes('selecturi')
                    with ui.row():
                        ui.label('Umbra(%) :')
                        umbraSelect = ui.select(['' , *map(str,range(0 , 100))])
                        umbraSelect.classes('selecturi')
                    with ui.row():
                        ui.label('Radiatia Solara(W/m²) :')
                        radiatiaSolaraSelect = ui.select(['' , *map(str,range(0 , 100))])
                        radiatiaSolaraSelect.classes('selecturi')
                    with ui.row():
                        butonAdaugaDate = ui.button('Adauga Date' , on_click = solarPanelProductionPredictionFunctions.addData(sezonSelect , oraSelect , temperaturaSelect , umbraSelect , radiatiaSolaraSelect , table)).tailwind.background_color('white').text_color('black').text_transform('normal-case').font_size('lg')
                        butonStartPrezicere = ui.button('Start Prezicere' , on_click = solarPanelProductionPredictionFunctions.startPrediction(table)).tailwind.background_color('white').text_color('black').text_transform('normal-case').font_size('lg')
                    butonDownloadPrezicere = ui.button('Download Prezicere' , on_click = lambda : ui.download(rf'{folder}\Prezicerea\Rezultat.csv')).tailwind.background_color('white').text_color('black').text_transform('normal-case').font_size('lg').position('relative').top_right_bottom_left('left-16')
        with ui.tab_panel(uploadTab):
            ui.add_head_html('''
                                <style>
                                    .table1 tbody td , .table1 th{
                                        font-family: 'Times New Roman' ;
                                        font-size : 20px ;
                                    }
                                </style>
                            ''')
            with ui.row():
                with ui.card():
                    with ui.column():
                        ui.upload(label = 'Incarca datele tale csv fara coloana Kw' , on_upload = csvtotable)
                        butonDownloadPrezicere1 = ui.button('Download Prezicere' , on_click = lambda : ui.download(rf'{folder}\Prezicerea\Rezultat.csv')).tailwind.background_color('white').text_color('black').text_transform('normal-case').font_size('lg')
                columns = [{'name' : 'Sezon' , 'label' : 'Sezon' , 'field' : 'Sezon' , 'align' : 'center'},
                        {'name' : 'Ora' , 'label' : 'Ora' , 'field' : 'Ora' , 'align' : 'center'},
                        {'name' : 'Temperatura' , 'label' : 'Temperatura' , 'field' : 'Temperatura' , 'align' : 'center'},
                        {'name' : 'Umbra' , 'label' : 'Umbra' , 'field' : 'Umbra' , 'align' : 'center'},
                        {'name' : 'Radiatia Solara' , 'label' : 'Radiatia Solara' , 'field' : 'Radiatia Solara' , 'align' : 'center'},
                        {'name' : 'Kw' , 'label' : 'Kw' , 'field' : 'Kw' , 'align' : 'center'},
                    ]
                table1 = ui.table(columns = columns , rows = [] , row_key = 'id').classes('table1')
homePage()
ui.run(dark = True , title = 'ToolVerseKit')
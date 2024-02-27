import configparser,os
from nicegui import ui
###Variables
config = configparser.ConfigParser()
columns = [
    {'name' : 'ID', 'label' : 'ID' , 'field' : 'ID' },
    {'name' : 'Site/App' , 'label' : 'Site/App' , 'field' : 'Site/App' , 'align' : 'center'},
    {'name' : 'User' , 'label' : 'User' , 'field' : 'User' , 'align' : 'center'},
    {'name' : 'Password' , 'label' : 'Password' , 'field' : 'Password' , 'align' : 'center'},
]
rows = []
rows_passwords_unhidden = []
program_data_path = os.getenv('PROGRAMDATA')+'\Password Manager By Manafique'
if not os.path.exists(os.getenv('PROGRAMDATA')+'\Password Manager By Manafique'):
    os.makedirs(os.getenv('PROGRAMDATA')+'\Password Manager By Manafique')
###
###Functions
def addAccount():
    next_id = len(rows_passwords_unhidden) + 1
    if newSiteApp.value and newUser.value and newPassword.value != '':
        id_taken = any(account['ID'] == next_id for account in rows_passwords_unhidden)
        if id_taken:
            next_id = max(account['ID'] for account in rows_passwords_unhidden) + 1
        new_account = {
            'ID': next_id,
            'Site/App': newSiteApp.value,
            'User': newUser.value,
            'Password': newPassword.value
        }
        rows_passwords_unhidden.append(new_account)
        table1.add_rows(new_account)
        config['Account{}'.format(next_id)] = {
            'ID': next_id,
            'Site/App': newSiteApp.value,
            'User': newUser.value,
            'Password': newPassword.value
        }
        with open(f'{program_data_path}\Accounts.ini', 'w') as configfile:
            config.write(configfile)
        newSiteApp.value, newUser.value, newPassword.value = '', '', ''
    else:
        ui.notify('You need to complete all text inputs to add a new account !')
async def showHidePasswords():
    if showHidePasswordsButton.text == 'Show Passwords':
        showHidePasswordsButton.set_text('Hide Passwords')
        await ui.run_javascript('''
            var tableElements = document.querySelectorAll('.table1');
            tableElements.forEach(function(tableElement) {
                var lastColumnHeader = tableElement.querySelector('th:last-child');
                var lastColumnCells = tableElement.querySelectorAll('tbody td:last-child');
                lastColumnHeader.style.display = 'table-cell';
                lastColumnCells.forEach(function(cell) {
                    cell.style.display = 'table-cell';
                });
            });
        ''')
    else:
        showHidePasswordsButton.set_text('Show Passwords')
        await ui.run_javascript('''
            var tableElements = document.querySelectorAll('.table1');
            tableElements.forEach(function(tableElement) {
                var lastColumnHeader = tableElement.querySelector('th:last-child');
                var lastColumnCells = tableElement.querySelectorAll('tbody td:last-child');
                lastColumnHeader.style.display = 'none';
                lastColumnCells.forEach(function(cell) {
                    cell.style.display = 'none';
                });
            });
        ''')
def removeAccount():
    selected_rows = table1.selected
    if selected_rows:
        while selected_rows:
            selected_rows = table1.selected
            selected_row = selected_rows[0]
            user_to_remove = selected_row['ID']
            for index, row in enumerate(rows_passwords_unhidden):
                if row['ID'] == user_to_remove:
                    del rows_passwords_unhidden[index]
                    config.remove_section(f'Account{index + 1}')
                    with open(f'{program_data_path}\Accounts.ini', 'w') as configfile:
                        config.write(configfile)
                    rows_to_remove = [r for r in table1.rows if r['ID'] == user_to_remove]
                    for row_to_remove in rows_to_remove:
                        table1.remove_rows(row_to_remove)
                    updated_config = configparser.ConfigParser()
                    for idx, account in enumerate(rows_passwords_unhidden, start=1):
                        updated_config[f'Account{idx}'] = {
                            'ID': account['ID'],
                            'Site/App': account['Site/App'],
                            'User': account['User'],
                            'Password': account['Password']
                        }
                    with open(f'{program_data_path}\Accounts.ini', 'w') as configfile:
                        updated_config.write(configfile)
    else:
        ui.notify('Select a row to remove !')
###
ui.label('Password Manager').tailwind.font_size('6xl').align_self('center').font_family('serif')
ui.label('By Manafique').tailwind.font_size('5xl').align_self('center').font_family('serif')
ui.label('Discord: manafique.alex').tailwind.font_size('4xl').align_self('center').font_family('serif')
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
                                    width : 675px;
                                }
                            </style>
                        ''')

        table1 = ui.table(columns = columns , rows = rows ,  row_key = 'ID' , selection = 'multiple').classes('table1').props('v-slot:body')
        ui.add_head_html('''
                            <style>
                                .table1 tbody td{
                                    font-size : 14px;
                                    font-family : serif;
                                    max-width: 150px;
                                    white-space: pre-wrap;
                                    word-wrap: break-word; /* Wrap long words onto new lines */
                                }
                                .table1 th{
                                    font-size : 19px;
                                    font-family : serif;
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
            newSiteApp.tailwind.font_family('serif')
            newUser = ui.input('User')
            newUser.tailwind.font_family('serif')
            newUser.style('position : relative ; right : -55px ;')
            newPassword = ui.input('Password' , password = True , password_toggle_button = True)
            newPassword.tailwind.font_family('serif')
            newPassword.style('position : relative ; right : -115px ;')
        with ui.row():
            addAccountButton = ui.button('Add Account' , on_click = addAccount , icon = 'person_add')
            addAccountButton.tailwind.font_family('serif').background_color('white').text_color('black')
            removeAccountButton = ui.button('Remove Account' , on_click = removeAccount , icon = 'delete')
            removeAccountButton.tailwind.font_family('serif').background_color('white').text_color('black')
            removeAccountButton.style('position : relative ; right : -40px ;')
            showHidePasswordsButton = ui.button('Show Passwords' , on_click = showHidePasswords , icon = 'visibility')
            showHidePasswordsButton.tailwind.font_family('serif').background_color('white').text_color('black')
            showHidePasswordsButton.style('position : relative ; right : -52px ;')
if os.path.exists(f'{program_data_path}\Accounts.ini'):
    config.read(f'{program_data_path}\Accounts.ini')
    required_keys = ['ID' , 'Site/App', 'User', 'Password']
    for section in config.sections():
        if all(key in config[section] for key in required_keys):
            accounts_unhidden = {
                'ID': config[section]['ID'],
                'Site/App': config[section]['Site/App'],
                'User': config[section]['User'],
                'Password': config[section]['Password']
            }
            rows_passwords_unhidden.append(accounts_unhidden)
            table1.add_rows(accounts_unhidden)
ui.run(dark = True , title = 'Password Manager' , native = True , reload = False , window_size = [715,700])

from nicegui import ui
import main
def addAccount(rows_passwords_unhidden , siteApp , user , password , table):
    next_id = len(rows_passwords_unhidden) + 1
    if siteApp and user and password != '':
        id_taken = any(account['ID'] == next_id for account in rows_passwords_unhidden)
        if id_taken:
            next_id = max(account['ID'] for account in rows_passwords_unhidden) + 1
        new_account = {
            'ID': next_id,
            'Site/App': siteApp.value,
            'User': user.value,
            'Password': password.value
        }
        rows_passwords_unhidden.append(new_account)
        table.add_rows(new_account)
        siteApp.value , user.value , password.value = '' , '' , ''
    else:
        ui.notify('You need to complete all text inputs to add a new account !')
async def showHidePasswords(button):
    if button.text == 'Show Passwords':
        button.set_text('Hide Passwords')
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
        button.set_text('Show Passwords')
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
def removeAccount(table , rows_passwords_unhidden):
    selected_rows = table.selected
    if selected_rows:
        while selected_rows:
            selected_rows = table.selected
            selected_row = selected_rows[0]
            user_to_remove = selected_row['ID']
            for index, row in enumerate(rows_passwords_unhidden):
                if row['ID'] == user_to_remove:
                    del rows_passwords_unhidden[index]
                    rows_to_remove = [r for r in table.rows if r['ID'] == user_to_remove]
                    for row_to_remove in rows_to_remove:
                        table.remove_rows(row_to_remove)
    else:
        ui.notify('Select a row to remove !')
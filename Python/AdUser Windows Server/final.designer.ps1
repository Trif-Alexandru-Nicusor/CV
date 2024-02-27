$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin)

    {

        $scriptPath = $MyInvocation.MyCommand.Path

        Start-Process powershell.exe -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`""

        exit

    }

$scriptPath=$MyInvocation.MyCommand.Path

$ScriptDirectory=Split-Path -Parent -Path (Get-Item -Path $scriptPath -Force).FullName

$smspath=$ScriptDirectory+"\sendsms_1.exe"

$smslogpath="$ScriptDirectory\sms_log.txt"

$emaillogpath="$ScriptDirectory\eml_log.txt"

Add-Type -AssemblyName System.Windows.Forms

Add-Type -AssemblyName 'System.Web'

import-module ActiveDirectory

$Form1 = New-Object -TypeName System.Windows.Forms.Form

[System.Windows.Forms.TabControl]$TabControl1 = $null

[System.Windows.Forms.TabPage]$TabPage1 = $null

[System.Windows.Forms.Button]$butonCreare = $null

[System.Windows.Forms.TextBox]$nrCerereCreare = $null

[System.Windows.Forms.TextBox]$nrTelCreare = $null

[System.Windows.Forms.TextBox]$emailCreare = $null

[System.Windows.Forms.TextBox]$totNumeleCreare = $null

[System.Windows.Forms.TextBox]$prenumeCreare = $null

[System.Windows.Forms.TextBox]$numeCreare = $null

[System.Windows.Forms.Label]$Label6 = $null

[System.Windows.Forms.Label]$Label5 = $null

[System.Windows.Forms.Label]$Label4 = $null

[System.Windows.Forms.Label]$Label3 = $null

[System.Windows.Forms.Label]$Label2 = $null

[System.Windows.Forms.Label]$Label1 = $null

[System.Windows.Forms.TabPage]$TabPage2 = $null

[System.Windows.Forms.Button]$butonResetare = $null

[System.Windows.Forms.TextBox]$nrCerereResetare = $null

[System.Windows.Forms.TextBox]$nrTelefonResetare = $null

[System.Windows.Forms.TextBox]$emailResetare = $null

[System.Windows.Forms.TextBox]$numeUtilizatorResetare = $null

[System.Windows.Forms.Label]$Label10 = $null

[System.Windows.Forms.Label]$Label9 = $null

[System.Windows.Forms.Label]$Label8 = $null

[System.Windows.Forms.Label]$Label7 = $null

function InitializeComponent

{

$TabControl1 = (New-Object -TypeName System.Windows.Forms.TabControl)

$TabPage1 = (New-Object -TypeName System.Windows.Forms.TabPage)

$TabPage2 = (New-Object -TypeName System.Windows.Forms.TabPage)

$Label1 = (New-Object -TypeName System.Windows.Forms.Label)

$Label2 = (New-Object -TypeName System.Windows.Forms.Label)

$Label3 = (New-Object -TypeName System.Windows.Forms.Label)

$Label4 = (New-Object -TypeName System.Windows.Forms.Label)

$Label5 = (New-Object -TypeName System.Windows.Forms.Label)

$Label6 = (New-Object -TypeName System.Windows.Forms.Label)

$numeCreare = (New-Object -TypeName System.Windows.Forms.TextBox)

$prenumeCreare = (New-Object -TypeName System.Windows.Forms.TextBox)

$totNumeleCreare = (New-Object -TypeName System.Windows.Forms.TextBox)

$emailCreare = (New-Object -TypeName System.Windows.Forms.TextBox)

$nrTelCreare = (New-Object -TypeName System.Windows.Forms.TextBox)

$nrCerereCreare = (New-Object -TypeName System.Windows.Forms.TextBox)

$butonCreare = (New-Object -TypeName System.Windows.Forms.Button)

$Label7 = (New-Object -TypeName System.Windows.Forms.Label)

$Label8 = (New-Object -TypeName System.Windows.Forms.Label)

$Label9 = (New-Object -TypeName System.Windows.Forms.Label)

$Label10 = (New-Object -TypeName System.Windows.Forms.Label)

$numeUtilizatorResetare = (New-Object -TypeName System.Windows.Forms.TextBox)

$emailResetare = (New-Object -TypeName System.Windows.Forms.TextBox)

$nrTelefonResetare = (New-Object -TypeName System.Windows.Forms.TextBox)

$nrCerereResetare = (New-Object -TypeName System.Windows.Forms.TextBox)

$butonResetare = (New-Object -TypeName System.Windows.Forms.Button)

$TabControl1.SuspendLayout()

$TabPage1.SuspendLayout()

$TabPage2.SuspendLayout()

$Form1.SuspendLayout()

#

#TabControl1

#

$TabControl1.Controls.Add($TabPage1)

$TabControl1.Controls.Add($TabPage2)

$TabControl1.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]3,[System.Int32]3))

$TabControl1.Name = [System.String]'TabControl1'

$TabControl1.SelectedIndex = [System.Int32]0

$TabControl1.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]464,[System.Int32]390))

$TabControl1.TabIndex = [System.Int32]0

#

#TabPage1

#

$TabPage1.Controls.Add($butonCreare)

$TabPage1.Controls.Add($nrCerereCreare)

$TabPage1.Controls.Add($nrTelCreare)

$TabPage1.Controls.Add($emailCreare)

$TabPage1.Controls.Add($totNumeleCreare)

$TabPage1.Controls.Add($prenumeCreare)

$TabPage1.Controls.Add($numeCreare)

$TabPage1.Controls.Add($Label6)

$TabPage1.Controls.Add($Label5)

$TabPage1.Controls.Add($Label4)

$TabPage1.Controls.Add($Label3)

$TabPage1.Controls.Add($Label2)

$TabPage1.Controls.Add($Label1)

$TabPage1.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]4,[System.Int32]36))

$TabPage1.Name = [System.String]'TabPage1'

$TabPage1.Padding = (New-Object -TypeName System.Windows.Forms.Padding -ArgumentList @([System.Int32]3))

$TabPage1.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]456,[System.Int32]350))

$TabPage1.TabIndex = [System.Int32]0

$TabPage1.Text = [System.String]'Creare cont'

$TabPage1.UseVisualStyleBackColor = $true

#

#TabPage2

#

$TabPage2.Controls.Add($butonResetare)

$TabPage2.Controls.Add($nrCerereResetare)

$TabPage2.Controls.Add($nrTelefonResetare)

$TabPage2.Controls.Add($emailResetare)

$TabPage2.Controls.Add($numeUtilizatorResetare)

$TabPage2.Controls.Add($Label10)

$TabPage2.Controls.Add($Label9)

$TabPage2.Controls.Add($Label8)

$TabPage2.Controls.Add($Label7)

$TabPage2.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]4,[System.Int32]36))

$TabPage2.Name = [System.String]'TabPage2'

$TabPage2.Padding = (New-Object -TypeName System.Windows.Forms.Padding -ArgumentList @([System.Int32]3))

$TabPage2.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]456,[System.Int32]350))

$TabPage2.TabIndex = [System.Int32]1

$TabPage2.Text = [System.String]'Resetare cont'

$TabPage2.UseVisualStyleBackColor = $true

#

#Label1

#

$Label1.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]6))

$Label1.Name = [System.String]'Label1'

$Label1.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]82,[System.Int32]23))

$Label1.TabIndex = [System.Int32]0

$Label1.Text = [System.String]'Nume :'

#

#Label2

#

$Label2.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]58))

$Label2.Name = [System.String]'Label2'

$Label2.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]110,[System.Int32]23))

$Label2.TabIndex = [System.Int32]1

$Label2.Text = [System.String]'Prenume :'

$Label2.add_Click($Label2_Click)

#

#Label3

#

$Label3.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]113))

$Label3.Name = [System.String]'Label3'

$Label3.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]133,[System.Int32]23))

$Label3.TabIndex = [System.Int32]2

$Label3.Text = [System.String]'Tot numele :'

#

#Label4

#

$Label4.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]162))

$Label4.Name = [System.String]'Label4'

$Label4.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]93,[System.Int32]23))

$Label4.TabIndex = [System.Int32]3

$Label4.Text = [System.String]'E-mail :'

#

#Label5

#

$Label5.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]213))

$Label5.Name = [System.String]'Label5'

$Label5.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]128,[System.Int32]23))

$Label5.TabIndex = [System.Int32]4

$Label5.Text = [System.String]'Nr. telefon :'

#

#Label6

#

$Label6.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]270))

$Label6.Name = [System.String]'Label6'

$Label6.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]128,[System.Int32]23))

$Label6.TabIndex = [System.Int32]5

$Label6.Text = [System.String]'Nr. cerere :'

$Label6.add_Click($Label6_Click)

#

#numeCreare

#

$numeCreare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]81,[System.Int32]3))

$numeCreare.Name = [System.String]'numeCreare'

$numeCreare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]224,[System.Int32]35))

$numeCreare.TabIndex = [System.Int32]6

$numeCreare.add_TextChanged($TextBox1_TextChanged)

#

#prenumeCreare

#

$prenumeCreare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]106,[System.Int32]55))

$prenumeCreare.Name = [System.String]'prenumeCreare'

$prenumeCreare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]199,[System.Int32]35))

$prenumeCreare.TabIndex = [System.Int32]7

$prenumeCreare.add_TextChanged($prenumeCreare_TextChanged)

$prenumeCreare.add_TextChanged({updateText})

#

#totNumeleCreare

#

$totNumeleCreare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]129,[System.Int32]110))

$totNumeleCreare.Name = [System.String]'totNumeleCreare'

$totNumeleCreare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]277,[System.Int32]35))

$totNumeleCreare.TabIndex = [System.Int32]8

$totNumeleCreare.add_TextChanged($TextBox3_TextChanged)

#

#emailCreare

#

$emailCreare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]81,[System.Int32]159))

$emailCreare.Name = [System.String]'emailCreare'

$emailCreare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]325,[System.Int32]35))

$emailCreare.TabIndex = [System.Int32]9

#

#nrTelCreare

#

$nrTelCreare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]129,[System.Int32]210))

$nrTelCreare.Name = [System.String]'nrTelCreare'

$nrTelCreare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]277,[System.Int32]35))

$nrTelCreare.TabIndex = [System.Int32]10

$nrTelCreare.Text = [System.String]'+40'

$nrTelCreare.add_TextChanged($TextBox5_TextChanged)

#

#nrCerereCreare

#

$nrCerereCreare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]129,[System.Int32]267))

$nrCerereCreare.Name = [System.String]'nrCerereCreare'

$nrCerereCreare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]95,[System.Int32]35))

$nrCerereCreare.TabIndex = [System.Int32]11

#

#butonCreare

#

$butonCreare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]318))

$butonCreare.Name = [System.String]'butonCreare'

$butonCreare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]133,[System.Int32]30))

$butonCreare.TabIndex = [System.Int32]12

$butonCreare.Text = [System.String]'Creare cont'

$butonCreare.UseVisualStyleBackColor = $true

$butonCreare.Add_Click({CreareContClick})

#

#Label7

#

$Label7.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]3,[System.Int32]3))

$Label7.Name = [System.String]'Label7'

$Label7.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]175,[System.Int32]23))

$Label7.TabIndex = [System.Int32]0

$Label7.Text = [System.String]'Nume utilizator :'

$Label7.add_Click($Label7_Click)

#

#Label8

#

$Label8.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]55))

$Label8.Name = [System.String]'Label8'

$Label8.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]89,[System.Int32]23))

$Label8.TabIndex = [System.Int32]1

$Label8.Text = [System.String]'E-mail :'

#

#Label9

#

$Label9.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]99))

$Label9.Name = [System.String]'Label9'

$Label9.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]128,[System.Int32]23))

$Label9.TabIndex = [System.Int32]2

$Label9.Text = [System.String]'Nr. telefon :'

#

#Label10

#

$Label10.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]0,[System.Int32]155))

$Label10.Name = [System.String]'Label10'

$Label10.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]128,[System.Int32]23))

$Label10.TabIndex = [System.Int32]3

$Label10.Text = [System.String]'Nr. cerere :'

#

#numeUtilizatorResetare

#

$numeUtilizatorResetare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]174,[System.Int32]3))

$numeUtilizatorResetare.Name = [System.String]'numeUtilizatorResetare'

$numeUtilizatorResetare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]282,[System.Int32]35))

$numeUtilizatorResetare.TabIndex = [System.Int32]4

#

#emailResetare

#

$emailResetare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]95,[System.Int32]52))

$emailResetare.Name = [System.String]'emailResetare'

$emailResetare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]361,[System.Int32]35))

$emailResetare.TabIndex = [System.Int32]5

#

#nrTelefonResetare

#

$nrTelefonResetare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]134,[System.Int32]96))

$nrTelefonResetare.Name = [System.String]'nrTelefonResetare'

$nrTelefonResetare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]322,[System.Int32]35))

$nrTelefonResetare.TabIndex = [System.Int32]6

$nrTelefonResetare.Text = [System.String]'+40'

#

#nrCerereResetare

#

$nrCerereResetare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]118,[System.Int32]152))

$nrCerereResetare.Name = [System.String]'nrCerereResetare'

$nrCerereResetare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]115,[System.Int32]35))

$nrCerereResetare.TabIndex = [System.Int32]7

#

#butonResetare

#

$butonResetare.Location = (New-Object -TypeName System.Drawing.Point -ArgumentList @([System.Int32]3,[System.Int32]202))

$butonResetare.Name = [System.String]'butonResetare'

$butonResetare.Size = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]106,[System.Int32]37))

$butonResetare.TabIndex = [System.Int32]8

$butonResetare.Text = [System.String]'Resetare'

$butonResetare.UseVisualStyleBackColor = $true

$butonResetare.Add_Click({ResetareContClick})

#

#Form1

#

$Form1.ClientSize = (New-Object -TypeName System.Drawing.Size -ArgumentList @([System.Int32]461,[System.Int32]389))

$Form1.Controls.Add($TabControl1)

$Form1.Font = (New-Object -TypeName System.Drawing.Font -ArgumentList @([System.String]'Times New Roman',[System.Single]18,[System.Drawing.FontStyle]::Regular,[System.Drawing.GraphicsUnit]::Point,([System.Byte][System.Byte]0)))

$Form1.Text = [System.String]'Creare/Resetare cont'

$Form1.add_Load($Form1_Load)

$TabControl1.ResumeLayout($false)

$TabPage1.ResumeLayout($false)

$TabPage1.PerformLayout()

$TabPage2.ResumeLayout($false)

$TabPage2.PerformLayout()

$Form1.ResumeLayout($false)

Add-Member -InputObject $Form1 -Name TabControl1 -Value $TabControl1 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name TabPage1 -Value $TabPage1 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name butonCreare -Value $butonCreare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name nrCerereCreare -Value $nrCerereCreare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name nrTelCreare -Value $nrTelCreare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name emailCreare -Value $emailCreare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name totNumeleCreare -Value $totNumeleCreare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name prenumeCreare -Value $prenumeCreare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name numeCreare -Value $numeCreare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label6 -Value $Label6 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label5 -Value $Label5 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label4 -Value $Label4 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label3 -Value $Label3 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label2 -Value $Label2 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label1 -Value $Label1 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name TabPage2 -Value $TabPage2 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name butonResetare -Value $butonResetare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name nrCerereResetare -Value $nrCerereResetare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name nrTelefonResetare -Value $nrTelefonResetare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name emailResetare -Value $emailResetare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name numeUtilizatorResetare -Value $numeUtilizatorResetare -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label10 -Value $Label10 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label9 -Value $Label9 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label8 -Value $Label8 -MemberType NoteProperty

Add-Member -InputObject $Form1 -Name Label7 -Value $Label7 -MemberType NoteProperty

}

function CreareContClick

    {

        $new_rand_password = [System.Web.Security.Membership]::GeneratePassword(10, 3)

        $samaccountname="$($prenumeCreare.Text).$($numeCreare.Text)"

        $userprincipalname = "$($prenumeCreare.Text).$($numeCreare.Text)@just.ro"

        $name="$($numeCreare.Text) $($prenumeCreare.Text)"

        $displayname="$($numeCreare.Text) $($prenumeCreare.Text)"

        $adUser = Get-ADUser -Filter "UserPrincipalName -eq '$userprincipalname'" -ErrorAction SilentlyContinue

        if ($adUser - $null)

            {  

                [System.Windows.Forms.MessageBox]::Show("Contu deja exista , trebuie introdus manual !", "Exista", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)

            }

        else

            {

                New-ADUser -SamAccountName $samaccountname -UserPrincipalName $userprincipalname -GivenName $prenumeCreare.Text -Surname $numeCreare.Text -Name $name -DisplayName $displayname -Enabled $true  -EmailAddress $userprincipalname -PasswordNeverExpires $true -AccountPassword (ConvertTo-SecureString -AsPlainText $new_rand_password -Force) -Path "DC=JUST,DC=ro"

            }

        $messagebody = "Conform cererii nr. " + $nrCerereCreare.Text + " contul " + $userprincipalname + " a fost creat iar parola este: " + "<br><br><b><font face='Trebuchet MS' color='red'>" + $new_rand_password + "</font></b>" + "<br><br><span style='font-family: Arial; color: black; font-size: 7pt; background-color: #99CCFF'>PID: " + $PID + " DateTime: " + (Get-Process -ID $PID).StartTime.toString() + "</span>" + "<br><br><span style='font-family: Arial; color: red; font-size: 7pt;'><b>Parola a fost generata prin mijloace automate, folosind un string securizat, si a fost comunicata in clar doar destinatarului prezentului email.<br>DTI nu isi asuma responsabilitatea privind activitatile derulate pe un cont de domeniu, i.e. casuta de posta electronica si activitate PC (local sau remote), de catre titularul acestuia sau a altor utilizatori care au intrat in posesia prezentelor credentiale de acces<br></span>"

        $messagesubject = "Credentiale noi cont - " + $userprincipalname

        Send-MailMessage -From 'dti@just.ro' -To $emailCreare.Text -Subject $messagesubject -Body $messagebody -SmtpServer 'mail.just.ro' -BodyAsHtml

        $sms_message = "Parola contului de domeniu " + $samaccountname + "@just.ro este: " + $new_rand_password + " "

        $sms_result = & $smspath @('-m', $sms_message, '-nr', $nrTelCreare.Text)

        $newl = "`n" + "Cond_domeniu: " + $userprincipalname + "`tPID: " + $PID + " DateTime: " + (Get-Process -ID $PID).StartTime.toString() + "`tDestinatar: " + $emailCreare.Text + "`tLucrare: " + $nrCerereCreare.Text

        Add-Content -path $emaillogpath -Value $newl -Encoding UTF8

        $newl1 = "`n" + "Cond_domeniu: " + $UserName + "`tPID: " + $PID + " DateTime: " + (Get-Process -ID $PID).StartTime.toString() + "`tDestinatar: " + $sms_dest + "`tLucrare: " + $nrCerereCreare.Text

        Add-Content -path $smslogpath -Value $newl1 -Encoding UTF8

        Add-Content -path $smslogpath -Value $sms_result  -Encoding UTF8

        Write-Host($smspath,$smslogpath,$emaillogpath)

    }

function ResetareContClick

    {

        $new_rand_password = [System.Web.Security.Membership]::GeneratePassword(10, 3)

        $messagebody = "Conform cererii nr. " + $nrCerereResetare.Text + " noua parola pentru contul " + $numeUtilizatorResetare.Text + " este: " + "<br><br><b><font face='Trebuchet MS' color='red'>" + $new_rand_password + "</font></b>" + "<br><br><span style='font-family: Arial; color: black; font-size: 7pt; background-color: #99CCFF'>PID: " + $PID + " DateTime: " + (Get-Process -ID $PID).StartTime.toString() + "</span>" + "<br><br><span style='font-family: Arial; color: red; font-size: 7pt;'><b>Parola a fost generata prin mijloace automate, folosind un string securizat, si a fost comunicata in clar doar destinatarului prezentului email.<br>DTI nu isi asuma responsabilitatea privind activitatile derulate pe un cont de domeniu, i.e. casuta de posta electronica si activitate PC (local sau remote), de catre titularul acestuia sau a altor utilizatori care au intrat in posesia prezentelor credentiale de acces<br></span>"

        $messagesubject = "Credentiale noi cont - " + $numeUtilizatorResetare.Text

        Send-MailMessage -From 'dti@just.ro' -To $emailResetare.Text -Subject $messagesubject -Body $messagebody -SmtpServer 'mail.just.ro' -BodyAsHtml

        $sms_message = "Parola contului de domeniu " + $numeUtilizatorResetare.Text + "@just.ro este: " + $new_rand_password + " "

        $sms_result = & $smspath @('-m', $sms_message, '-nr', $nrTelefonResetare.Text)

        $newl = "`n" + "Cond_domeniu: " + $numeUtilizatorResetare.Text + "`tPID: " + $PID + " DateTime: " + (Get-Process -ID $PID).StartTime.toString() + "`tDestinatar: " + $emailResetare.Text + "`tLucrare: " + $nrCerereResetare.Text

        Add-Content -path $emaillogpath -Value $newl -Encoding UTF8

        $newl1 = "`n" + "Cond_domeniu: " + $numeUtilizatorResetare.Text + "`tPID: " + $PID + " DateTime: " + (Get-Process -ID $PID).StartTime.toString() + "`tDestinatar: " + $nrTelefonResetare.Text + "`tLucrare: " + $nrCerereResetare.Text

        Add-Content -path $smslogpath -Value $newl1 -Encoding UTF8

        Add-Content -path $smslogpath -Value $sms_result  -Encoding UTF8

        $new_rand_password = ConvertTo-SecureString $new_rand_password -AsPlainText -Force

        Enable-ADAccount -Identity $numeUtilizatorResetare.Text

        Set-ADAccountPassword $numeUtilizatorResetare.Text -Reset -NewPassword $new_rand_password

    }

function updateText

    {

        $prenume = $prenumeCreare.Text

        $nume = $numeCreare.Text

        $newValue = "$prenume $nume"

        $totNumeleCreare.Text = $newValue

    }

. InitializeComponent

$Form1.ShowDialog()
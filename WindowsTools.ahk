Gui 1:Default
Gui 1:Color,000000
Gui, Font, S22 CWhite, Times New Roman
Gui, Add, Text, x32 y-1 w220 h30 gActivators, Windows Activator
Gui, Add, Text, x82 y59 w130 h30 gDownloads, Downloads
Gui, Add, Text, x32 y119 w220 h30 gCFU, Check For Updates
Gui, Add, Text, x62 y179 w170 h30 gUPP,Activate UPP
Gui, Show, x50 y50 h256 w287, Windows Tools
WinSet,Transparent,200,Windows Tools
Return

UPP:
    Run, %comspec% /c "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61", , Hide
    Run powercfg.cpl
    Sleep 1000
    Msgbox,,Activate Ultimate Performance Profile, Enable Ultimate Performance Profile , if u want.
Return

CFU:
    Run ms-settings:windowsupdate
    BlockInput, On
    Sleep 1000
    Loop 3
        {
            Send {tab}
        }
    Send {enter}
    BlockInput, Off
Return


GuiClose:
ExitApp
Return

Activators:
    Gui 2:Destroy
    Gui 2:Default
    Gui 2:Color,000000
    Gui, Font, S22 CWhite, Times New Roman
    Gui, Add, Text, x122 y-1 w70 h30 gHome, Home
    Gui, Add, Text, x92 y59 w140 h30 gPro, Professional
    Gui, Show, x340 y50 h93 w318, Windows Activator
    WinSet,Transparent,200,Windows Activator
    Return

    2GuiClose:
        Gui 2:Destroy
    Return
    
    Home:
        Run, %comspec% /c slmgr /ipk "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99" & slmgr /skms "kms8.msguides.com" & slmgr /ato, , Hide
    Return

    Pro:
        Run, %comspec% /c slmgr /ipk "W269N-WFGWX-YVC9B-4J6C9-T83GX" & slmgr /skms "kms8.msguides.com" & slmgr /ato, , Hide
    Return
Return

Downloads:
    Gui 3:Destroy
    Gui 3:Default
    Gui 3:Color,000000
    Gui, Font, S22 CWhite, Times New Roman
    Gui, Add, Text, x2 y-1 w330 h30 gTFA, Download Tools For Taskbar
    Gui, Add, Text, x2 y39 w270 h30 gDWM, Download HWMonitor
    Gui, Add, Text, x2 y79 w300 h30 gDGT, Download Gaming Things
    Gui, Add, Text, x2 y119 w310 h30 gDW, Download Windows 10/11
    Gui, Add, Text, x2 y159 w200 h30 gDR, Download Rufus
    Gui, Add, Text, x2 y199 w360 h30 gDNE, Download NVIDIA Experience
    Gui, Add, Text, x2 y239 w390 h30 gDAT, Download AnyDesk/TeamViewer
    Gui, Add, Text, x2 y279 w340 h30 gOC, Download Chrome
    Gui, Add, Text, x2 y319 w280 h30 gDW7, Download WinRar/7Zip
    Gui, Add, Text, x2 y359 w230 h30 gDU, Download uTorrent
    Gui, Add, Text, x2 y399 w240 h30 gDHAI, Download HideAllIp
    Gui, Add, Text, x2 y439 w300 h30 gDCT, Download Coding Things
    Gui, Show, x340 y50 h476 w390, Downloads
    WinSet,Transparent,200,Downloads
    Return

    TFA:
        UrlDownloadToFile,https://www.dm.origin.com/download,OriginThinSetup.exe
    Return

    DWM:
        UrlDownloadToFile,https://download.cpuid.com/hwmonitor/hwmonitor_1.48.zip,hwmonitor_1.48.zip
    Return

    DGT:
        MsgBox, 4, Download Gaming Things, You want to download Steam ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe,SteamSetup.exe
            }
        MsgBox, 4, Download Gaming Things, You want to download EpicGames ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi,EpicGamesLauncherInstaller.msi
            }
        MsgBox, 4, Download Gaming Things, You want to download League Of Legends ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://lol.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.eune.exe,Install League of Legends eune.exe
            }
        MsgBox, 4, Download Gaming Things, You want to download Ubisoft?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://ubistatic3-a.akamaihd.net/orbit/launcher_installer/UbisoftConnectInstaller.exe,UbisoftConnectInstaller.exe
            }
        MsgBox, 4, Download Gaming Things, You want to download Battle.net ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://eu.battle.net/download/getInstaller?os=win&installer=Battle.net-Setup.exe,Battle.net-Setup.exe
            }
    Return

    DW:
        MsgBox, 4, Download Gaming Things, You want to download Windows 10 ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://go.microsoft.com/fwlink/?LinkId=691209,Windows10.exe
            }
        MsgBox, 4, Download Gaming Things, You want to download Windows 11 ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://go.microsoft.com/fwlink/?linkid=2156295,Windows11.exe
            }
    Return

    DR:
        MsgBox, 4, Download Gaming Things, You want to download Rufus ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://github.com/pbatard/rufus/releases/download/v3.21/rufus-3.21p.exe,rufus-3.21p.exe
            }
    Return

    DNE:
        MsgBox, 4, Download Gaming Things, You want to download NVIDIA Experience ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://uk.download.nvidia.com/GFE/GFEClient/3.26.0.160/GeForce_Experience_v3.26.0.160.exe,GeForce_Experience_v3.26.0.160.exe
            }
    Return

    DAT:
        MsgBox, 4, Download Gaming Things, You want to download AnyDesk  ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://anydesk.com/en/downloads/thank-you?dv=win_exe,AnyDesk.exe
            }
        MsgBox, 4, Download Gaming Things, You want to download TeamViewer  ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://download.teamviewer.com/download/TeamViewer_Setup_x64.exe,TeamViewer_Setup_x64.exe
            }
    Return

    OC:
        MsgBox, 4, Download Gaming Things, You want to download Chrome  ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B6C8DF38B-79EC-E56C-603C-3C7C42F09BC1%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe,ChromeSetup.exe
            }
    Return

    DW7:
        MsgBox, 4, Download Gaming Things, You want to download WinRar  ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-611.exe,winrar-x64-611.exe
            }
        MsgBox, 4, Download Gaming Things, You want to download 7Zip  ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://www.7-zip.org/a/7z2201-x64.exe,7z2201-x64.exe
            }   
    Return

    DU:
        MsgBox, 4, Download Gaming Things, You want to download uTorrent  ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://download-hr.utorrent.com/track/stable/endpoint/utorrent/os/windows,utorrent_installer.exe
            }   
    Return

    DHAI:
        MsgBox, 4, Download Gaming Things, You want to download HideAllIp  ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://www.hideallip.com/dwn/hideallipsetup.exe,hideallipsetup.exe
            }   
    Return

    DCT:
        MsgBox, 4, Download Gaming Things, You want to download Visual Studio ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=Release&version=VS2022&source=VSLandingPage&includeRecommended=true&cid=2030:b011c2f7-fdf2-42ca-8c71-5181939d1930,VisualStudioSetup.exe
            } 
        MsgBox, 4, Download Gaming Things, You want to download Visual Studio Code ?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://az764295.vo.msecnd.net/stable/1ad8d514439d5077d2b0b7ee64d2ce82a9308e5a/VSCode-win32-x64-1.74.1.zip,VSCode-win32-x64-1.74.1.zip
            }
        MsgBox, 4, Download Gaming Things, You want to download Python 3.11.1?
        IfMsgBox, Yes
            {
                UrlDownloadToFile,https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe,python-3.11.1-amd64.exe
            }     
    Return

    3GuiClose:
        Gui 3:Destroy
    Return
Return
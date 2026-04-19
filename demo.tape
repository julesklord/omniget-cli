# demo.tape

Output demo.gif

Set Shell "pwsh"
Set FontSize 16
Set Width 1200
Set Height 800

Type ".\target\release\omniget-cli.exe --help"
Enter
Sleep 3s

Type ".\target\release\omniget-cli.exe download https://www.youtube.com/watch?v=dQw4w9WgXcQ"
Enter
Sleep 10s

Type ".\target\release\omniget-cli.exe download https://www.instagram.com/p/C3p_2q_A7Z_/"
Enter
Sleep 15s

Hide
Type "exit"
Enter

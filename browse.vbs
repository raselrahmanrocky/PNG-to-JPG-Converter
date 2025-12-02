Set objShell = CreateObject("Shell.Application")
Set objFolder = objShell.BrowseForFolder(0, "Select the Folder with your PNG files:", 0)

If objFolder Is Nothing Then
    ' User clicked Cancel, print an empty string
    WScript.Echo ""
Else
    ' Print the selected folder path
    WScript.Echo objFolder.Self.Path
End If
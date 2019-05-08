Sub UnmergeAndFill()
'
' Unmerge a range and fill blanks with duplicate values.
'
' Keyboard Shortcut: Ctrl+Shift+U
'

temp = ""
    Selection.UnMerge
    For Each cell In Selection
        If cell.Value <> "" Then
            temp = cell.Value
        Else
            cell.Value = temp
        End If
    Next cell
    

End Sub

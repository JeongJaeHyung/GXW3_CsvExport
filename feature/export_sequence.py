from package.key_press import key_press, hotkey_press

def work():
    export_speed = 0.05
    key_press(export_speed, 'e') # Select "Export to File" option
    key_press(export_speed, 'down') # Select "Program" option
    key_press(export_speed, 'enter') # Select "Local Label..." option
    key_press(export_speed, 'left') # Move to the Export to File Pop-up
    key_press(export_speed, 'enter') # Execute the Export to File Pop-up
    hotkey_press(export_speed, ['alt', 'tab']) # Select the
    hotkey_press(export_speed, ['alt', 'tab']) # Save work window
    key_press(export_speed, 'enter') # Continue the csv saving
    print(">>> [SUCCESS] Local Label 내보내기 완료")
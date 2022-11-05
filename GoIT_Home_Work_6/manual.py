def all_commands():
    """
    Функция показывает все возможные команды.
    :return: 'Enter new command.'
    """

    print('-' * 108)
    print('{:^35}|{:^20}|{:^15}|{:^16}|{:^16} |'.format(
        'DESCRIPTION', 'COMMAND', 'PARAMETER 1', 'PARAMETER 2', 'PARAMETER 3'))
    print('-' * 108)

    help_list = [
                ['Add contact', 'add', 'name', 'phone_number', ''],
                ['Add phone for contact', 'add_phone', 'name', 'phone_number', ''],
                ['Add birthday contact', 'add_birthday', 'name', 'YYYY.MM.DD', ''],
                ['Dell phone for contact', 'dell_phone', 'name', 'phone_number', ''],
                ['Change phone contact', 'change', 'name', 'old_phone_number', 'new_phone_number'],
                ['Show phone contact', 'phone', 'name', '', ''],
                ['Show all contacts', 'show_all', '', '', ''],
                ['Show how many days until birthday', 'show_birthday', 'name', '', ''],
                ['Show paging output', 'show_page', 'number', '', ''],
                ['Greetings', 'hello', '', '', ''],
                ['Save contacts and close the program', 'close', '', '', ''],
                ['Save contacts and close the program', 'exit', '', '', ''],
                ['Save contacts and close the program', 'good_bye', '', '', ''],
                ['Help on commands', 'help', '', '', '']
    ]
    for column_1, column_2, column_3, column_4, column_5 in help_list:
        text = ("{:<35}|{:^20}|{:^15}|{:^16}|{:^16} |".format(column_1, column_2, column_3, column_4, column_5))
        print(text)
    print('-' * 108)
    return 'Enter new command.'

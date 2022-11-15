"""
 * Email Scraper
 * Author: Sanjay Sunil
 * License: MIT
"""
import os
import webbrowser
from src.email_scraper import EmailScraper

OPTIONS = ["Scrape 1 Email", "Scrape Multiple Emails",
           "GitHub", "Exit"]
os.system('clear')

while True:
    os.system('clear')
    print("Email Scraper\n")
    [print(i+1, OPTIONS[i]) for i in range(len(OPTIONS))]
    print('\n')

    while True:
      try:
        option = int(input("Choose an option: "))
        break
      except ValueError:
        print('Please type an option number.\n')

    if option == 1:
        file_to_write = input('Enter filename to write to: ')
        scraper = EmailScraper(file_path=file_to_write)
        scraper.start(1)
        back_to_menu = input(
            f'Added 1 email to {scraper._file_path}!\n\nPress enter to go back to menu. ')

    elif option == 2:
        emails = int(input("Emails to scrape: "))
        file_to_write = input('Enter filename to write to: ')
        scraper = EmailScraper(file_path=file_to_write)
        scraper.start(emails)
        back_to_menu = input(
            f'Added {emails} emails to {scraper._file_path}!\n\nPress enter to go back to menu. ')

    elif option == 3:
        webbrowser.open(scraper._GITHUB_URL)

    elif option == 4:
      exit("Thank you for using email-scraper.")

    else:
        try_again = input(
            'Invalid option, please enter to try again. ')

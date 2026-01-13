import pytest

from selene import have

def test_automation_form(browser):
    browser.config.timeout = 10
    browser.driver.set_window_size(1920, 1080)

    browser.open('/automation-practice-form')

    # 1. Заполняем имя и фамилию
    browser.element('#firstName').type('Олег')
    browser.element('#lastName').type('Олегович')

    # 2. Вводим email
    browser.element('#userEmail').type('oleg.olegovich@example.com')

    # 3. Выбираем пол
    browser.element('[for="gender-radio-1"]').click()

    # 4. Вводим номер телефона
    browser.element('#userNumber').type('1234567890')

    # 5. Выбираем дату рождения через календарь
    browser.element('#dateOfBirthInput').click()

    # Выбираем год
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select') \
        .all('option') \
        .element_by(have.text('2000')) \
        .click()

    # Выбираем месяц
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select') \
        .all('option') \
        .element_by(have.text('July')) \
        .click()

    # Выбираем день
    browser.element('.react-datepicker__day--010').click()

    # 6. Вводим subject
    browser.element('#subjectsInput').type('Maths')
    browser.element('.subjects-auto-complete__menu').element('div').click()

    # 7. Выбираем хобби
    browser.element('[for="hobbies-checkbox-1"]').click()

    # 8. Загружаем файл
    browser.element('#uploadPicture').set_value('/Users/artiom/Downloads/_.jpeg')

    # 9. Вводим текущий адрес
    browser.element('#currentAddress').type('г. Москва, ул. 9-мая, д. 1')

    # 10. Выбираем State
    browser.element('#react-select-3-input').type('NCR')
    browser.element('[id^="react-select-3-option-"]').click()

    # 11. Выбираем City
    browser.element('#react-select-4-input').type('Delhi')
    browser.element('[id^="react-select-4-option-"]').click()

    # 12. Нажимаем кнопку Submit
    browser.element('#submit').click()

    # 13. Проверяем появление модального окна с подтверждением
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))


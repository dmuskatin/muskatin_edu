def test_e2e():
    # Импортируем тестируемые компоненты
    from app import App

    # Создаем экземпляр приложения и запускаем его
    app = App()
    app.start()

    # Симулируем действия пользователя и проверяем результат
    app.click_button("submit")
    assert app.get_text("result") == "Success"
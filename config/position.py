class PositionConfig():
    def __init__(self) -> None:
        self.username_xpath = "//*[@id = 'id_email']"
        self.password_xpath = "//*[@id = 'pwd']"
        self.search_xpath = '//*[@id="search-form-kw"]'
        self.login_btn = "//*[@id='btn_submit']"
        self.search_btn = '/html//button[@class="search-form-sb_bg"]'

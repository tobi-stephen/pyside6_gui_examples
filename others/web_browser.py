import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QTabWidget, QToolBar, QStatusBar, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QAction


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Zen Browser")
        
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)

        self.tabs.tabBarDoubleClicked.connect(self.new_tab_on_doubleclick)
        self.tabs.tabCloseRequested.connect(self.tab_close)
        self.tabs.currentChanged.connect(self.current_tab_changed)

        # Action Creation
        new_tab = QAction("New", self)
        new_tab.setStatusTip("Create a new tab")
        new_tab.triggered.connect(self.new_tab_up)

        quit_tab = QAction("Quit", self)
        quit_tab.setStatusTip("Quit Browser")
        quit_tab.triggered.connect(self.quit_tab_up)
        
        back_tab = QAction("Back", self)
        back_tab.setStatusTip("Go back to previous page")
        back_tab.triggered.connect(lambda: self.tabs.currentWidget().back())

        fwd_tab = QAction("Fwd", self)
        fwd_tab.setStatusTip("Forward to next page")
        fwd_tab.triggered.connect(lambda: self.tabs.currentWidget().forward())

        home_tab = QAction("Home", self)
        home_tab.setStatusTip("Go to browser home page")
        home_tab.triggered.connect(self.home_tab_up)

        refresh_tab = QAction("Refresh", self)
        refresh_tab.setStatusTip("Refresh current page")
        refresh_tab.triggered.connect(lambda: self.tabs.currentWidget().reload())

        self.address_tab = QLineEdit(self)
        self.address_tab.setPlaceholderText("Enter URL")
        self.address_tab.returnPressed.connect(self.goto_page)

        stop_tab = QAction("Stop", self)
        stop_tab.setStatusTip("Stop loading the page")
        stop_tab.triggered.connect(lambda: self.tabs.currentWidget().stop())
        
        self.secure_tab = QAction("Sec", self)
        self.secure_tab.setStatusTip("Indicates secure")
        
        # Menu Setup
        menu = self.menuBar()
        
        file_menu = menu.addMenu("&File")
        file_menu.addAction(new_tab)
        file_menu.addAction(quit_tab)

        help_menu = menu.addMenu("&Help")
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.about_message)

        # Toolbar setup
        file_toolbar = self.addToolBar("Nav")
        file_toolbar.addAction(back_tab)
        file_toolbar.addAction(fwd_tab)
        file_toolbar.addAction(refresh_tab)
        file_toolbar.addAction(home_tab)
        file_toolbar.addAction(self.secure_tab)
        file_toolbar.addWidget(self.address_tab)
        file_toolbar.addAction(stop_tab)

        # self.statusbar = QStatusBar(self)
        # self.setStatusBar(self.statusbar)
        
        self.new_tab_up(QUrl('http://www.google.com'), 'Home Page')
        self.setCentralWidget(self.tabs)
    
    def about_message(self):
        QMessageBox.aboutQt(self)

    def quit_tab_up(self):
        sys.exit()

    def home_tab_up(self):
        self.address_tab.setText(None)
        self.goto_page()

    def goto_page(self):
        url = self.address_tab.text()

        if self.tabs.count() < 1:
            self.new_tab_up(QUrl(url), url)
            return

        q = QUrl(url)
        if q.scheme() == "":
            q.setScheme("http")
        
        self.tabs.currentWidget().setUrl(q)
        # self.tabs.currentWidget().setWindowTitle(q.toString())
        self.update_addressbar(self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def tab_close(self, idx):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(idx)

    def new_tab_on_doubleclick(self, i):
        if i == -1:
            self.new_tab_up()

    def new_tab_up(self, qurl=None, label="Blank"):        
        if not qurl:
            qurl = QUrl('')
        
        web_view = QWebEngineView()
        web_view.setUrl(qurl)

        idx = self.tabs.addTab(web_view, label)
        self.tabs.setCurrentIndex(idx)
        
        web_view.urlChanged.connect(lambda qurl, view=web_view: self.update_addressbar(qurl, view))
        web_view.loadFinished.connect(lambda _, i=idx, browser=web_view: self.tabs.setTabText(i, web_view.page().title()))
        web_view.loadFinished.connect(lambda _, i=idx, browser=web_view: self.update_secure_bar(web_view.url(), web_view))

    def update_addressbar(self, q, browser=None):
        self.address_tab.setText(q.toString())
        self.address_tab.setCursorPosition(0)

    def update_title(self, browser=None):
        if browser != self.tabs.currentWidget():
            return 

        title = self.tabs.currentWidget().page().title()
        print("update title", title)
        self.setWindowTitle("%s - Zen Browser" % title)

    def update_secure_bar(self, q :QUrl, browser=None):
        if browser != self.tabs.currentWidget():
            return

        if q.scheme() == 'https':
            self.secure_tab.setText("Sec")
        else:
            self.secure_tab.setText("UnSec")

        self.address_tab.setText(q.toString())
        self.address_tab.setCursorPosition(0)

    def current_tab_changed(self, idx):
        qurl = self.tabs.currentWidget().url()
        print(qurl)
        self.update_addressbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())
        self.update_secure_bar(qurl, self.tabs.currentWidget())


if __name__=='__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.resize(400, 400)
    window.show()

    app.exec()
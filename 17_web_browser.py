import sys
from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox, QApplication, QTabWidget, QPushButton, QLineEdit
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crackers")

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.tabBarDoubleClicked.connect(self.tabBarDoubleClickedResponse)
        self.tabs.currentChanged.connect(self.currentChangedResponse)

        toolbar = self.addToolBar("Menu")
        newAction = toolbar.addAction("New")
        newAction.triggered.connect(self.addNewTab)

        backAction = toolbar.addAction("Back")
        backAction.triggered.connect(lambda: self.tabs.currentWidget().back())

        reloadAction = toolbar.addAction("Reload")
        reloadAction.triggered.connect(lambda: self.tabs.currentWidget().reload())

        fwdAction = toolbar.addAction("Fwd")
        fwdAction.triggered.connect(lambda: self.tabs.currentWidget().forward())

        self.secureAction = toolbar.addAction("UnSec")
        self.secureAction.triggered.connect(self.updateSecureIcon)

        self.addressBar = QLineEdit()
        self.addressBar.setPlaceholderText("Enter url here")
        self.addressBar.returnPressed.connect(self.goToUrl)
        toolbar.addWidget(self.addressBar)

        stopAction = toolbar.addAction("Stop")
        stopAction.triggered.connect(lambda: self.tabs.currentWidget().stop())

        aboutAction = toolbar.addAction("About")
        aboutAction.triggered.connect(lambda: QMessageBox.aboutQt(self))

        self.addNewTab(QUrl("www.google.com"), "www.google.com")

    def currentChangedResponse(self, idx):
        browser: QWebEngineView = self.tabs.widget(idx)
        self.updateLabelAndBar(browser.url(), browser)

    def tabBarDoubleClickedResponse(self, idx):
        if idx < 0:
            self.addNewTab()

    def updateSecureIcon(self):
        pass

    def goToUrl(self):
        url = self.addressBar.text().strip()
        if not url:
            return

        qurl = QUrl(url)
        qurl.setScheme('http')

        webView: QWebEngineView = self.tabs.currentWidget()
        webView.setUrl(qurl)

    def addNewTab(self, qurl=None, label='Blank'):
        if not qurl:
            qurl = QUrl('')

        qurl.setScheme('http')
        webView = QWebEngineView()
        webView.setUrl(qurl)
        webView.loadFinished.connect(lambda qurl=qurl, browser=webView: self.updateLabelAndBar(qurl, browser))

        idx = self.tabs.addTab(webView, label)
        self.tabs.setCurrentIndex(idx)

    def updateLabelAndBar(self, qurl: QUrl, browser: QWebEngineView = None):
        if not browser or browser != self.tabs.currentWidget():
            return

        self.addressBar.setText(qurl.toString())
        self.addressBar.setCursorPosition(0)
        self.tabs.currentWidget().setWindowTitle(self.tabs.currentWidget().page().title())

        scheme = browser.url().scheme()
        if scheme == 'https':
            self.secureAction.setText("Sec")
        else:
            self.secureAction.setText("UnSec")


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
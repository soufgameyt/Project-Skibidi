from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGraphicsOpacityEffect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QTimer
import socket

import LogicVariablesFactory
LogicVariables = LogicVariablesFactory.LogicVariables()

# App setup
ProjectSkibidi = QApplication([])
ProjectSkibidi.setWindowIcon(QIcon("Assets/Icons/ProjectSkibidi.jpg"))
ProjectSkibidi.setApplicationName("Project Skibidi")

# Main menu
SkibidiMainMenu = QLabel()
SkibidiMainMenu.resize(800, 600)
SkibidiMainMenu.setPixmap(QPixmap("Assets/Icons/ProjectSkibidi-Menu2.png"))
SkibidiMainMenu.setScaledContents(True)

# Play button
SkibidiPlayButton = QPushButton(SkibidiMainMenu)
SkibidiPlayButton.setIcon(QIcon("Assets/Icons/PLAYBUTTONXD.png"))
SkibidiPlayButton.setIconSize(QSize(200, 150))
SkibidiPlayButton.setFixedSize(200, 150)
SkibidiPlayButton.move(300, 400)
SkibidiPlayButton.setStyleSheet("border: none; background-color: transparent;")

# Loading screen
SkibidiLoadingScreen = QLabel(SkibidiMainMenu)
SkibidiLoadingScreen.resize(800, 600)
SkibidiLoadingScreen.setPixmap(QPixmap("Assets/Icons/LoadingScreen.png"))
SkibidiLoadingScreen.setScaledContents(True)
SkibidiLoadingScreen.hide()

# InGame screen
SkibidiInGameScreen = QLabel(SkibidiMainMenu)
SkibidiInGameScreen.resize(800, 600)
SkibidiInGameScreen.setPixmap(QPixmap("Assets/Icons/mainscreen.png"))
SkibidiInGameScreen.setScaledContents(True)
SkibidiInGameScreen.hide()

# Login failed screen
SkibidiLoginFailedScreen = QLabel(SkibidiMainMenu)
SkibidiLoginFailedScreen.resize(800, 600)
SkibidiLoginFailedScreen.setPixmap(QPixmap("Assets/Icons/serverdown.png"))
SkibidiLoginFailedScreen.setScaledContents(True)
SkibidiLoginFailedScreen.hide()

# Quit button
SkibidiQuitButton = QPushButton(SkibidiMainMenu)
SkibidiQuitButton.setIcon(QIcon("Assets/Icons/quitbutton.png"))
SkibidiQuitButton.setIconSize(QSize(200, 150))
SkibidiQuitButton.setFixedSize(200, 150)
SkibidiQuitButton.move(300, 400)
SkibidiQuitButton.setStyleSheet("border: none; background-color: transparent;")
SkibidiQuitButton.hide()
SkibidiQuitButton.clicked.connect(ProjectSkibidi.quit)

# Opacity thing
SkibidiEffect = QGraphicsOpacityEffect()
SkibidiLoadingScreen.setGraphicsEffect(SkibidiEffect)
SkibidiEffect.setOpacity(0)

SkibidiFadeIn = QPropertyAnimation(SkibidiEffect, b"opacity")
SkibidiFadeOut = QPropertyAnimation(SkibidiEffect, b"opacity")

def FireFadeIn():
    SkibidiLoadingScreen.show()
    SkibidiFadeIn.setDuration(1000)
    SkibidiFadeIn.setStartValue(0)
    SkibidiFadeIn.setEndValue(1)
    SkibidiFadeIn.start()

def FireFadeOut():
    SkibidiFadeOut.setDuration(1000)
    SkibidiFadeOut.setStartValue(1)
    SkibidiFadeOut.setEndValue(0)
    SkibidiFadeOut.start()
    SkibidiFadeOut.finished.connect(lambda: (
        SkibidiLoadingScreen.hide(),
        SkibidiInGameScreen.show(),
    ))
    SkibidiFadeOut.start()
    

def ServerConnection():
    server_ip = "127.0.0.1"
    server_port = 3993
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        client_socket.connect((server_ip, server_port))
        print("Connected to server")
    except ConnectionRefusedError:
        SkibidiLoginFailedScreen.show()
        SkibidiQuitButton.show()
        print("server !boomed")

def StartLoading():
    print("fireeeeee Play Button Clicked")
    FireFadeIn()
    QTimer.singleShot(3000, ServerConnection)
    QTimer.singleShot(5000, FireFadeOut)

# Main
if __name__ == "__main__":
    SkibidiMainMenu.show()
    SkibidiPlayButton.show()
    SkibidiPlayButton.clicked.connect(StartLoading)
    ProjectSkibidi.exec()
    print(f"IsProd: {LogicVariables.LogicVersion.IsProd()}")
    print(f"IsDev: {LogicVariables.LogicVersion.IsDev()}")
    print(f"IsDeveloperBuild: {LogicVariables.LogicVersion.IsDeveloperBuild()}")
    print(f"IsStage: {LogicVariables.LogicVersion.IsStage()}")

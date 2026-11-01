

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick
import QtQuick.Controls
import ShopSmartWelcome

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Text {
        width: 173
        height: 16
        text: qsTr("You have chosen to Shop Smart!")
        font.pixelSize: 32
        anchors.verticalCenterOffset: 12
        anchors.horizontalCenterOffset: -108
        anchors.centerIn: parent
        font.family: Constants.font.family
    }

    Button {
        id: button
        x: 493
        y: 1061
        text: qsTr("Start/Sign In")
    }
}

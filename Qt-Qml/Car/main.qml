import QtQuick
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "qrc:/"

ApplicationWindow {
    id:root
    width: 640
    height: 480
    visible: true
    title: qsTr("Car Dashboard")
    color: "#122f5c"
    Image {
        anchors.fill: parent
        source: "qrc:/img/bg.jpg"
        width: root.width
        height: root.height
    }

    header: RowLayout{
        RowLayout{
            anchors.left: parent.left
            anchors.leftMargin:  10
            Label{
                text:"1/ 1"
                font.pointSize: 10
                color: "white"
            }
            Label{
                text: "|"
                font.pointSize: 30
                color: "white"
            }

            Label{
                text:"10:23"
                font.pointSize: 20
                color: "white"
            }
        }
        RowLayout{
            anchors.right: parent.right
            anchors.rightMargin: 10
            RoundButton{
                icon.source: "qrc:/img/icons8_music_32.png"
                radius: 5
            }
            RoundButton{
                icon.source: "qrc:/img/icons8_power_off_button_32.png"
                radius: 5
                onClicked: {
                    Qt.quit();
                }
            }
            RoundButton{
                icon.source: "qrc:/img/icons8_settings_32.png"
                radius: 5
                onClicked: {
                    myStack.push(settings)
                }
            }
        }
    }

    StackView{
        id: myStack
        initialItem:startingPage
        anchors.fill: parent
    }
    Component{
        id:startingPage
        StartingPage{}
    }
    Component{
        id:settings
        Settings{}
    }
    Component{
        id:radio
        Radio{}
    }
    Component{
        id:music
        Music{}
    }
    Component{
        id:camera
        Camera{}
    }

    footer: RowLayout{
        height: 50
        RoundButton{
            id:backing
            icon.source: "qrc:/img/icons8_back_32.png"
            anchors.left: parent.left
            anchors.margins: 10
            radius: 5
            onClicked: {
               myStack.pop()
            }
        }
        RoundButton{
            id:home
            icon.source: "qrc:/img/icons8_home_32.png"
            anchors.centerIn: parent
//            anchors.margins: 10
            radius: 5
            onClicked: {
               myStack.push(startingPage)
            }
        }
        RoundButton{
            icon.source: "qrc:/img/icons8_phone_32.png"
            anchors.right: parent.right
            anchors.margins: 10
            radius: 5
            onClicked: {
                console.log("clicked")
            }
        }
    }

}

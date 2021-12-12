import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.15
import "qrc:/"

Item {
    Material.theme: Material.Dark
    Component.onCompleted: {
        footer.visible= false
    }


    RowLayout{
        anchors.top: parent
        anchors.left: parent.left
        anchors.right: parent.right

        RoundButton{
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.margins: 5
            text: "<b>23</b>°C"
            font.pointSize: 10
        }
    }
    ColumnLayout{
        anchors.centerIn: parent
        RowLayout{
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_settings.ico"
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_bluetooth.ico"
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_itunes.ico"
                }
                onClicked: {
                    myStack.push(music)
                    header.visible=true
                    footer.visible=true
                }
            }

        }
        RowLayout{
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_camera_32.png"
                    width: sourceSize.width-10
                    height: sourceSize.height-10
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_car.ico"
                }
                onClicked: {
                    myStack.push(car)
                    header.visible = true
                    footer.visible = true
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_wi-fi.ico"
                }
            }

        }
        RowLayout{
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_fan_head_32.png"
                    width: sourceSize.width-10
                    height: sourceSize.height-10
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_near_me_16.png"
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_info.ico"
                }
                onClicked: {
                     myStack.push(about)
                }
            }

        }

    }

}

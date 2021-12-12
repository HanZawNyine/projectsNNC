import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    RowLayout{
        anchors.centerIn: parent
        spacing: 20
        RoundButton{
            icon.source: "qrc:/img/icons8_bluetooth_32.png"
            icon.width: 50
            icon.height: 50
            radius: 5
            onClicked: {
                console.log("clicked")
            }
        }
        RoundButton{
            icon.source: "qrc:/img/icons8_camera_32.png"
            icon.width: 50
            icon.height: 50
            radius: 5
            onClicked: {
                myStack.push(camera)
            }
        }
        RoundButton{
            icon.source: "qrc:/img/icons8_music_32.png"
            icon.width: 50
            icon.height: 50
            radius: 5
            onClicked: {
                myStack.push(music)
            }
        }
        RoundButton{
            icon.source: "qrc:/img/icons8_optical_disc_32.png"
            icon.width: 50
            icon.height: 50
            radius: 5
            onClicked: {
                console.log("clicked")
            }
        }
        RoundButton{
            icon.source: "qrc:/img/icons8_radio_32.png"
            icon.width: 50
            icon.height: 50
            radius: 5
            onClicked: {
                myStack.push(radio)
            }
        }
        RoundButton{
            icon.source: "qrc:/img/icons8_aux_cable_32.png"
            icon.width: 50
            icon.height: 50
            radius: 5
            onClicked: {
                console.log("clicked")
            }
        }
    }
}

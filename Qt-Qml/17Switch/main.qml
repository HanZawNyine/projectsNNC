import QtQuick
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    ColumnLayout{
        anchors.fill: parent
        Text {
            text: qsTr("Switch")
            Layout.fillWidth: true
            font.pointSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
        Repeater{
            model: ListModel{
                ListElement{myText:'Wi-Fi'}
                ListElement{myText:"Bluetooth"}
                ListElement{myText:"Other"}
            }
            RowLayout{
                Layout.fillWidth: true
                Layout.fillHeight: true
                Label {
                    Layout.fillWidth: true
                    text: myText + "=" + mySwitch.position
                    font.pointSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
                Switch{
                    id:mySwitch
                    Layout.fillWidth: true
                    text:myText
                }
            }


        }


    }

}

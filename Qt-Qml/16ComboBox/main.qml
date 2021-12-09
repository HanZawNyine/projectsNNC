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
            Layout.fillWidth: true
            horizontalAlignment: Text.AlignHCenter
            text: myCombo.currentText
            font.pointSize: 30
        }
        ComboBox{
            Layout.fillWidth: true
            id:myCombo
            font.pointSize: 20
            model: ListModel{
                ListElement{text:"Element 1"}
                ListElement{text:"Element 2"}
                ListElement{text:"Element 3"}
                ListElement{text:"Element 4"}
            }
        }
    }
}

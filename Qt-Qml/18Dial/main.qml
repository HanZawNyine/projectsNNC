import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    ColumnLayout{
        anchors.fill:parent
        ProgressBar{
            id:myProgress
            Layout.fillWidth: true
            height: 50
            from: myDial.from
            to:myDial.to
            value: myDial.value

        }
        Dial{
            anchors.centerIn: parent
//            Layout.fillHeight: true
//            Layout.fillWidth: true
            id:myDial
            from:0
            to:100
            value: 50
        }
    }
}

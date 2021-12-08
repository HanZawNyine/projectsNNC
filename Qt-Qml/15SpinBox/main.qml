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
        ProgressBar{
            id: myPro
            from: mySpin.from
            to:mySpin.to
            value: mySpin.value
            Layout.fillWidth: true
        }
        SpinBox{
            id:mySpin
            from: 0
            to:100
            stepSize: 20
            Layout.fillWidth: true
            font.pointSize: 30
        }
    }
}

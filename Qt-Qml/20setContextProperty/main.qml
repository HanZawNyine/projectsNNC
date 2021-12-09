import QtQuick.Controls 2.0

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    ListView{
        anchors.fill:parent
        model:myModel
        spacing:10
        delegate:Text{
            text:myText
            font.pointSize: 20
            font.bold: true
        }
    }
}

import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    ColumnLayout{
        anchors.fill:parent
        ScrollView{
            Layout.fillWidth: true
            Layout.fillHeight: true
            TextArea{
                id:area
                selectByKeyboard: true
                selectByMouse: true
                font.pointSize: 30
                wrapMode: TextArea.WrapAtWordBoundaryOrAnywhere
            }
        }
        Button{
            Layout.fillWidth: true
            text:"Clear"
            onClicked: {
                area.clear();
            }
        }
    }
}

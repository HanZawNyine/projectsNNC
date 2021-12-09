import QtQuick.Controls 2.15
import QtQuick 2.15
import "qrc:/"

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Alias")

    MainPage{
        id:mP
        anchors.fill: parent
        Button{
            text: "Change Color"
            anchors.centerIn: parent
            onClicked: {
                mP.section1.sect1Rect.color = "Red";
                mP.section2.sect2Rect.color = "Green";

            }
        }
    }
}

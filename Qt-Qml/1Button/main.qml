import QtQuick 2.6
import QtQuick.Controls 2.1

ApplicationWindow{
    id:root
    visible: true
    width: 600
    height: 600
    title:qsTr("1Button")

    Row{
        id:btnRow
        spacing: 2
        anchors.centerIn: parent
        Button{
            id:btn1
            text: 'btn 1'
            onClicked: {
                root.title = text
            }
        }
        Button{
            id:btn2
            text: 'btn 2'
            onClicked: {
                root.title = text
            }
        }
        Button{
            id:btn3
            text: 'btn 3'
            onClicked: {
                root.title = text
            }
        }
        Button{
            id:btn4
            text: 'exit'
            onClicked: {
                Qt.quit()
            }
        }
    }

}

import QtQuick
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("8 Tab Bar")

    footer: TabBar{
        id:bar
        font.pointSize: 30
        TabButton{
            text: 'one'
        }
        TabButton{
            text: 'two'
        }
        TabButton{
            text: 'three'
        }
    }
    StackLayout{
        anchors.fill: parent
        currentIndex: bar.currentIndex
        Item{
            Rectangle{
                color: 'red'
                anchors.fill: parent
                Text {
                    text: 'tab 1'
                    anchors.centerIn: parent
                    color: 'white'
                    font.pointSize: 30
                }
            }
        }
        Item{
            Rectangle{
                color: 'green'
                anchors.fill: parent
                Text {
                    text: 'tab 2'
                    anchors.centerIn: parent
                    color: 'white'
                    font.pointSize: 30
                }
            }
        }
        Item{
            Rectangle{
                color: 'blue'
                anchors.fill: parent
                Text {
                    text: 'tab 3'
                    anchors.centerIn: parent
                    color: 'white'
                    font.pointSize: 30
                }
            }
        }
    }
}

import QtQuick
import QtQuick.Controls

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    SwipeView{
        id:swipeview
        anchors.fill: parent
        currentIndex: 0

        Item{
            id:firstElement
            Rectangle{
                color: 'red'
                anchors.fill: parent
                Text {text: "Page 1";anchors.centerIn: parent;font.pointSize: 20;color: 'white'}

            }
        }
        Item{
            id:secondElement
            Rectangle{
                color: 'cyan'
                anchors.fill: parent
                Text {text: "Page 2";anchors.centerIn: parent;font.pointSize: 20;color: 'black'}

            }
        }
        Item{
            id:thirdElement
            Rectangle{
                color: 'blue'
                anchors.fill: parent
                Text {text: "Page 3";anchors.centerIn: parent;font.pointSize: 20;color: 'white'}
            }
        }
        Item{
            Rectangle{
                color: 'Yellow'
                anchors.fill: parent
                Text {text: "Page 4";anchors.centerIn: parent;font.pointSize: 20;color: 'black'}
            }
        }
    }
    PageIndicator{
        id:indicator
        count: swipeview.count
        currentIndex: swipeview.currentIndex
        anchors.bottom: swipeview.bottom
        anchors.horizontalCenter: parent.horizontalCenter
    }
}

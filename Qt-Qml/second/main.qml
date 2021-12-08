import QtQuick
import QtQuick.Window

Window {
    id:root
    width: 400
    height: 400
    visible: true
    title: qsTr("Digital Clock")
    color: 'white'

    Flickable{
        id:flick
        width: 400
        height: 400
        contentHeight: 1000
        contentWidth:  1000
        anchors.centerIn: parent

        PinchArea{
            anchors.fill: parent
            pinch.target: img
            pinch.maximumScale: 1.0
            pinch.minimumScale: 0.1
            pinch.dragAxis: Pinch.XAndYAxis


        }

        Image {
            id: img
            source: "qrc:/images/image-animated.gif"
            width: flick.contentWidth
            height: flick.contentHeight
        }
    }


}

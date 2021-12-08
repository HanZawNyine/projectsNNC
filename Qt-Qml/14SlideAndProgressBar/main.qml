import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    ColumnLayout{
        anchors.fill: parent
        ProgressBar{
            id:myProgress
            Layout.fillWidth:  true
            from: mySlide.from
            to:myslide.to
            value: myslide.value
        }
        Slider{
            Layout.fillWidth:  true
            id:myslide
            from: 0
            to:100
            stepSize: 5
            value: 50
        }
        Text {
            id: myTxt
            text: myslide.value
            Layout.fillWidth: true
            font.pointSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlighVCenter
        }
    }
}

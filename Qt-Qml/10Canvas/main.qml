import QtQuick
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("10 Canvas Paint")

    RowLayout{
        id:rowLayout
        anchors.horizontalCenter:parent.horizontalCenter
        z:canvas.z +1

        Button{
            text: 'clear'
            onClicked: {
                canvas.clear();
            }
        }
        Button{
            text: 'Exit'
            onClicked: {
                Qt.quit()
            }
        }
    }

    Canvas{
        id:canvas
        anchors.fill: parent

        property int lastX: 0
        property int lastY: 0

        function clear(){
            var ctx = getContext('2d');
            ctx.reset();
            canvas.requestPaint();
        }
        MouseArea{
            id:area
            anchors.fill: parent
            onPressed: {
                canvas.lastX = mouseX;
                canvas.lastY = mouseY;
            }
            onPositionChanged: {
                canvas.requestPaint()
            }
        }

        onPaint: {
            var ctx = getContext('2d');
            ctx.lineWidth = 5;
            ctx.beginPath();
            ctx.moveTo(lastX,lastY);
            lastX=area.mouseX
            lastY=area.mouseY
            ctx.lineTo(lastX,lastY);
            ctx.stroke();
        }
    }
}

import QtQuick
import QtQuick.Controls 2.12

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Component.onCompleted: {
        var colores =['red','green','blue','green']
        var a=1;
        for(var jx=0;jx<20;jx++){
            for(var ix=0;ix<colores.length;ix++){
                gV.model.append({
                                    myColor:colores[ix],
                                    myText:a++
                                })
            }
        }
    }

    GridView{
        id:gV
        anchors{
            left: parent.left
            right: parent.right
            top:parent.top
            bottom: parent.bottom
            leftMargin: 20
            rightMargin: 20
        }
        cellWidth: width/3
        cellHeight: height/3

        model: ListModel{}
        delegate: Rectangle{
            width: gV.cellWidth-10
            height: gV.cellHeight-10
            color: myColor
            Text {
                id: text
                text: myText
                font.pointSize: 20
                anchors.centerIn: parent
                color: 'white'
            }
        }
    }
}

import QtQuick
import QtQuick.Controls 2.12

ApplicationWindow {
    id:root
    width: 640
    height: 480
    visible: true
    title: qsTr("3ListView")


    Component.onCompleted: {
        var colores = ['red','green','blue']
        var jx=0
        for(var a=0;a<10;a++){
            if(jx == colores.length)
            {
                jx=0
            }

            myListView.model.append({delegateText:'Number '+a,colorr:colores[jx]});
            jx++
        }


    }

    ListView{
        id:myListView
        anchors.fill:parent
        model: ListModel{}

        spacing: 5
        delegate: Rectangle{
            color: colorr
            border.color: 'blue'
            border.width: 5
            width: root.width
            height: root.height/3
            Text {
                id: txt
                anchors.centerIn: parent
                font.pointSize: 20
                color: 'white'
                text: delegateText
            }
        }

    }
}

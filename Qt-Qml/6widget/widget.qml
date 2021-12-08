import QtQuick 2.0

Item {
    width: 600
    height: 600
    Component.onCompleted: {
        myListView.model.append({myColor:"red",myText:"red"})
        myListView.model.append({myColor:"green",myText:"green"})
        myListView.model.append({myColor:"blue",myText:"blue"})
        myListView.model.append({myColor:"cyan",myText:"cyan"})
        myListView.model.append({myColor:"yellow",myText:"yellow"})
        myListView.model.append({myColor:"orange",myText:"orange"})
        myListView.model.append({myColor:"gray",myText:"gray"})
        myListView.model.append({myColor:"red",myText:"red"})
        myListView.model.append({myColor:"green",myText:"green"})
        myListView.model.append({myColor:"blue",myText:"blue"})
        myListView.model.append({myColor:"cyan",myText:"cyan"})
        myListView.model.append({myColor:"yellow",myText:"yellow"})
        myListView.model.append({myColor:"orange",myText:"orange"})
        myListView.model.append({myColor:"gray",myText:"gray"})
    }

    ListView{
        id:myListView
        anchors.fill: parent
        model: ListModel{}
        spacing:5
        delegate: Rectangle{
            color: myColor
            width: parent.width
            height: 50
            Text {
                text:myText
                font.pointSize: 20
                anchors.centerIn: parent
                color: 'white'

            }
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    w.printTextColor(myText);
                }
            }
        }
    }

}

import QtQuick
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    id:root
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    Material.theme: Material.Dark


    ListView{
        anchors.centerIn: parent
        width: parent.width-10
        height: parent.height-10
        model: people
        spacing:10

        delegate:  RowLayout{
            spacing: 5
            width: parent.width


            Rectangle{
                width: root.width/6
                Text {
                    color:'white'
                    text: name
                    font.pointSize: 20
                    anchors.left: parent.left
                }
            }
            Rectangle{
                width: root.width/6
                Text {
                    color:'white'
                    text: age
                    font.pointSize: 20
                    anchors.left: parent.left
                }
            }

            Button{
                width: root.width/6

                text:'age + 1'
                onClicked: {
                    age = age+1;
                }
            }
            Button{
                width: root.width/6
                text:'age - 1'
                onClicked: {
                    age = age-1;
                }
            }
            TextField{
                id: nameFiled
                width: root.width/6
                placeholderText: 'Enter Name ...'

            }
            Button{
                text: 'OK'
                width: parent.width/6
                anchors{
                    right: parent.right
                    top:parent.top
                    bottom: parent.bottom
                }
                onClicked: {
                    name = nameFiled.text
                }
            }
        }
    }
}


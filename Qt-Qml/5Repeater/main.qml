import QtQuick
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    header: Rectangle{
        width: parent.width
        height: 50
        color: 'red'
        Label{
            anchors.centerIn: parent
            font.pointSize: 20
            id:myTitle
            color: 'white'
        }
    }

    ColumnLayout{
        anchors.fill:parent
        spacing:5
        Repeater{
            model: 5
            RowLayout{
                Layout.fillHeight:  true
                width:parent.width
                height:10
                spacing: 5
                Repeater{
                    model: ListModel{
                        ListElement{myText: 'button 1'}
                         ListElement{myText: 'button 2'}
                          ListElement{myText: 'button 3'}
                           ListElement{myText: 'button 4'}
                    }

                    Button{
                        Layout.fillWidth: true
                        text: myText
                        onClicked: {
                            myTitle.text = text
                        }

                    }
                }
            }
        }

    }
}

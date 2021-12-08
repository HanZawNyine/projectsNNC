import QtQuick
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Tool Bar")

    header: ToolBar{
        RowLayout{
            anchors.fill: parent

            ToolButton{
                text: "aa"
                onClicked: {
                        menu.open()
                }
            }
            Label{
                id:title
                text:'Tool Bar Application'
//                elide: Label.ElideLeft
               anchors.centerIn: parent
//               Layout.fillWidth: true
            }
            ToolButton{
                text: '<'

                anchors.right: parent.right
                onClicked: {
                    stack.pop();
                }
            }
        }
    }
    Menu{
        id:menu
        MenuItem{
            text: 'options 1'
            onClicked: {

                stack.push(pushEle)
            }
        }
        MenuItem{
            text: 'options 2'
            onClicked: {

                  stack.push(two)
            }
        }
        MenuItem{
            text: "options 3"
            onClicked: {

                  stack.push(three)
            }
        }
    }

    Component{
        id:pushEle
        Rectangle{
            anchors.fill: parent
            color: 'red'
        }
    }

    Component{
        id:two
        Rectangle{
            anchors.fill: parent
            color: 'green'
        }
    }
    Component{
        id:three
        Rectangle{
            anchors.fill: parent
            color: 'blue'
        }
    }

    StackView{
        id:stack
        anchors.fill: parent
    }
}

import QtQuick 2.0
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15
import "qrc:/"

Item {
    RowLayout{
        anchors.fill: parent
            ColumnLayout{
                width: iccc.width
                Layout.fillHeight: true
                anchors.left: parent.left
                RoundButton{
                    id:iccc
                    icon.source: "qrc:/img/icons8_star_32.png"
                    icon.width: 50
                    icon.height: 50
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }
                RoundButton{
                    icon.source: "qrc:/img/icons8_maintenance_32.png"
                    icon.width: 50
                    icon.height: 50
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }
                RoundButton{
                    icon.source: "qrc:/img/icons8_paint_palette_32.png"
                    icon.width: 50
                    icon.height: 50
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }
                RoundButton{
                    icon.source: "qrc:/img/icons8_sound_32.png"
                    icon.width: 50
                    icon.height: 50
                    radius: 5
                    onClicked: {
                        myStack.push(soundSettings)
                    }
                }
                RoundButton{
                    icon.source: "qrc:/img/icons8_optical_disc_32.png"
                    icon.width: 50
                    icon.height: 50
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }
                RoundButton{
                    icon.source: "qrc:/img/icons8_bluetooth_32.png"
                    icon.width: 50
                    icon.height: 50
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }

            }
            ColumnLayout{
                width: parent.width-iccc.width
                Layout.fillHeight: true
//                StackView{
//                    id: myStack
//                    initialItem:soundSettings
//                    anchors.fill: parent
//                }
            }

    }
}

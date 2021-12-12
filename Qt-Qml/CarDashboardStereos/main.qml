import QtQuick
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.15
import "qrc:/"

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    Material.theme: Material.Dark

    header: Rectangle{
//        visible: false
        height: 50
        color: "Gray"
        Button{
            anchors.left: parent.left
            Layout.fillHeight: true
            text: "HOME"
            onClicked: {
                myStack.push(mainPage)
            }
        }
        Button{
            anchors.right: parent.right
            Layout.fillHeight: true
            text: "BACK"
            onClicked: {
                 myStack.push(mainPage)
//                myStack.pop()
//                header.visible = true
//                footer.visible = false
            }
        }
        RowLayout{
            anchors.centerIn: parent
            Layout.fillWidth: true
            Image {
                source: "qrc:/img/icons8_fog_lamp.ico"
            }
            Image {
                source: "qrc:/img/icons8_car_door.ico"
            }

            Image {
                source: "qrc:/img/icons8_brake_warning.ico"
            }
            Image {
                source: "qrc:/img/icons8_brake_pedal.ico"
            }
            Image {
                source: "qrc:/img/icons8_fog_lamp.ico"
                transformOrigin: Item.Center
                rotation: 180
            }
        }
    }
    StackView{
        id: myStack
        initialItem:mainPage
        anchors.fill: parent
    }
    Component{
        id:mainPage
        MainPage{}
    }
    Component{
        id:car
        Car{}
    }
    Component{
        id: music
        Music{}
    }
    Component{
        id: about
        About{}
    }

    footer: Rectangle{
        visible: false
        color: "Gray"
        height: 65
        //        ScrollView{
        //            anchors.fill: parent
        RowLayout{
            anchors.centerIn: parent

            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_settings.ico"
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_bluetooth.ico"
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_itunes.ico"
                }
                onClicked: {
                    myStack.push(music)
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_camera_32.png"
                    width: sourceSize.width-10
                    height: sourceSize.height-10
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_car.ico"
                }
                onClicked: {
                    myStack.push(car)
                    header.visible = true
                    footer.visible = true
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_wi-fi.ico"
                }
            }

            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_fan_head_32.png"
                    width: sourceSize.width-10
                    height: sourceSize.height-10
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_near_me_16.png"
                }
            }
            Button{
                Image {
                    anchors.centerIn: parent
                    source: "qrc:/img/icons8_info.ico"
                }
                onClicked: {
                     myStack.push(about)
                }
            }
        }
        //        }
    }


}

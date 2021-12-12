import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.15


Item {

    ColumnLayout{
        anchors.fill: parent
        RowLayout{
            Rectangle{
                anchors.fill: parent
                color: "red"
                Image {
                    source: "qrc:/img/musicc.jpg"
                    width:parent.width
                    height: parent.height+30
                }

            }
        }
        Slider{
            Material.theme: Material.Light
            anchors.left: parent.left
            anchors.right: parent.right
            from: 100
            to:0
            value: 50
        }

        RowLayout{
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.margins: 10
            RowLayout{
                RoundButton{
                    icon.source: "qrc:/img/icons8_sound_32.png"
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }
                Slider{
                    width: 50
                    from: 0
                    to:20
                    value: 15
                }
            }
            RowLayout{
                anchors.centerIn: parent
                RoundButton{
                    icon.source: "qrc:/img/icons8_rewind_32.png"
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }
                RoundButton{
                    icon.source: "qrc:/img/icons8_play_32.png"

                    radius: 5
                    onClicked: {

                        if(icon.source == "qrc:/img/icons8_play_32.png"){
                            icon.source = "qrc:/img/icons8_pause_16.png"
                        }else{
                            icon.source = "qrc:/img/icons8_play_32.png"
                        }
                    }
                }


                RoundButton{
                    icon.source: "qrc:/img/icons8_fast_forward_32.png"
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }

                }
            }

            RowLayout{
                anchors.right: parent.right
                RoundButton{
                    icon.source: "qrc:/img/icons8_shuffle_32.png"
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }
                RoundButton{
                    icon.source: "qrc:/img/icons8_playlist_32.png"
                    radius: 5
                    onClicked: {
                        console.log("clicked")
                    }
                }
            }


        }

    }
}


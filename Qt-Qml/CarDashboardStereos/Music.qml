import QtQuick 2.9
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.3
import QtQuick.Window 2.0

Item {
    id: window


    ColumnLayout{
        anchors.fill: parent
        Label{
            anchors.top: parent.top
            text: "Poster Sexy Beauty Girl"
            Layout.fillWidth: true
            horizontalAlignment: Text.AlignHCenter
            color: 'white'
            font.pointSize: 20
        }

        Rectangle{
            anchors.centerIn: parent
            color: 'gray'
            width: parent.width/2
            height: parent.height/2
            radius: 50
            Image{
                anchors.fill: parent
                source: "https://img.pixers.pics/pho_wat(s3:700/FO/55/95/41/63/700_FO55954163_e21820f4ad17391fa7fef2c7b3ac63df.jpg,700,684,cms:2018/10/5bd1b6b8d04b8_220x50-watermark.png,over,480,634,jpg)/posters-sexy-beauty-girl-with-levres-et-les-ongles-rouges-provocateur-maquillage.jpg.jpg"
            }
        }
        Slider{
            id:progreess
            Layout.fillWidth: true
            anchors.bottom: player.top
            anchors.bottomMargin: 5
            value: 50
            from: 0
            to:100
        }
        RowLayout{
            anchors.bottomMargin: 5
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            spacing: 5


            RowLayout{
                anchors.left: parent.left
                width: 50
                RoundButton{
                    icon.source: "qrc:/img/icons8_sound.ico"
                }
                Slider{
                    from: 0
                    to:100
                    value: 50
                    stepSize: 5
                }
            }


            RowLayout{
                id:player
                anchors.horizontalCenter: parent.horizontalCenter
                RoundButton {
                    icon.source: "qrc:/img/icons8_fast_forward.ico"
                    transformOrigin: Item.Center
                    rotation: 180
                }
                RoundButton {
                    icon.source: "qrc:/img/icons8_play.ico"
                }
                RoundButton {
                    icon.source: "qrc:/img/icons8_fast_forward.ico"

                }
            }
            RoundButton {
                id:playlist
                icon.source: "qrc:/img/icons8_playlist.ico"
                anchors.right: parent.right
            }
            RoundButton {
                  anchors.right: playlist.left
                icon.source: "qrc:/img/icons8_shuffle.ico"
            }


        }


    }



}


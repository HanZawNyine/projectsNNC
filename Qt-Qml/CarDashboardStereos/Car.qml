import QtQuick 2.0
import QtQuick.Controls.Material 2.15
import QtQuick.Layouts 1.15

Item {
    Material.theme: Material.Dark

    ColumnLayout{
        anchors.centerIn: parent
        spacing: 10
        RowLayout{
            spacing: 10
            ColumnLayout{

                    Image {
                        source: "qrc:/img/icons8_wheel.ico"
                    }
                    Label{
                        text: "30 FPS"
                        font.pointSize: 10
                    }
                    Label{
                        text: "12 LB"
                    }
            }
            ColumnLayout{

                    Image {
                        source: "qrc:/img/icons8_wheel.ico"
                    }
                    Label{
                        text: "30 FPS"
                    }
                    Label{
                        text: "12 LB"
                    }
            }
            ColumnLayout{
                    Image {
                        source: "qrc:/img/icons8_wheel.ico"
                    }
                    Label{
                        text: "30 FPS"
                    }
                    Label{
                        text: "12 LB"
                    }
            }
            ColumnLayout{
                    Image {
                        source: "qrc:/img/icons8_wheel.ico"
                    }
                    Label{
                        text: "30 FPS"
                    }
                    Label{
                        text: "12 LB"
                    }
            }
        }
        RowLayout{
            ColumnLayout{
                Image{
                    source: "qrc:/img/icons8_charging_station.ico"
                }
                Label{
                    text: "13%"
                }
            }
        }
    }




}

import QtQuick
import QtQuick.Controls 2.12

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Button{
        id:openMenu
        text: 'Open Menu'
        font.pointSize: 20
        onClicked: {
            menu.open()
        }
    }
    Menu{
        id:menu
        y:openMenu.height
        MenuItem{
            text:'options 1'
            onClicked: {
                openMenu.text = text
            }
        }
        MenuItem{
            text:'options 2'
            onClicked: {
                openMenu.text = text
            }
        }
        MenuItem{
            text:'options 3'
            onClicked: {
                openMenu.text = text
            }
        }
        MenuItem{
            text:'options 4'
            onClicked: {
                openMenu.text = text
            }
        }
        MenuItem{
            text:'exit'
            onClicked: {
                Qt.quit()
            }
        }
    }
}

import QtQuick
import QtQuick.Window
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12

Window {
    id:window
    width: 600
    height: 600
    visible: true
    title: qsTr("Hello World")
//    color: '#000040'

    GridLayout {
        anchors.fill: parent
        anchors.margins: 5

        columns: 3

        // auto positioning based on flow: forth button overflows into second row//--> hide
        Button {
            Layout.fillWidth: true

            text: "One"
        }
        Button {
            Layout.fillWidth: true

            text: "Two"
        }

        Button {
            Layout.fillWidth: true

            text: "Three"
        }
        Button {
            Layout.fillWidth: true

            text: "Four"
        }

        // specific placement
        Button {
            Layout.row: 1
            Layout.column: 2
            Layout.fillWidth: true

            text: "Five"
        }

        // overflow into next row still works
        Label {
            text: "File"
        }

        // spanning two columns, same row
        TextField {
            Layout.columnSpan: 2
            Layout.fillWidth: true

            placeholderText: "Enter filename"
        }//<-- hide

        Label {
            text: "Comment"
        }

        TextArea {
            Layout.columnSpan: 2
            Layout.rowSpan: 4
            Layout.fillWidth: true
            Layout.fillHeight: true
        }

        Button  {
            Layout.row: 6
            Layout.column: 0

            text: "Send"
        }
    }
    //<-- slide
}



import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts
import QtQuick.Window

ApplicationWindow {
    id: window
    width: 400
    height: 500
    visible: true
     Material.theme: Material.Dark

    ListView {
        id: alarmListView
        anchors.fill: parent
        model: AlarmModel {}
        delegate: AlarmDelegate {}
    }

    RoundButton {
        id: addAlarmButton
        text: "+"
        anchors.bottom: alarmListView.bottom
        anchors.bottomMargin: 8
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: alarmDialog.open()
    }

    AlarmDialoag {
        id: alarmDialog
        x: Math.round((parent.width - width) / 2)
        y: Math.round((parent.height - height) / 2)
        alarmModel: alarmListView.model
    }
}

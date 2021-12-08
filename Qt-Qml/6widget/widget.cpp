#include "widget.h"
#include "ui_widget.h"
#include <QQmlContext>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
    QQuickWindow::setGraphicsApi(QSGRendererInterface::OpenGL);
    ui->quickWidget->rootContext()->setContextProperty("w",this);
    ui->quickWidget->setSource(QUrl(QStringLiteral("qrc:/widget.qml")));
}

Widget::~Widget()
{
    delete ui;
}

void Widget::printTextColor(const QString &textColor)
{
    ui->lineEdit->setText(textColor);
}

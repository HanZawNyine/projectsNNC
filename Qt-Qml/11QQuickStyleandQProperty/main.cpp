#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QQuickStyle>
#include "myperson.h"



int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QQuickStyle::setStyle("Material");
    QQmlApplicationEngine engine;

    QObjectList people;
    people.append(new MyPerson("Han",20));
    people.append(new MyPerson("Zaw",20));
    people.append(new MyPerson("Nyine",20));
    people.append(new MyPerson("Han",20));
    people.append(new MyPerson("Zaw",20));
    people.append(new MyPerson("Nyine",20));
    people.append(new MyPerson("Han",20));
    people.append(new MyPerson("Zaw",20));
    people.append(new MyPerson("Nyine",20));


    engine.rootContext()->setContextProperty("people",QVariant::fromValue(people));


    const QUrl url(u"qrc:/11QQuickStyleandQProperty/main.qml"_qs);
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                     &app, [url](QObject *obj, const QUrl &objUrl) {
        if (!obj && url == objUrl)
            QCoreApplication::exit(-1);
    }, Qt::QueuedConnection);
    engine.load(url);

    return app.exec();
}

#ifndef MYPERSON_H
#define MYPERSON_H

#include <QObject>

class MyPerson : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString name READ name WRITE set_Name NOTIFY name_changed);
    Q_PROPERTY(int age READ age WRITE set_age NOTIFY age_changed);
public:
    explicit MyPerson(QObject *parent = nullptr);

    MyPerson(const QString &name,int age, QObject *parent=nullptr);

    QString name() const{
        return m_name;
    }
    int age() const{
        return m_age;
    }
    void set_name(const QString &name);
    void set_age(int age);

signals:
        void name_changed();
        void age_changed();

private:
    QString     m_name;
    int m_age;

};

#endif // MYPERSON_H

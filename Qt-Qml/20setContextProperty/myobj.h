#ifndef MYOBJ_H
#define MYOBJ_H
#include<QObject>

class myObj :public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString text READ text WRITE setText NOTIFY textChanged)
public:
    myObj(const QString &text="");

    void setText(const QString &text){
        m_Text= text;
    }
    QString text() const{
        return m_Text;
    }
};
signals:
    void textChanged();
private:
    QString m_Text;
#endif // MYOBJ_H

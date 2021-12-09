#ifndef MYMODEL_H
#define MYMODEL_H

#include <QObject>


class myModel
{
public:
    myModel();

    QObjectList &refModel(){
        return m_model;
    }
};

private:
    QObjectList m_model;
#endif // MYMODEL_H

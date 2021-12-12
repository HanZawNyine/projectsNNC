#include "myimagesaver.h"
#include <QFile>
#include <QImage>
#include <QDebug>
#include <QBuffer>
#include <QStandardPaths>
#include <QQuickItemGrabResult>

MyImageSaver::MyImageSaver(QObject *parent):QObject{parent}
{

}

bool MyImageSaver::savePicture(const QString &id, QObject *objectImage)
{
    const int nImages = mImages.size();
    for(int ix=0;ix<nImages;++ix){
        if(mImages.at(ix).id() == id){
            return false;
        }

    }
    QQuickItemGrabResult *item= static_cast<QQuickItemGrabResult *>(objectImage);
    QByteArray imageData;
    QBuffer buffer(&imageData);

    if(item->image().save(&buffer,"PNG")){
        MyImage img;
        img.setData(imageData);
        img.setId(id);
        mImages.append(img);
        return true;
    }
    return false;
}

bool MyImageSaver::writePictures(){
    const int nImages = mImages.size();
    for (int ix=0;ix<nImages; ++ix){
        QFile file;
        QString filename= mImages.at(ix).id().split("/").last()+".png";
        QString directory = QStandardPaths::writableLocation(QStandardPaths::DesktopLocation);
        QString path = directory+"/"+filename;
        file.setFileName(path);
        if(file.open(QIODevice::WriteOnly)){
            if(file.write(mImages.at(ix).data()) >0){
                file.flush();
                file.close();
            }else{
                qDebug() <<"Error"<<file.errorString();
                return false;
            }
        }else{
            qDebug() <<"Error"<<file.errorString();
            return false;
        }

    }
    return true;
}

/****************************************************************************
** Resource object code
**
** Created by: The Resource Compiler for Qt version 6.2.2
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

static const unsigned char qt_resource_data[] = {
  // D:/projectsNNC/Qt-Qml/dfgfd/CMakeLists.txt
  0x0,0x0,0x0,0x6b,
  0x66,
  0x69,0x6e,0x64,0x5f,0x70,0x61,0x63,0x6b,0x61,0x67,0x65,0x28,0x51,0x74,0x36,0x20,
  0x43,0x4f,0x4d,0x50,0x4f,0x4e,0x45,0x4e,0x54,0x53,0x20,0x4d,0x75,0x6c,0x74,0x69,
  0x6d,0x65,0x64,0x69,0x61,0x20,0x52,0x45,0x51,0x55,0x49,0x52,0x45,0x44,0x29,0xd,
  0xa,0x74,0x61,0x72,0x67,0x65,0x74,0x5f,0x6c,0x69,0x6e,0x6b,0x5f,0x6c,0x69,0x62,
  0x72,0x61,0x72,0x69,0x65,0x73,0x28,0x6d,0x79,0x5f,0x70,0x72,0x6f,0x6a,0x65,0x63,
  0x74,0x20,0x50,0x55,0x42,0x4c,0x49,0x43,0x20,0x51,0x74,0x3a,0x3a,0x4d,0x75,0x6c,
  0x74,0x69,0x6d,0x65,0x64,0x69,0x61,0x29,0xd,0xa,
  
};

static const unsigned char qt_resource_name[] = {
  // CMakeLists.txt
  0x0,0xe,
  0xd,0xb9,0xf,0xf4,
  0x0,0x43,
  0x0,0x4d,0x0,0x61,0x0,0x6b,0x0,0x65,0x0,0x4c,0x0,0x69,0x0,0x73,0x0,0x74,0x0,0x73,0x0,0x2e,0x0,0x74,0x0,0x78,0x0,0x74,
  
};

static const unsigned char qt_resource_struct[] = {
  // :
  0x0,0x0,0x0,0x0,0x0,0x2,0x0,0x0,0x0,0x1,0x0,0x0,0x0,0x1,
0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
  // :/CMakeLists.txt
  0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x1,0x0,0x0,0x0,0x0,
0x0,0x0,0x1,0x7d,0xa9,0x85,0x72,0xa5,

};

#ifdef QT_NAMESPACE
#  define QT_RCC_PREPEND_NAMESPACE(name) ::QT_NAMESPACE::name
#  define QT_RCC_MANGLE_NAMESPACE0(x) x
#  define QT_RCC_MANGLE_NAMESPACE1(a, b) a##_##b
#  define QT_RCC_MANGLE_NAMESPACE2(a, b) QT_RCC_MANGLE_NAMESPACE1(a,b)
#  define QT_RCC_MANGLE_NAMESPACE(name) QT_RCC_MANGLE_NAMESPACE2( \
        QT_RCC_MANGLE_NAMESPACE0(name), QT_RCC_MANGLE_NAMESPACE0(QT_NAMESPACE))
#else
#   define QT_RCC_PREPEND_NAMESPACE(name) name
#   define QT_RCC_MANGLE_NAMESPACE(name) name
#endif

#ifdef QT_NAMESPACE
namespace QT_NAMESPACE {
#endif

bool qRegisterResourceData(int, const unsigned char *, const unsigned char *, const unsigned char *);
bool qUnregisterResourceData(int, const unsigned char *, const unsigned char *, const unsigned char *);

#ifdef QT_NAMESPACE
}
#endif

int QT_RCC_MANGLE_NAMESPACE(qInitResources_res)();
int QT_RCC_MANGLE_NAMESPACE(qInitResources_res)()
{
    int version = 3;
    QT_RCC_PREPEND_NAMESPACE(qRegisterResourceData)
        (version, qt_resource_struct, qt_resource_name, qt_resource_data);
    return 1;
}

int QT_RCC_MANGLE_NAMESPACE(qCleanupResources_res)();
int QT_RCC_MANGLE_NAMESPACE(qCleanupResources_res)()
{
    int version = 3;
    QT_RCC_PREPEND_NAMESPACE(qUnregisterResourceData)
       (version, qt_resource_struct, qt_resource_name, qt_resource_data);
    return 1;
}

namespace {
   struct initializer {
       initializer() { QT_RCC_MANGLE_NAMESPACE(qInitResources_res)(); }
       ~initializer() { QT_RCC_MANGLE_NAMESPACE(qCleanupResources_res)(); }
   } dummy;
}
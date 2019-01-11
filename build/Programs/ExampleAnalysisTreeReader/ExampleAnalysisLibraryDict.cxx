// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME ExampleAnalysisLibraryDict

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Since CINT ignores the std namespace, we need to do so in this file.
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.hh"

// Header files passed via #pragma extra_include

namespace ROOT {
   static void *new_ExampleAnalysisTreeReader(void *p = 0);
   static void *newArray_ExampleAnalysisTreeReader(Long_t size, void *p);
   static void delete_ExampleAnalysisTreeReader(void *p);
   static void deleteArray_ExampleAnalysisTreeReader(void *p);
   static void destruct_ExampleAnalysisTreeReader(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ExampleAnalysisTreeReader*)
   {
      ::ExampleAnalysisTreeReader *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ExampleAnalysisTreeReader >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ExampleAnalysisTreeReader", ::ExampleAnalysisTreeReader::Class_Version(), "", 17,
                  typeid(::ExampleAnalysisTreeReader), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::ExampleAnalysisTreeReader::Dictionary, isa_proxy, 4,
                  sizeof(::ExampleAnalysisTreeReader) );
      instance.SetNew(&new_ExampleAnalysisTreeReader);
      instance.SetNewArray(&newArray_ExampleAnalysisTreeReader);
      instance.SetDelete(&delete_ExampleAnalysisTreeReader);
      instance.SetDeleteArray(&deleteArray_ExampleAnalysisTreeReader);
      instance.SetDestructor(&destruct_ExampleAnalysisTreeReader);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ExampleAnalysisTreeReader*)
   {
      return GenerateInitInstanceLocal((::ExampleAnalysisTreeReader*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ExampleAnalysisTreeReader*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

//______________________________________________________________________________
atomic_TClass_ptr ExampleAnalysisTreeReader::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *ExampleAnalysisTreeReader::Class_Name()
{
   return "ExampleAnalysisTreeReader";
}

//______________________________________________________________________________
const char *ExampleAnalysisTreeReader::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ExampleAnalysisTreeReader*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int ExampleAnalysisTreeReader::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ExampleAnalysisTreeReader*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *ExampleAnalysisTreeReader::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ExampleAnalysisTreeReader*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *ExampleAnalysisTreeReader::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ExampleAnalysisTreeReader*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
void ExampleAnalysisTreeReader::Streamer(TBuffer &R__b)
{
   // Stream an object of class ExampleAnalysisTreeReader.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ExampleAnalysisTreeReader::Class(),this);
   } else {
      R__b.WriteClassBuffer(ExampleAnalysisTreeReader::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ExampleAnalysisTreeReader(void *p) {
      return  p ? new(p) ::ExampleAnalysisTreeReader : new ::ExampleAnalysisTreeReader;
   }
   static void *newArray_ExampleAnalysisTreeReader(Long_t nElements, void *p) {
      return p ? new(p) ::ExampleAnalysisTreeReader[nElements] : new ::ExampleAnalysisTreeReader[nElements];
   }
   // Wrapper around operator delete
   static void delete_ExampleAnalysisTreeReader(void *p) {
      delete ((::ExampleAnalysisTreeReader*)p);
   }
   static void deleteArray_ExampleAnalysisTreeReader(void *p) {
      delete [] ((::ExampleAnalysisTreeReader*)p);
   }
   static void destruct_ExampleAnalysisTreeReader(void *p) {
      typedef ::ExampleAnalysisTreeReader current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ExampleAnalysisTreeReader

namespace {
  void TriggerDictionaryInitialization_ExampleAnalysisLibraryDict_Impl() {
    static const char* headers[] = {
"/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.hh",
0
    };
    static const char* includePaths[] = {
"/homea/vsk10/vsk1056/Software/ACsoft",
"/homea/vsk10/vsk1056/Software/ACsoft/acceptance",
"/homea/vsk10/vsk1056/Software/ACsoft/acqt",
"/homea/vsk10/vsk1056/Software/ACsoft/analysis",
"/homea/vsk10/vsk1056/Software/ACsoft/backtracing",
"/homea/vsk10/vsk1056/Software/ACsoft/binning",
"/homea/vsk10/vsk1056/Software/ACsoft/calibration",
"/homea/vsk10/vsk1056/Software/ACsoft/compat",
"/homea/vsk10/vsk1056/Software/ACsoft/compat/QtCore",
"/homea/vsk10/vsk1056/Software/ACsoft/core",
"/homea/vsk10/vsk1056/Software/ACsoft/math",
"/homea/vsk10/vsk1056/Software/ACsoft/mva",
"/homea/vsk10/vsk1056/Software/ACsoft/mva/implementations",
"/homea/vsk10/vsk1056/Software/ACsoft/cuts",
"/homea/vsk10/vsk1056/Software/ACsoft/cuts/attachments",
"/homea/vsk10/vsk1056/Software/ACsoft/detector",
"/homea/vsk10/vsk1056/Software/ACsoft/io",
"/homea/vsk10/vsk1056/Software/ACsoft/modelling",
"/homea/vsk10/vsk1056/Software/ACsoft/producer",
"/homea/vsk10/vsk1056/Software/ACsoft/systemx",
"/homea/vsk10/vsk1056/Software/ACsoft/trdcalibration",
"/homea/vsk10/vsk1056/Software/ACsoft/unfolding",
"/homea/vsk10/vsk1056/Software/ACsoft/utilities",
"/homea/vsk10/vsk1056/Software/ACsoft/rti",
"/homea/vsk10/vsk1056/Software/ACsoft/build/streamers",
"/homea/vsk10/vsk1056/Software/ACsoft/build/adl",
"/homea/vsk10/vsk1056/Software/ACsoft/build/adl/AC",
"/homea/vsk10/vsk1056/Software/ACsoft/build/compat",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtDesigner",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtDeclarative",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtScriptTools",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtDesigner",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtXml",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtSql",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtOpenGL",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtMultimedia",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtNetwork",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtHelp",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtUiTools",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtTest",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtScript",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtSvg",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/Qt3Support",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtGui",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtCore",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/mkspecs/default",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include",
"/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtCore",
"/work/vsk10/vsk1002/public/software/root/6.08.02/x86_64-slc6-icc17_gcc63-opt/include",
"/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Libraries/ExampleAnalysisTree",
"/work/vsk10/vsk1002/public/software/root/6.08.02/x86_64-slc6-icc17_gcc63-opt/include",
"/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "ExampleAnalysisLibraryDict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
class __attribute__((annotate("$clingAutoload$/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.hh")))  ExampleAnalysisTreeReader;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "ExampleAnalysisLibraryDict dictionary payload"
#ifdef NDEBUG
  #undef NDEBUG
#endif

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif
#ifndef QT_NO_DEBUG
  #define QT_NO_DEBUG 1
#endif
#ifndef _GLIBCXX_USE_CXX11_ABI
  #define _GLIBCXX_USE_CXX11_ABI 1
#endif
#ifndef HAVE_NEWER_TYPE_TRAITS
  #define HAVE_NEWER_TYPE_TRAITS 1
#endif
#ifndef ENABLE_MPI
  #define ENABLE_MPI 1
#endif
#ifndef QT_NO_DEBUG
  #define QT_NO_DEBUG 1
#endif
#ifndef QT_CORE_LIB
  #define QT_CORE_LIB 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.hh"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"ExampleAnalysisTreeReader", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("ExampleAnalysisLibraryDict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_ExampleAnalysisLibraryDict_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_ExampleAnalysisLibraryDict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_ExampleAnalysisLibraryDict() {
  TriggerDictionaryInitialization_ExampleAnalysisLibraryDict_Impl();
}

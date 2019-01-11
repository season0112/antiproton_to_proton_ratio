#include "ExampleAnalysisTree.hh"

// ACsoft includes
#include "AnalysisEvent.hh"
#include "ConfigHandler.hh"
#include "EventFactory.hh"
#include "FileManager.hh"
#include "Selector.hh"
#include "SelectionParser.hh"
#include "TreeWriter.hh"
#include "Environment.hh"
#include "ObjectManager.hh"
#include "McSpectrumScaler.hh"
#include "TemplateFitter.hh"
#include <iostream>
#include <cassert>
#include <TH2.h>
#include <TFile.h>
#include <TMath.h>
#include "TemplateFitter2D.hh"
#include <vector>
#include <TCanvas.h>
#include <sstream>
#include <string>

using namespace std;

#define INFO_OUT_TAG "Templatefitter"
#include "debugging.hh"

int main(int argc, char** argv) {
/*
   int   i;   
   for (i = 0; i<argc; i++)   
       std::cout<<argv[i]<<std::endl;   
       std::cin>>i; 
*/

TFile *f = new TFile("histo.root");
TH2D *template_correct = (TH2D*)f->Get("template_correct");
TH2D *template_confused = (TH2D*)f->Get("template_confused");
TH2D *template_electron = (TH2D*)f->Get("template_electron");
TH2D *data = (TH2D*)f->Get(argv[1]); 

Utilities::TemplateFitter2D templateFitter(0);
templateFitter.AddTemplateHistogram(template_correct);
templateFitter.AddTemplateHistogram(template_confused);
templateFitter.AddTemplateHistogram(template_electron);
templateFitter.SetDataHistogram(data);

templateFitter.SetStartValue(0, 322);
templateFitter.SetStartValue(1, 2500);
templateFitter.SetStartValue(2, 1500);
templateFitter.Fit(0);

 // store those
vector<double> result, ResultError;
assert(result.empty());
assert(ResultError.empty());
result.assign(templateFitter.GetAbsoluteResult().begin(), templateFitter.GetAbsoluteResult().end());
ResultError.assign(templateFitter.GetAbsoluteResultError().begin(), templateFitter.GetAbsoluteResultError().end());
double Chi2 = templateFitter.Chi2(); 
int NDF = templateFitter.NDF();
 
cout << result << endl;
cout << ResultError << endl;
cout << Chi2 << endl;
cout << NDF << endl;



TCanvas * c1 = templateFitter.CreateResultDrawing("Fit_Result",800,600);
c1->SaveAs("Fit_Result.png");
TCanvas * c2 = templateFitter.CreateResultDrawingXprojection("CCprojection",800,600);
c2->SaveAs("CCprojection.png");
TCanvas * c3 = templateFitter.CreateResultDrawingYprojection("TRDprojection",800,600);
c3->SaveAs("TRDprojection.png");








/*
//Createresultdrawing and prejection
char *s= *argv[1];
string a= "FitResult";
string b= "CCprojection";
string c= "TRDprojection";
ostringstream oss;
oss << a << *s << endl;
ostringstream oss2;
oss2 << b << *s << endl;
ostringstream oss3;
oss3 << c << *s << endl;


s = argv[1];
TCanvas * c1 = templateFitter.CreateResultDrawing("Fit_Result",800,600);
c1->SaveAs(oss.str());
TCanvas * c2 = templateFitter.CreateResultDrawingXprojection("CCprojection",800,600);
c2->SaveAs(oss2.str());
TCanvas * c3 = templateFitter.CreateResultDrawingYprojection("TRDprojection",800,600);
c3->SaveAs(oss3.str());
*/






 
  return EXIT_SUCCESS;
}

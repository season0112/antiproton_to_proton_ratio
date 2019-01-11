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

using namespace std;

#define INFO_OUT_TAG "1Dtemplate"
#include "debugging.hh"

int main(int argc, char** argv) {
/*
   int   i;   
   for (i = 0; i<argc; i++)   
       std::cout<<argv[i]<<std::endl;   
       std::cin>>i; 
*/

TFile *f = new TFile("histo.root");
TH1D *template_correct = (TH1D*)f->Get("template_correct");
TH1D *template_confused = (TH1D*)f->Get("template_confused");
TH2D *template_electron = (TH2D*)f->Get("template_electron");
TH1D *data = (TH1D*)f->Get(argv[1]); 

Utilities::TemplateFitter templateFitter(0);
templateFitter.AddTemplateHistogram(template_correct);
templateFitter.AddTemplateHistogram(template_confused);
templateFitter.AddTemplateHistogram(template_electron);
templateFitter.SetDataHistogram(data);

templateFitter.SetStartValue(0, 100);
templateFitter.SetStartValue(1, 2500);
templateFitter.SetStartValue(2, 0);
templateFitter.Fit(1);

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

//Createresultdrawing and prejection
TCanvas * c1 = templateFitter.CreateResultDrawing("Fit_Result",800,600);
c1->SaveAs("FitResult.png");
 
  return EXIT_SUCCESS;
}


#include "Statistics.hh"
#include "TemplateFitter2D.hh"

#include <TCanvas.h>
#include <TH1.h>
#include <TH2.h>
#include <TLegend.h>
#include <TStyle.h>

#include <cassert>
#include <cmath>

#include <QString>

#define INFO_OUT_TAG "TemplateFitter2D"
#include "debugging.hh"

namespace Utilities {

TemplateFitter2D::TemplateFitter2D(int printlevel)
  : TemplateFitter(printlevel) {
}

TemplateFitter2D::~TemplateFitter2D() {
}

void TemplateFitter2D::AddTemplateHistogram(const TH1* hist, double start) {
  assert(hist->GetDimension() == 2);
  fInputTemplates.push_back(hist);
  fStartValues.push_back(start);
  fFixParameter.push_back(false);
}

TCanvas* TemplateFitter2D::CreateResultDrawing(std::string canvasname, int width, int height) const {

  if (!fHasBeenFit) {
    WARN_OUT << "No fit was done!" << std::endl;
    return 0;
  }

  gStyle->SetOptStat(0);
  TCanvas* graphicsOutput = new TCanvas(canvasname.c_str(), canvasname.c_str(), width, height);
  graphicsOutput->cd();
  graphicsOutput->Divide(2, 2);


  graphicsOutput->cd(1); //data
  gPad->SetLogz();
//  gPad->SetGrid();

  TH1* dataCopy = fInputData->DrawCopy("COLZ");
  dataCopy->SetStats(0); // disable statistic boxes in template canvas
  dataCopy->GetXaxis()->SetTitle("#bf{Charge Confusion Estimator}");
  dataCopy->GetYaxis()->SetTitle("#bf{TrdLikelihood}");

  graphicsOutput->cd(2); //fit result
  gPad->SetLogz();
//  gPad->SetGrid();
  fFitResult->SetStats(0);
  TH1* fitResultCopy = fFitResult->DrawCopy("COLZ");
  fitResultCopy->GetXaxis()->SetTitle("#bf{Charge Confusion Estimator}");
  fitResultCopy->GetYaxis()->SetTitle("#bf{TrdLikelihood}");

  graphicsOutput->cd(3); //fit-data difference
  gPad->SetLogz();
//  gPad->SetGrid();
  TH2F* differenceCopy = (TH2F*) fInputData->Clone("difference_hist");
  differenceCopy->SetTitle("(data-fit)**2/sigma_data**2");
  differenceCopy->GetXaxis()->SetTitle("#bf{Charge Confusion Estimator}");
  differenceCopy->GetYaxis()->SetTitle("#bf{TrdLikelihood}");
  //---> This assumes the template has no error!!
  for (int k = 1; k <= differenceCopy->GetXaxis()->GetNbins(); k++)
    for (int l = 1; l <= differenceCopy->GetYaxis()->GetNbins(); l++) {
      float dat = differenceCopy->GetBinContent(k, l);
      float fitres = fFitResult->GetBinContent(k, l);
      double upE, lowE;
      PoissonUncertainty((int) dat, lowE, upE);
      float error = (dat > fitres ? lowE : upE);

      float reldiffabs = (dat + fitres > 0 ? std::pow((dat - fitres), 2) / std::pow(error, 2) : 0);
      differenceCopy->SetBinContent(k, l, reldiffabs);
    }
  differenceCopy->DrawCopy("COLZ");
  differenceCopy->SetStats(0);


  graphicsOutput->cd(4); //legend
  TLegend* legend = new TLegend(0.2, 0.2, 0.8, 0.8, NULL, "brNDC");
  legend->SetFillColor(kWhite);
  //legend->SetLineColor(kWhite);
  legend->AddEntry(dataCopy, Form("Data distribution (%i entries)", (int) fInputData->GetEntries()));
  legend->AddEntry(fitResultCopy, Form("Template fit result (#chi^{2}/ndf=%5.2f)", Chi2() / NDF()));
  legend->Draw();


  return graphicsOutput;
}

TH2F* TemplateFitter2D::CloneCombinedResultHistogram(const char* hname = "") const {

  if (!fHasBeenFit) {
    WARN_OUT << "No fit was done!" << std::endl;
    return 0;
  }

  return (TH2F*) fFitResult->Clone(hname);
}

double TemplateFitter2D::Fit(int i, double lowBound, double highBound) {

  if (lowBound != 0 || highBound != 0)
    WARN_OUT << "TemplateFitter2D does not support fit ranges." << std::endl;

  return TemplateFitter::Fit(i, 0, 0);
}

bool TemplateFitter2D::TestHistogramCompatibility() const {

  //INFO_OUT << "Compatibility..." << std::endl;

  for (int i = 0; i < (int) fInputTemplates.size(); i++) {
    //check minimum, maximum, bin number and bin width
    assert(fInputTemplates.at(i));
    assert(fInputData);
    if (fInputTemplates.at(i)->GetNbinsX() != fInputData->GetNbinsX())
      return false;

    if (fInputTemplates.at(i)->GetNbinsY() != fInputData->GetNbinsY())
      return false;

    if (fInputTemplates.at(i)->GetEntries() == 0)
      return false;

    for (int k = 1; k <= fInputData->GetNbinsX(); k++)
      if (fInputTemplates.at(i)->GetXaxis()->GetBinLowEdge(k) != fInputData->GetXaxis()->GetBinLowEdge(k)) {
        return false;
      }

    for (int k = 1; k <= fInputData->GetNbinsY(); k++)
      if (fInputTemplates.at(i)->GetYaxis()->GetBinLowEdge(k) != fInputData->GetYaxis()->GetBinLowEdge(k)) {
        return false;
      }
  }

  return true;
}

TH1F* TemplateFitter2D::GetResultHistogramXprojection(const char* hname = "", double Ylow, double Yhigh) const {

  if (!fHasBeenFit) {
    WARN_OUT << "No fit was done!" << std::endl;
    return 0;
  }

  if (Ylow == 0 && Yhigh == 0)
    return (TH1F*) Cast(fFitResult)->ProjectionX(hname, 0, -1, "e");
  else
    return (TH1F*) Cast(fFitResult)->ProjectionX(hname, fFitResult->GetYaxis()->FindFixBin(Ylow), fFitResult->GetYaxis()->FindFixBin(Yhigh), "e");
}

TH1F* TemplateFitter2D::GetResultHistogramYprojection(const char* hname = "", double Xlow, double Xhigh) const {

  if (!fHasBeenFit) {
    WARN_OUT << "No fit was done!" << std::endl;
    return 0;
  }

  if (Xlow == 0 && Xhigh == 0)
    return (TH1F*) Cast(fFitResult)->ProjectionY(hname, 0, -1, "e");
  else
    return (TH1F*) Cast(fFitResult)->ProjectionY(hname, fFitResult->GetXaxis()->FindFixBin(Xlow), fFitResult->GetXaxis()->FindFixBin(Xhigh), "e");
}

TCanvas* TemplateFitter2D::CreateResultDrawingXprojection(std::string canvasname, int width, int height, double Ylow, double Yhigh) const {

  if (!fHasBeenFit) {
    WARN_OUT << "No fit was done!" << std::endl;
    return 0;
  }

  bool allrange = false;
  if (Ylow == 0 && Yhigh == 0)
    allrange = true;

  gStyle->SetOptStat(0);
  TCanvas* graphicsOutput = new TCanvas(canvasname.c_str(), canvasname.c_str(), width, height);
  graphicsOutput->cd();
  gPad->SetLogy();
//  gPad->SetGrid();

//  TLegend* legend = new TLegend(0.6034913, 0.7009346, 0.8944306, 0.8913551, NULL, "brNDC");
  TLegend* legend = new TLegend(0.35453035, 0.7009346, 0.64546965, 0.8913551, NULL, "brNDC");
  legend->SetFillColor(kWhite);
  legend->SetLineColor(kWhite);
  legend->SetTextFont(62); 

  TH1* dataCopy;
  if (allrange)
    dataCopy = Cast(fInputData)->ProjectionX()->DrawCopy("PE");
  else
    dataCopy = Cast(fInputData)->ProjectionX("", fInputData->GetYaxis()->FindFixBin(Ylow), fInputData->GetYaxis()->FindFixBin(Yhigh))->DrawCopy("PE");
  dataCopy->SetStats(0); // disable statistic boxes in template canvas
  const int dataColor = kBlack;
  const int dataMarker = 20;
  dataCopy->SetLineWidth(2);
  dataCopy->SetLineColor(dataColor);
  dataCopy->SetMarkerColor(dataColor);
  dataCopy->SetMarkerStyle(dataMarker);
  dataCopy->GetXaxis()->SetTitle("#bf{Charge Confusion Estimator}");
  if (allrange)
    legend->AddEntry(dataCopy, Form("Data distribution (X projection) (%.0f entries)", fInputData->GetEntries()));
  else
    legend->AddEntry(dataCopy, Form("Data distribution (X projection, %.2f < Y < %.2f) (%.0f entries)", Ylow, Yhigh, fInputData->GetEntries()));

  TH1* fitResultCopy;
  if (allrange)
    fitResultCopy = Cast(fFitResult)->ProjectionX()->DrawCopy("hist.same");
  else
    fitResultCopy = Cast(fFitResult)->ProjectionX("", fFitResult->GetYaxis()->FindFixBin(Ylow), fFitResult->GetYaxis()->FindFixBin(Yhigh))->DrawCopy("hist.same");
  fitResultCopy->SetStats(0);
  const int fitColor = kBlack;
  const int fitStyle = 2;
  fitResultCopy->SetLineWidth(4);
  fitResultCopy->SetLineColor(fitColor);
  fitResultCopy->SetLineStyle(fitStyle);
  if (allrange)
    legend->AddEntry(fitResultCopy, Form("Template fit result (X projection) (#chi^{2}/ndf=%5.2f/%d=%5.2f)", Chi2(), NDF(), Chi2() / NDF()));
  else
    legend->AddEntry(fitResultCopy, Form("Template fit result (X projection, %.2f < Y < %.2f) (#chi^{2}/ndf=%5.2f/%d=%5.2f)", Ylow, Yhigh, Chi2(), NDF(), Chi2() / NDF()));

  for (unsigned int i = 0; i < fResultHistos.size(); ++i) {
    TH1* resultCopy;
    if (allrange)
      resultCopy = Cast(fResultHistos.at(i))->ProjectionX()->DrawCopy("hist.same");
    else
      resultCopy = Cast(fResultHistos.at(i))->ProjectionX("", fResultHistos.at(i)->GetYaxis()->FindFixBin(Ylow), fResultHistos.at(i)->GetYaxis()->FindFixBin(Yhigh))->DrawCopy("hist.same");
    resultCopy->SetStats(0);

    resultCopy->SetLineWidth(2);
    const int color = TemplateColor(i);
    const int fillStyle = TemplateFillStyle(i);
    resultCopy->SetFillStyle(fillStyle);
    resultCopy->SetFillColor(color);
    resultCopy->SetLineColor(color);
    resultCopy->SetMarkerColor(color);

    // split to long titles in two lines
    QString title = resultCopy->GetTitle();
    QString fittedValue = QString(" #color[%1]{Fitted: %2 #pm %3}")
                            .arg(resultCopy->GetLineColor())
                            .arg(GetAbsoluteResult().at(i), 0, 'f', 1, '0')
                            .arg(GetAbsoluteResultError().at(i), 0, 'f', 1, '0');
    title.append(fittedValue);
    if (title.contains(",")) {
      title.replace(",", "}{");
      title.prepend("#splitline{");
      title.append("}");
    }
    legend->AddEntry(resultCopy, qPrintable(title), "F");
  }
  // Redraw  fitResult and data to be on top of the templates
  fitResultCopy->Draw("hist.same");
  dataCopy->Draw("PEsame");

  legend->Draw();
  return graphicsOutput;
}

TCanvas* TemplateFitter2D::CreateResultDrawingYprojection(std::string canvasname, int width, int height, double Xlow, double Xhigh) const {

  if (!fHasBeenFit) {
    WARN_OUT << "No fit was done!" << std::endl;
    return 0;
  }

  bool allrange = false;
  if (Xlow == 0 && Xhigh == 0)
    allrange = true;

  gStyle->SetOptStat(0);
  TCanvas* graphicsOutput = new TCanvas(canvasname.c_str(), canvasname.c_str(), width, height);
  graphicsOutput->cd();
  gPad->SetLogy();
//  gPad->SetGrid();

  TLegend* legend = new TLegend(0.6034913, 0.7009346, 0.8944306, 0.8913551, NULL, "brNDC");
  legend->SetFillColor(kWhite);
  legend->SetLineColor(kWhite);
  legend->SetTextFont(62);

  TH1* dataCopy;
  if (allrange)
    dataCopy = Cast(fInputData)->ProjectionY()->DrawCopy("PE");
  else
    dataCopy = Cast(fInputData)->ProjectionY("", fInputData->GetXaxis()->FindFixBin(Xlow), fInputData->GetXaxis()->FindFixBin(Xhigh))->DrawCopy("PE");
  dataCopy->SetStats(0); // disable statistic boxes in template canvas
  const int dataColor = kBlack;
  const int dataMarker = 20;
  dataCopy->SetLineWidth(2);
  dataCopy->SetLineColor(dataColor);
  dataCopy->SetMarkerColor(dataColor);
  dataCopy->SetMarkerStyle(dataMarker);
  dataCopy->GetXaxis()->SetTitle("#bf{TrdLikelihood}");
  if (allrange)
    legend->AddEntry(dataCopy, Form("Data distribution (Y projection) (%.0f entries)", fInputData->GetEntries()));
  else
    legend->AddEntry(dataCopy, Form("Data distribution (Y projection, %.2f < X < %.2f) (%.0f entries)", Xlow, Xhigh, fInputData->GetEntries()));

  TH1* fitResultCopy;
  if (allrange)
    fitResultCopy = Cast(fFitResult)->ProjectionY()->DrawCopy("hist.same");
  else
    fitResultCopy = Cast(fFitResult)->ProjectionY("", fFitResult->GetXaxis()->FindFixBin(Xlow), fFitResult->GetXaxis()->FindFixBin(Xhigh))->DrawCopy("hist.same");
  fitResultCopy->SetStats(0);
  const int fitColor = kBlack;
  const int fitStyle = 2;
  fitResultCopy->SetLineWidth(4);
  fitResultCopy->SetLineColor(fitColor);
  fitResultCopy->SetLineStyle(fitStyle);
  if (allrange)
    legend->AddEntry(fitResultCopy, Form("Template fit result (Y projection) (#chi^{2}/ndf=%5.2f/%d=%5.2f)", Chi2(), NDF(), Chi2() / NDF()));
  else
    legend->AddEntry(fitResultCopy, Form("Template fit result (Y projection, %.2f < X < %.2f) (#chi^{2}/ndf=%5.2f/%d=%5.2f)", Xlow, Xhigh, Chi2(), NDF(), Chi2() / NDF()));


  for (unsigned int i = 0; i < fResultHistos.size(); ++i) {
    TH1* resultCopy;
    if (allrange)
      resultCopy = Cast(fResultHistos.at(i))->ProjectionY()->DrawCopy("hist.same");
    else
      resultCopy = Cast(fResultHistos.at(i))->ProjectionY("", fResultHistos.at(i)->GetXaxis()->FindFixBin(Xlow), fResultHistos.at(i)->GetXaxis()->FindFixBin(Xhigh))->DrawCopy("hist.same");
    resultCopy->SetStats(0);

    resultCopy->SetLineWidth(2);
    const int color = TemplateColor(i);
    const int fillStyle = TemplateFillStyle(i);
    resultCopy->SetFillStyle(fillStyle);
    resultCopy->SetFillColor(color);
    resultCopy->SetLineColor(color);
    resultCopy->SetMarkerColor(color);

    // split to long titles in two lines
    QString title = resultCopy->GetTitle();
    QString fittedValue = QString(" #color[%1]{Fitted: %2 #pm %3}")
                            .arg(resultCopy->GetLineColor())
                            .arg(GetAbsoluteResult().at(i), 0, 'f', 1, '0')
                            .arg(GetAbsoluteResultError().at(i), 0, 'f', 1, '0');
    title.append(fittedValue);
    if (title.contains(",")) {
      title.replace(",", "}{");
      title.prepend("#splitline{");
      title.append("}");
    }
    legend->AddEntry(resultCopy, qPrintable(title), "F");
  }
  // Redraw  fitResult and data to be on top of the templates
  fitResultCopy->Draw("hist.same");
  dataCopy->Draw("PEsame");

  legend->Draw();
  return graphicsOutput;
}

const TH2* TemplateFitter2D::Cast(const TH1* histogram) const {
  const TH2* castHistogram = dynamic_cast<const TH2*>(histogram);
  assert(castHistogram);
  return castHistogram;
}

} // namespace Utilities

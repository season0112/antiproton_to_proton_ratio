void ROOTBuild(const char* filename) {
  gSystem->SetBuildDir("/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/compiledROOT");

  int rc = gSystem->CompileMacro(filename,"kf");
  exit(!rc);
}

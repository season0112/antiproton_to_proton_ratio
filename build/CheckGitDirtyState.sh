#!/bin/bash
if [[ -e /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/ProjectVersion.C ]]
then
  GITSHA=$(git --git-dir /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/.git --work-tree /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt rev-parse HEAD)
  ISNOTDIRTY=$(git --git-dir /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/.git --work-tree /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt diff-index --name-only HEAD)
  if [[ -n "$ISNOTDIRTY" ]]
  then
    GITSHA=$GITSHA"-dirty"
  fi
  FOUND=$(grep "// GIT SHA" /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/ProjectVersion.C | sed "s#// GIT SHA: ##")
  if [[ "$FOUND" != "$GITSHA" ]]
  then
    /usr/local/software/juropatest/Stages/2016b/software/CMake/3.6.2-GCCcore-6.3.0/bin/cmake -DPROJECTNAME=ExampleAnalysis -DPROJECTVERSION=undefined -DPROJECTGITSHA=${GITSHA} -DIN_FILE=/homea/vsk10/vsk1056/Software/ACsoft/cmake/templates/ProjectVersion.C.in -DOUT_FILE=/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/ProjectVersion.C -P /homea/vsk10/vsk1056/Software/ACsoft/cmake/ReconfigureVersion.cmake
  fi
fi

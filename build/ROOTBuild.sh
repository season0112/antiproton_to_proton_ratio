#!/bin/bash
unset SDKROOT
pushd /homea/vsk10/vsk1056/Software/ACsoft >& /dev/null
source scripts/thisacsoft.sh >& /dev/null
popd >& /dev/null

unset ACSOFT_ADDITIONAL_LOGONS
export ACSOFT_SOURCEDIR_OVERRIDE=/homea/vsk10/vsk1056/Software/ACsoft

if [[ -z $VERBOSE ]]; then
    OUTPUT=$(/work/vsk10/vsk1002/public/software/root/6.08.02/x86_64-slc6-icc17_gcc63-opt/bin/root -l -n -b -q /homea/vsk10/vsk1056/Software/ACsoft/rootlogon.C /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/rootlogon.C /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/ROOTBuild.C\(\"$1\"\) 2>&1)
    RETVALUE=$?
    if [[ $RETVALUE != 0 ]]; then
        echo -e "$OUTPUT" 1>&2
    fi
    exit $RETVALUE
else
    /work/vsk10/vsk1002/public/software/root/6.08.02/x86_64-slc6-icc17_gcc63-opt/bin/root -l -n -b -q /homea/vsk10/vsk1056/Software/ACsoft/rootlogon.C /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/rootlogon.C /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/ROOTBuild.C\(\"$1\"\)
    exit $?
fi

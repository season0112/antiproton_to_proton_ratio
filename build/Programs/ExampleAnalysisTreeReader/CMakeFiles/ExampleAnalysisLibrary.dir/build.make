# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/software/juropatest/Stages/2016b/software/CMake/3.6.2-GCCcore-6.3.0/bin/cmake

# The command to remove a file.
RM = /usr/local/software/juropatest/Stages/2016b/software/CMake/3.6.2-GCCcore-6.3.0/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build

# Include any dependencies generated for this target.
include Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/depend.make

# Include the progress variables for this target.
include Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/progress.make

# Include the compile flags for this target's objects.
include Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/flags.make

Programs/ExampleAnalysisTreeReader/ExampleAnalysisLibraryDict.cxx: ../Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.hh
Programs/ExampleAnalysisTreeReader/ExampleAnalysisLibraryDict.cxx: ../Programs/ExampleAnalysisTreeReader/Linkdef.h
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating ExampleAnalysisLibraryDict.cxx, ../../../lib/ExampleAnalysisLibraryDict_rdict.pcm"
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && /work/vsk10/vsk1002/public/software/root/6.08.02/x86_64-slc6-icc17_gcc63-opt/bin/rootcint -cint -f ExampleAnalysisLibraryDict.cxx -c -p -std=c++11 -DQT_NO_DEBUG -D_GLIBCXX_USE_CXX11_ABI=1 -DHAVE_NEWER_TYPE_TRAITS -DENABLE_MPI -DQT_NO_DEBUG -DQT_CORE_LIB -UNDEBUG -I/homea/vsk10/vsk1056/Software/ACsoft -I/homea/vsk10/vsk1056/Software/ACsoft/acceptance -I/homea/vsk10/vsk1056/Software/ACsoft/acqt -I/homea/vsk10/vsk1056/Software/ACsoft/analysis -I/homea/vsk10/vsk1056/Software/ACsoft/backtracing -I/homea/vsk10/vsk1056/Software/ACsoft/binning -I/homea/vsk10/vsk1056/Software/ACsoft/calibration -I/homea/vsk10/vsk1056/Software/ACsoft/compat -I/homea/vsk10/vsk1056/Software/ACsoft/compat/QtCore -I/homea/vsk10/vsk1056/Software/ACsoft/core -I/homea/vsk10/vsk1056/Software/ACsoft/math -I/homea/vsk10/vsk1056/Software/ACsoft/mva -I/homea/vsk10/vsk1056/Software/ACsoft/mva/implementations -I/homea/vsk10/vsk1056/Software/ACsoft/cuts -I/homea/vsk10/vsk1056/Software/ACsoft/cuts/attachments -I/homea/vsk10/vsk1056/Software/ACsoft/detector -I/homea/vsk10/vsk1056/Software/ACsoft/io -I/homea/vsk10/vsk1056/Software/ACsoft/modelling -I/homea/vsk10/vsk1056/Software/ACsoft/producer -I/homea/vsk10/vsk1056/Software/ACsoft/systemx -I/homea/vsk10/vsk1056/Software/ACsoft/trdcalibration -I/homea/vsk10/vsk1056/Software/ACsoft/unfolding -I/homea/vsk10/vsk1056/Software/ACsoft/utilities -I/homea/vsk10/vsk1056/Software/ACsoft/rti -I/homea/vsk10/vsk1056/Software/ACsoft/build/streamers -I/homea/vsk10/vsk1056/Software/ACsoft/build/adl -I/homea/vsk10/vsk1056/Software/ACsoft/build/adl/AC -I/homea/vsk10/vsk1056/Software/ACsoft/build/compat -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtDesigner -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtDeclarative -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtScriptTools -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtDesigner -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtXml -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtSql -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtOpenGL -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtMultimedia -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtNetwork -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtHelp -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtUiTools -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtTest -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtScript -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtSvg -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/Qt3Support -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtGui -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtCore -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/mkspecs/default -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include -I/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/include/QtCore -I/work/vsk10/vsk1002/public/software/root/6.08.02/x86_64-slc6-icc17_gcc63-opt/include -I/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Libraries/ExampleAnalysisTree /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.hh /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/Linkdef.h && mkdir -p /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/lib && cp -f ExampleAnalysisLibraryDict_rdict.pcm /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/lib

../lib/ExampleAnalysisLibraryDict_rdict.pcm: Programs/ExampleAnalysisTreeReader/ExampleAnalysisLibraryDict.cxx
	@$(CMAKE_COMMAND) -E touch_nocreate ../lib/ExampleAnalysisLibraryDict_rdict.pcm

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/flags.make
Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o: ../Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.C
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o"
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o -c /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.C

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.i"
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.C > CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.i

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.s"
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader/ExampleAnalysisTreeReader.C -o CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.s

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o.requires:

.PHONY : Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o.requires

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o.provides: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o.requires
	$(MAKE) -f Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/build.make Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o.provides.build
.PHONY : Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o.provides

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o.provides.build: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o


Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/flags.make
Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o: Programs/ExampleAnalysisTreeReader/ExampleAnalysisLibraryDict.cxx
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o"
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o -c /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader/ExampleAnalysisLibraryDict.cxx

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.i"
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader/ExampleAnalysisLibraryDict.cxx > CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.i

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.s"
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader/ExampleAnalysisLibraryDict.cxx -o CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.s

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o.requires:

.PHONY : Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o.requires

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o.provides: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o.requires
	$(MAKE) -f Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/build.make Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o.provides.build
.PHONY : Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o.provides

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o.provides.build: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o


# Object files for target ExampleAnalysisLibrary
ExampleAnalysisLibrary_OBJECTS = \
"CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o" \
"CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o"

# External object files for target ExampleAnalysisLibrary
ExampleAnalysisLibrary_EXTERNAL_OBJECTS =

../lib/libExampleAnalysisLibrary.so: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o
../lib/libExampleAnalysisLibrary.so: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o
../lib/libExampleAnalysisLibrary.so: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/build.make
../lib/libExampleAnalysisLibrary.so: ../lib/libExampleAnalysisTree.so
../lib/libExampleAnalysisLibrary.so: ../lib/libExampleAnalysisVersion.so
../lib/libExampleAnalysisLibrary.so: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared library ../../../lib/libExampleAnalysisLibrary.so"
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ExampleAnalysisLibrary.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/build: ../lib/libExampleAnalysisLibrary.so

.PHONY : Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/build

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/requires: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisTreeReader.C.o.requires
Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/requires: Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/ExampleAnalysisLibraryDict.cxx.o.requires

.PHONY : Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/requires

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/clean:
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader && $(CMAKE_COMMAND) -P CMakeFiles/ExampleAnalysisLibrary.dir/cmake_clean.cmake
.PHONY : Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/clean

Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/depend: Programs/ExampleAnalysisTreeReader/ExampleAnalysisLibraryDict.cxx
Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/depend: ../lib/ExampleAnalysisLibraryDict_rdict.pcm
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/Programs/ExampleAnalysisTreeReader /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Programs/ExampleAnalysisTreeReader/CMakeFiles/ExampleAnalysisLibrary.dir/depend


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
include CMakeFiles/ExampleAnalysisVersion.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/ExampleAnalysisVersion.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/ExampleAnalysisVersion.dir/flags.make

CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o: CMakeFiles/ExampleAnalysisVersion.dir/flags.make
CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o: ProjectVersion.C
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o"
	ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o -c /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/ProjectVersion.C

CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.i"
	ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/ProjectVersion.C > CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.i

CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.s"
	ccache /usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicpc  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/ProjectVersion.C -o CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.s

CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o.requires:

.PHONY : CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o.requires

CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o.provides: CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o.requires
	$(MAKE) -f CMakeFiles/ExampleAnalysisVersion.dir/build.make CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o.provides.build
.PHONY : CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o.provides

CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o.provides.build: CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o


# Object files for target ExampleAnalysisVersion
ExampleAnalysisVersion_OBJECTS = \
"CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o"

# External object files for target ExampleAnalysisVersion
ExampleAnalysisVersion_EXTERNAL_OBJECTS =

../lib/libExampleAnalysisVersion.so: CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o
../lib/libExampleAnalysisVersion.so: CMakeFiles/ExampleAnalysisVersion.dir/build.make
../lib/libExampleAnalysisVersion.so: CMakeFiles/ExampleAnalysisVersion.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library ../lib/libExampleAnalysisVersion.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ExampleAnalysisVersion.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/ExampleAnalysisVersion.dir/build: ../lib/libExampleAnalysisVersion.so

.PHONY : CMakeFiles/ExampleAnalysisVersion.dir/build

CMakeFiles/ExampleAnalysisVersion.dir/requires: CMakeFiles/ExampleAnalysisVersion.dir/ProjectVersion.C.o.requires

.PHONY : CMakeFiles/ExampleAnalysisVersion.dir/requires

CMakeFiles/ExampleAnalysisVersion.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ExampleAnalysisVersion.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ExampleAnalysisVersion.dir/clean

CMakeFiles/ExampleAnalysisVersion.dir/depend:
	cd /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build /homea/vsk10/vsk1056/Software/myanalysisversion6.2_ecalbdt/build/CMakeFiles/ExampleAnalysisVersion.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ExampleAnalysisVersion.dir/depend


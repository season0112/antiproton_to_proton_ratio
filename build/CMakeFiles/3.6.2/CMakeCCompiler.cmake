set(CMAKE_C_COMPILER "/usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/bin64/mpiicc")
set(CMAKE_C_COMPILER_ARG1 "")
set(CMAKE_C_COMPILER_ID "Intel")
set(CMAKE_C_COMPILER_VERSION "17.0.1.20161005")
set(CMAKE_C_COMPILER_WRAPPER "")
set(CMAKE_C_STANDARD_COMPUTED_DEFAULT "11")
set(CMAKE_C_COMPILE_FEATURES "c_function_prototypes;c_restrict;c_static_assert;c_variadic_macros")
set(CMAKE_C90_COMPILE_FEATURES "c_function_prototypes")
set(CMAKE_C99_COMPILE_FEATURES "c_restrict;c_static_assert;c_variadic_macros")
set(CMAKE_C11_COMPILE_FEATURES "")

set(CMAKE_C_PLATFORM_ID "Linux")
set(CMAKE_C_SIMULATE_ID "")
set(CMAKE_C_SIMULATE_VERSION "")

set(CMAKE_AR "/usr/local/software/juropatest/Stages/2016b/software/binutils/2.27-GCCcore-6.3.0/bin/ar")
set(CMAKE_RANLIB "/usr/local/software/juropatest/Stages/2016b/software/binutils/2.27-GCCcore-6.3.0/bin/ranlib")
set(CMAKE_LINKER "/usr/local/software/juropatest/Stages/2016b/software/binutils/2.27-GCCcore-6.3.0/bin/ld")
set(CMAKE_COMPILER_IS_GNUCC )
set(CMAKE_C_COMPILER_LOADED 1)
set(CMAKE_C_COMPILER_WORKS TRUE)
set(CMAKE_C_ABI_COMPILED TRUE)
set(CMAKE_COMPILER_IS_MINGW )
set(CMAKE_COMPILER_IS_CYGWIN )
if(CMAKE_COMPILER_IS_CYGWIN)
  set(CYGWIN 1)
  set(UNIX 1)
endif()

set(CMAKE_C_COMPILER_ENV_VAR "CC")

if(CMAKE_COMPILER_IS_MINGW)
  set(MINGW 1)
endif()
set(CMAKE_C_COMPILER_ID_RUN 1)
set(CMAKE_C_SOURCE_FILE_EXTENSIONS c;m)
set(CMAKE_C_IGNORE_EXTENSIONS h;H;o;O;obj;OBJ;def;DEF;rc;RC)
set(CMAKE_C_LINKER_PREFERENCE 10)

# Save compiler ABI information.
set(CMAKE_C_SIZEOF_DATA_PTR "8")
set(CMAKE_C_COMPILER_ABI "ELF")
set(CMAKE_C_LIBRARY_ARCHITECTURE "")

if(CMAKE_C_SIZEOF_DATA_PTR)
  set(CMAKE_SIZEOF_VOID_P "${CMAKE_C_SIZEOF_DATA_PTR}")
endif()

if(CMAKE_C_COMPILER_ABI)
  set(CMAKE_INTERNAL_PLATFORM_ABI "${CMAKE_C_COMPILER_ABI}")
endif()

if(CMAKE_C_LIBRARY_ARCHITECTURE)
  set(CMAKE_LIBRARY_ARCHITECTURE "")
endif()

set(CMAKE_C_CL_SHOWINCLUDES_PREFIX "")
if(CMAKE_C_CL_SHOWINCLUDES_PREFIX)
  set(CMAKE_CL_SHOWINCLUDES_PREFIX "${CMAKE_C_CL_SHOWINCLUDES_PREFIX}")
endif()




set(CMAKE_C_IMPLICIT_LINK_LIBRARIES "mpifort;mpi;mpigi;dl;rt;pthread;imf;svml;irng;m;ipgo;decimal;cilkrts;stdc++;irc;svml;c;irc_s;dl;c")
set(CMAKE_C_IMPLICIT_LINK_DIRECTORIES "/usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/intel64/lib/release_mt;/usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/intel64/lib;/usr/local/software/juropatest/Stages/2016b/software/Valgrind/3.11.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/FFTW/3.3.5-iimpi-2016b.1/lib;/usr/local/software/juropatest/Stages/2016b/software/X.Org/2016-09-22-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/zsh/5.2-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/Qt/4.8.7-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/libGLU/9.0.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/freetype/2.7-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/libpng/1.6.25-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/LLVM/3.9.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/eudev/3.2-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/GLib/2.50.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/util-linux/2.28.2-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/Python/2.7.12-GCCcore-6.3.0-bare/lib;/usr/local/software/juropatest/Stages/2016b/software/libxslt/1.1.29-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/SQLite/3.14.2-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/Tcl/8.6.6-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/libreadline/7.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/PCRE/8.39-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/libxml2/2.9.4-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/libffi/3.2.1-GCCcore-6.3.0/lib64;/usr/local/software/juropatest/Stages/2016b/software/libffi/3.2.1-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/GSL/1.16-intel-2016b.1/lib;/usr/local/software/juams/Stages/2016b/software/imkl/2017.1.132-iimpi-2016b.1/mkl/lib/intel64;/usr/local/software/juams/Stages/2016b/software/imkl/2017.1.132-iimpi-2016b.1/lib/intel64;/usr/local/software/juropatest/Stages/2016b/software/git/2.10.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/Perl/5.24.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/gettext/0.19.8-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/XZ/5.2.2-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/zlib/1.2.8-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/expat/2.1.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/cURL/7.50.3-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/ncurses/6.0-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/binutils/2.27-GCCcore-6.3.0/lib;/usr/local/software/juropatest/Stages/2016b/software/GCCcore/6.3.0/lib64;/usr/local/software/juropatest/Stages/2016b/software/GCCcore/6.3.0/lib;/usr/local/software/juams/Stages/2016b/software/impi/2017.1.132-iccifort-2017.1.132-GCC-5.4.0/lib64;/usr/local/software/juams/Stages/2016b/software/ifort/2017.1.132-GCC-5.4.0/compilers_and_libraries_2017.1.132/linux/mpi/intel64;/usr/local/software/juams/Stages/2016b/software/ifort/2017.1.132-GCC-5.4.0/compilers_and_libraries_2017.1.132/linux/compiler/lib/intel64;/usr/local/software/juams/Stages/2016b/software/ifort/2017.1.132-GCC-5.4.0/lib/intel64;/usr/local/software/juams/Stages/2016b/software/ifort/2017.1.132-GCC-5.4.0/lib;/usr/local/software/juams/Stages/2016b/software/icc/2017.1.132-GCC-5.4.0/compilers_and_libraries_2017.1.132/linux/compiler/lib/intel64;/usr/local/software/juams/Stages/2016b/software/icc/2017.1.132-GCC-5.4.0/lib/intel64;/usr/local/software/juams/Stages/2016b/software/icc/2017.1.132-GCC-5.4.0/lib;/usr/local/software/juropatest/Stages/2016b/software/icc/2017.1.132-GCC-5.4.0/compilers_and_libraries_2017.1.132/linux/compiler/lib/intel64_lin;/usr/local/software/juams/Stages/2016b/software/ifort/2017.1.132-GCC-5.4.0/compilers_and_libraries_2017.1.132/linux/mpi/lib64;/usr/local/software/juropatest/Stages/2016b/software/GCCcore/6.3.0/lib/gcc/x86_64-pc-linux-gnu/6.3.0;/lib64;/usr/lib64;/lib;/usr/lib")
set(CMAKE_C_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES "")

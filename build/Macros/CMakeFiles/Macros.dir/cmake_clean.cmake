file(REMOVE_RECURSE
  "../../lib/libMacros.pdb"
  "../../lib/libMacros.so"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/Macros.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()

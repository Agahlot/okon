add_library(okon STATIC
    btree.hpp
    btree_base.hpp
    btree_node.cpp
    btree_node.hpp
    btree_sorted_keys_inserter.hpp
    okon.cpp
    preparer.cpp
    preparer.hpp
    sha1_utils.hpp
    splitted_files.hpp
    splitted_files.cpp
)

target_link_libraries(okon
    PRIVATE
        ${CMAKE_THREAD_LIBS_INIT}
)

target_include_directories(okon
    PRIVATE
        ${OKON_INCLUDE_DIR}
)

set_target_properties(okon
    PROPERTIES
        PUBLIC_HEADER ${OKON_INCLUDE_DIR}/okon/okon.h
)

include(GNUInstallDirs)

install(
    TARGETS okon
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/okon
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

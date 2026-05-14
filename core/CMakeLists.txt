add_library(stego_core SHARED
    src/stego.cpp
)

target_include_directories(stego_core PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
add_library(stego_core SHARED
    src/stego.cpp
    src/image.cpp
    src/steganography.cpp
)

target_include_directories(stego_core PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
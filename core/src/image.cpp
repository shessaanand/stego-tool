#include "image.hpp"
#define STB_IMAGE_IMPLEMENTATION
#include "../../external/stb/stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "../../external/stb/stb_image_write.h"
#include <iostream>

Image::Image(const std::string& filename)
    : width(0), height(0), channels(0){
    unsigned char* imgData = stbi_load(
        filename.c_str(),
        &width,
        &height,
        &channels,
        0
    );

    if (!imgData){
        std::cerr << "Failed to load image\n";
        return;
    }

    data.assign(
        imgData,
        imgData + (width * height * channels)
    );

    stbi_image_free(imgData);
}

bool Image::save(const std::string& filename){
    return stbi_write_png(
        filename.c_str(),
        width,
        height,
        channels,
        data.data(),
        width * channels
    );
}
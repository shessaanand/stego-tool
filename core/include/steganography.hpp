#pragma once
#include "image.hpp"
#include <string>

class Steganography{
public:
    static void encode(Image& image, const std::string& message);
    static std::string decode(const Image& image);
};
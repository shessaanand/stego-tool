#pragma once
#include "image.hpp"
#include <string>

class Steganography{
public:
    static void encode(Image& image, const std::string& message);
};
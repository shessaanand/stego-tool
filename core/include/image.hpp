#pragma once

#include <string>
#include <vector>

class Image{
public:
    int width;
    int height;
    int channels;

    std::vector<unsigned char> data;

    Image(const std::string& filename);
    bool save(const std::string& filename);
};
#include "../include/steganography.hpp"
#include <bitset>
#include <iostream>

void Steganography::encode(Image& image, const std::string& message){
    std::string binaryMessage;

    for (char c : message){
        binaryMessage += std::bitset<8>(c).to_string();
    }

    if (binaryMessage.size() > image.data.size()){
        std::cerr << "Message too large for image\n";
        return;
    }

    for (size_t i = 0; i < binaryMessage.size(); ++i){
        image.data[i] &= 0xFE;

        image.data[i] |= (binaryMessage[i] - '0');
    }

    std::cout << "Message encoded successfully\n";
}
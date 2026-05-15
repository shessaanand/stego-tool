#include "../include/steganography.hpp"
#include <bitset>
#include <iostream>
#include <cstdint>

void Steganography::encode(Image& image, const std::string& message){
    uint32_t messageLength = message.size();

    std::string binaryMessage;

    binaryMessage += std::bitset<32>(messageLength).to_string();

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

std::string Steganography::decode(const Image& image){
    std::string lengthBits;

    for (size_t i = 0; i < 32; ++i){
        lengthBits += (image.data[i] & 1) ? '1' : '0';
    }

    uint32_t messageLength =
        std::bitset<32>(lengthBits).to_ulong();

    std::string decodedMessage;

    size_t bitIndex = 32;

    for (uint32_t charIndex = 0;
         charIndex < messageLength;
         ++charIndex){

        std::string byte;

        for (int bit = 0; bit < 8; ++bit){
            byte += (image.data[bitIndex] & 1)
                ? '1'
                : '0';

            ++bitIndex;
        }

        char character = static_cast<char>(
            std::bitset<8>(byte).to_ulong()
        );

        decodedMessage += character;
    }

    return decodedMessage;
}
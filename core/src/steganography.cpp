#include "../include/steganography.hpp"
#include <bitset>
#include <iostream>

void Steganography::encode(Image& image, const std::string& message){
    std::string fullMessage = message + '\0';
    std::string binaryMessage;
    for (char c : fullMessage){
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
    std::string binaryMessage;
    for (size_t i = 0; i < image.data.size(); ++i){
        binaryMessage += (image.data[i] & 1) ? '1' : '0';
    }

    std::string decodedMessage;

    for (size_t i = 0; i < binaryMessage.size(); i += 8){
        std::string byte = binaryMessage.substr(i, 8);
        char character = static_cast<char>(
            std::bitset<8>(byte).to_ulong()
        );
        if (character == '\0'){
            break;
        }
        decodedMessage += character;
    }
    return decodedMessage;
}
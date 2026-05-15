#include "core/include/image.hpp"
#include "core/include/steganography.hpp"
#include <iostream>

int main(){
    Image img("../sample.png");
    std::cout << "Width: " << img.width << "\n";
    std::cout << "Height: " << img.height << "\n";
    std::cout << "Channels: " << img.channels << "\n";
    std::string secretMessage = "Hello World";
    Steganography::encode(img, secretMessage);

    if (!img.save("encoded.png")){
        std::cout << "Failed to save image\n";
        return 1;
    }

    std::cout << "Saved encoded.png\n";
    Image encodedImage("encoded.png");
    std::string decoded = Steganography::decode(encodedImage);
    std::cout << "Decoded message: "<< decoded << "\n";
    return 0;
}
#include "core/include/image.hpp"
#include "core/include/steganography.hpp"
#include <iostream>

int main(){
    Image img("../sample.png");

    std::cout << "Width: " << img.width << "\n";
    std::cout << "Height: " << img.height << "\n";
    std::cout << "Channels: " << img.channels << "\n";

    Steganography::encode(img, "Hello World");
    if (img.save("encoded.png")){
        std::cout << "Saved encoded.png\n";
    }
    else{
        std::cout << "Failed to save image\n";
    }

    return 0;
}
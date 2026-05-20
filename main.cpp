#include "core/include/image.hpp"
#include "core/include/steganography.hpp"

#include <iostream>
#include <string>

int main(int argc, char* argv[]){
    if (argc < 2){
        std::cout
            << "Usage:\n"
            << "./stego encode <input> <output> <message>\n"
            << "./stego decode <image>\n";

        return 1;
    }

    std::string mode = argv[1];

    if (mode == "encode"){
        if (argc < 5){
            std::cout
                << "Usage:\n"
                << "./stego encode <input> <output> <message>\n";

            return 1;
        }

        std::string inputImage = argv[2];
        std::string outputImage = argv[3];
        std::string message = argv[4];

        Image img(inputImage);

        if (img.data.empty()){
            std::cout << "Failed to load image\n";
            return 1;
        }

        size_t maxBytes =
            (img.data.size() - 32) / 8;

        std::cout
            << "Maximum capacity: "
            << maxBytes
            << " bytes\n";

        if (message.size() > maxBytes){
            std::cout
                << "Message exceeds image capacity\n";

            return 1;
        }

        Steganography::encode(img, message);

        if (!img.save(outputImage)){
            std::cout << "Failed to save image\n";
            return 1;
        }

        std::cout
            << "Encoded image saved to "
            << outputImage
            << "\n";
    }

    else if (mode == "decode"){
        if (argc < 3){
            std::cout
                << "Usage:\n"
                << "./stego decode <image>\n";

            return 1;
        }

        std::string imagePath = argv[2];

        Image img(imagePath);

        if (img.data.empty()){
            std::cout << "Failed to load image\n";
            return 1;
        }

        std::string decoded =
            Steganography::decode(img);

        std::cout
            << "Decoded message: "
            << decoded
            << "\n";
    }

    else{
        std::cout
            << "Invalid mode\n"
            << "Use encode or decode\n";
    }

    return 0;
}

1. Local дээр буюу Pycharm project дээр турших
   1. Install dependencies
   ```bash
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```
   2. Configure environment variable
   ```bash
    export CLIENT_ID="my_value"
    export CLIENT_SECRET="my_value"
    export REFRESH_TOKEN="my_value"
    ```
   Санамж: pycharm project-оо шинээр нээх бүрт environment variable буюу орчны хувьсагчууд устах тул нээж шинээр нээхдээ дээрх 3 утгаа terminal дээр ажиллуулна. 
   Амархан байлгах үүднээс env.txt файл нээгээд энэ утгуудаа хадгалаад шууд copy/paste хийгээрэй. env.txt файлыг .gitignore буюу git рүү хуулахгүй байдлаар тохируулсан. Энэ нь нууц мэдээлэл агуулж байгаа (credentials) тул аюулгүй байдлын үүднээс зөвхөн компьютер дээрээ (онлайнд бус) хадгалах нь зүүтэй юм.
2. 
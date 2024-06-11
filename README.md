## Хэрхэн python code-оо xxx цаг тутам эсвэл xxx минут тутам ажиллуулах вэ?

### Ашиглах шаардлагатай технологууд:
1. **Google cloud console** - бол Google-ийн үүлэн үйлчилгээ ашиглан програм бүтээж ажиллуулах, өгөгдөл хадгалах, төрөл бүрийн тооцооллын ажлуудыг гүйцэтгэхэд ашигладаг вэбсайт юм. Үүний тусламжтай биш google drive API credencials буюу google drive руугаа кодоосоо хандах нууц түлхүүрийг гаргаж авна.
2. **Github** - бол хүмүүс кодоо хадгалж, хуваалцаж, төслүүд дээр хамтран ажиллаж, коддоо хийсэн өөрчлөлтүүдийг хянах боломжтой вэбсайт юм. Жишээ нь: myfile.txt, myfile2.txt, myfile_final.txt гэх мэтээр өөрчлөлтэй хадгалахгүй ээ л гэсэн үг хаха.
3. **Github runner & yml** - runner нь бол yml файлд бичигдсэн зааврыг дагуу кодыг ажиллуулдаг хэрэгсэл гэсэн үг.

#### Үндсэн зарчмын хувьд 
1. Google cloud console - н тусламжтай нууц түлхүүрээ үүсгэнэ.
2. Github руу кодоо буюу python кодоо хуулна.
3. yml файлаа бэлдэх буюу аль хэр давтамжтай ажиллуулахаа сонгох юм.


### 1. Set Up Google Drive API
Үндсэн зорилго нь credential.json файл татаж авах, татаж авсан файлаас CLIENT_ID, CLIENT_SECRET гэсэн утгууд авах, мөн нэгэн python script ажуллуулж REFRESH_TOKEN гаргаж авах юм.


#### Step 1: Create a Google Cloud Project

1. **Go to Google Cloud Console**:
   - Navigate to [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a New Project**:
   - Click on the project drop-down menu at the top of the page.
   - Click "New Project".
   - Enter a name for your project and click "Create".

#### Step 2: Enable the Google Drive API

1. **Navigate to the API & Services Dashboard**:
   - In the left sidebar, click on "APIs & Services" and then "Dashboard".

2. **Enable APIs and Services**:
   - Click on "Enable APIs and Services" at the top.
   - Search for "Google Drive API" and select it.
   - Click the "Enable" button.

#### Step 3: Create OAuth 2.0 Credentials

1. **Navigate to the Credentials Page**:
   - In the left sidebar, click on "APIs & Services" and then "Credentials".

2. **Create Credentials**:
   - Click on the "Create Credentials" button at the top.
   - Select "OAuth 2.0 Client IDs".

3. **Configure Consent Screen**:
   - If you haven't already configured the OAuth consent screen, you will be prompted to do so. Follow the on-screen instructions to configure it.
     - Choose "External" for user type.
     - Fill out the necessary information (e.g., App name, User support email, Developer contact information).
     - Click "Save and Continue".

4. **Create OAuth Client ID**:
   - After configuring the consent screen, select "Application type" as "Desktop app" (or "Web application" if you are deploying to a server).
   - Provide a name for the OAuth 2.0 client.
   - Click "Create".

5. **Download `credentials.json`**:
   - Once the OAuth 2.0 client ID is created, you will see a dialog with the client ID and client secret.
   - Click the "Download" button to download the `credentials.json` file. (яг үнэндээ файлын чинь нэр client_secret_bla_bla_bla.json байгаа тэрнийг credentials.json нэрээр хадгалаарай.)
   - Save this file securely as it contains sensitive information.

#### Step 4: Obtain a Refresh Token --- !!!!! SKIP it until run on local

To use the Google Drive API without user interaction every time, you need to generate a refresh token:

1. **Install Google Auth Library**:
   ```sh
   pip install google-auth google-auth-oauthlib google-auth-httplib2
   ```

2. **Generate the Refresh Token**:
   - run generate_refresh_token.py script

3. **Run the Script**:
   - Execute the script in your terminal or command prompt.
   - Follow the instructions in the browser window that opens to authorize access.
   - After authorization, the script will print the refresh token. Note it down.

#### Step 5: Store Secrets in GitHub --- !!!!! SKIP it until run on local

Эхлээд github.com дээр account үүсгээд нэг repository буюу төсөл/фолдер үүсгэнэ.
1. **Go to Your GitHub Repository**:
   - Navigate to `Settings > Secrets and variables > Actions`.

2. **Add the Following Secrets**:
   - `CLIENT_ID`: Copy from `credentials.json`.
   - `CLIENT_SECRET`: Copy from `credentials.json`.
   - `REFRESH_TOKEN`: The refresh token generated from the script.

#### Step 6: Create the GitHub Action Workflow --- !!!!! SKIP it until run on local

1. **Create a Workflow File**:
   - In your GitHub repository, create a directory called `.github/workflows`.
   - Inside this directory, create a file called `write_to_drive.yml`.

2. **Add the Following Content to the Workflow File**:

scheduler.yml нь 2 цаг тутам
blank.yml push хийх тутам ажиллах ёстой.




### ЖИЧ!!! 4, 5, 6-алхмыг хийхээс өмнө кодоо local дээр буюу өөрийн компьютер дээр ажиллаж байгаа эсэхийг шалгана. Үүний тулд энэ кодыг/repository-г татаж аваад (SUBLIME MERGE гээд програм ашиглавал амар - file->clone repository гэдгээр татаад аваарай) Pycharm дээрээ нээгээд write_to_file.py-г ажиллуулаад үзнэ. Local дээр ажиллуулахад


Миний бичсэн кодыг ажиллуулах
1. Repository татаж авах Sublime merge -> File -> Clone repository -> Source url (https://github.com/Serchmaa/repositoryforjavzaa), Destination path (хүссэн фолдероо зааж өгнө) -> CLONE
2. Өнөөх фолдерт чинь repositoryforjavzaa фолдер үүссэн байгаа. Үүнийг pycharm -> open гээд нээнэ.
3. Install dependencies (pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client)
4. credentials.json файлаа repositoryforjavzaa  фолдерт хуулаарай.
5. Алгассан step 4 дээрх generate_refresh_token.py-г ажиллууж REFRESH_TOKEN-ийн утгыг авна. Өмнө нь бичсэнчлэн env.txt файлд 
6. **env.txt** файл үүсгээд өнөөх 3 хувьсагчдаа утгыг нь өгнө. Жишээ нь миний env.txt файл дараах агуулгатай. Утгыг нь өөрийнхөө утгаар сольж бичнэ гэсэн үг. CLIENT_ID, CLIENT_SECRET-ийн утгыг credentials.json файлаасаа харна.
```bash
    CLIENT_ID="503737474545blalblalallb.apps.googleusercontent.com"
    CLIENT_SECRET="GOCSPX-blablabla-blablabla"
    REFRESH_TOKEN="1//09e71ybOWO_blablabla-blablabla-blablabla"
```
7. Одоо **write_to_file.py**-г ажиллуулахад алдаа гарахгүй байх ёстой. Алдаа гарч байвал аль нэг алхмыг буруу хийсэн эсвэл фолдерийг id-г солих файлын нэр солих гэх мэтээр засна. Github scheduler ажиллуулахаас өмнө чиний том буюу жинхэнэ ipynb кодоо python болгооод local дээрээ ажиллуулаад дараа github руу хуулж хэдэн цаг тутам ажиллуулах тохиргоогоо хийнэ гэсэн үг. Гэхдээ!!! google drive руу colab-с биш гаднаас хандаж байгаа тул маш үнэхээр удаан уншиж байна. Тиймээс чиний хуучин 2 цаг ажилладаг код өдөржин ажиллах магадлалтай тул энэ маш удаан бараг бүтэл муутай санаа байх магадлалтай байна.

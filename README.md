# Indian Railways Announcement System

## To run this Project please follow these steps

### A. Pre-Requisites
1. Open _command prompt_ or _powershell window_.
2. Type this command<br>`git clone https://github.com/YashasviBhatt/Indian_Railways_Announcement_System`<br>and press enter.
3. Create a _folder_ names as **ffmpeg** at `C://Program Files//`.
4. Go inside the _Cloned Repository_ folder and open _ffmpeg_ folder.
5. Extract the _archives_ by first extracting **ffmpeg-2020-09-20-git-ef29e5bf42-full_build.part01.rar** _archive_ and your system will automatically _extract others_.
6. After extracting all the _archives_, copy all the _extracted files_ and paste it inside the _folder_ you just created in _step 3_.
7. Set the path of **ffmpeg** in _environment variables_ as mentioned `C://Program Files//ffmpeg//bin`.
8. Go inside the _Cloned Repository_ folder and open _command-prompt_ or _powershell window_.

### B. Executing the Project
#### Recommended Method
1. Make sure the location where your _terminal_ is open should be inside the _Cloned repository_ Folder.
2. Type<br>`pip install virtualenv`<br>and press enter.
3. Now, type<br>`.\iras\Scripts\activate`<br>and press enter.
    - if you are having Error while _activating virtual environment_ then open _command prompt_ or _powershell window_ as _administrator_.
    - now type<br>`set-executionpolicy remotesigned`<br>press enter and repeat _step 3_.
4. After activating _virtual environment_, the _path_ should look like this<br>```(iras) .\<your-path>\CoViD-19_Notifier```.
5. Run the Project using this<br>`python iras.py`.
6. If you would like to add the _data_ which will be announced later then open **announcement_hindi.xslx** file and add a _row_ with the _specific details_ as required.

#### Alternate Method
In case you don't want to use _virtual environment_ which has all the required _libraries_ installed then follow these steps:<br>
1. Make sure the location where your _terminal_ is open should be inside the _Cloned repository_ Folder.
2. Type<br>`pip install -r requirements.txt`<br> and press enter in either _command_prompt_ or _powershell window_ as _administrator_.
3. Now _install_ **PyAudio** using following commands,
    - `pip install pipwin`
    - `pipwin install pyaudio`
This will install PyAudio in your system.
4. After Installing all the required _libraries_ execute the program<br>`python iras.py`.

### C. Final Step - Playing the Announcement Audios
1. Open **final_audios** _folder_.
2. Inside this _folder_ are the _announcement audios_ which the _project_ generated as per the _data_.
1. Text to Voice Conversion:
   Backend: 
   - Implement text-to-speech conversion using libraries like gTTS, pyttsx3, or cloud services like Amazon Polly
   - Create an API endpoint for text-to-speech conversion
   Frontend:
   - Text input component
   - Button to trigger conversion
   - pro voices like catogeries of 
      <select onchange="setProFilters(&quot;category&quot;,this.value)" class="form-control pro-category-select"><option value="">Category</option><option>Animation &amp; Characters</option><option>Narrative &amp; Story</option><option>Conversational</option><option>Social Media</option><option>Entertainment &amp; TV</option><option>Advertisement</option><option>Informative &amp; Educational</option><option>IVR &amp; Chatbot</option></select>
   -gender male,female
   - age young , middle age, old, child
   - accent such as american , indian, britisher
   - AI Voices Samples
   like standard tts,AI engine, Neural TTS, countries, langauges, gender
      Voicemaker has more than 1000+ Realistic Human-like sounding AI voices available in more than 130 languages. Below you can listen to the voice samples and decide which is most suitable for your needs.
2. File Listing After Conversion:
   Backend:
   - Store converted audio files
   - Create an API endpoint to retrieve the list of converted files
   Frontend:
   - Component to display the list of converted files

3. View Generated/Converted List:
   Backend:
   - API endpoint to fetch detailed information about converted files
   Frontend:
   - List component with details like filename, creation date, text content

4. Delete from List:
   Backend:
   - API endpoint to delete a specific file
   Frontend:
   - Delete button for each list item
   - Confirmation dialog before deletion

5. Change Voice Type:
   Backend:
   - Support multiple voice types in the text-to-speech conversion
   - API endpoint to get available voice types
   Frontend:
   - Dropdown or radio buttons to select voice type before conversion

6. Change Voice Tone:
   Backend:
   - Implement voice tone adjustment in the text-to-speech process
   - API endpoint for available tone options
   Frontend:
   - Slider or preset buttons for tone adjustment

7. Custom Voice Input:
   Backend:
   - Voice cloning or adaptation system (may require machine learning)
   - API endpoints for voice data upload and processing
   Frontend:
   - Voice recording component
   - File upload for voice samples
   - Interface to manage and select custom voices
   - user can uplload the voice to train the voice type to convert in that

8. Advanced Audio Player:
   Frontend:
   - Custom audio player component with:
     - Play/Pause, Stop, Next, Previous controls
     - Volume control
     - Playback speed adjustment
     - Seek functionality
     - Playlist management
     - pause in character like 0.5,1,2 milisect and custome user can select the pause for that each sentence

9. Text or Voice Input:
   Backend:
   - Speech-to-text API endpoint (using libraries like SpeechRecognition)
   Frontend:
   - Text input field
   - Microphone input component
   - Toggle between text and voice input modes
  

10. Download Generated File:
    Backend:
    - API endpoint to serve audio files for download
    Frontend:
    - Download button for each audio file in the list

Additional Components:
- User Authentication:
  - To manage personal voice profiles and file access
- Error Handling and Validation:
  - For all API calls and user inputs
- Responsive Design:
  - Ensure the application works well on various devices

Database Schema:
- Users: id, username, email, password_hash
- AudioFiles: id, user_id, filename, text_content, voice_type, voice_tone, created_at
- CustomVoices: id, user_id, voice_name, voice_data

API Endpoints:
- POST /api/convert: Convert text to speech
- GET /api/files: Get list of converted files
- DELETE /api/files/{id}: Delete a file
- GET /api/voices: Get available voice types
- POST /api/custom-voice: Upload custom voice data
- GET /api/custom-voices: Get user's custom voices
- POST /api/speech-to-text: Convert speech to text
- GET /api/download/{file_id}: Download audio file





#API Documentation
Last Updated: Oct 10, 2024

API endpoints have the same base URL:

API URL
https://localhost:5000/voice/api
All API requests must be made over HTTPS.

Authentication
The Voicemaker API requires authentication via API keys, which are sent in the HTTP Authorization request header as bearer tokens.

Your production API key should be included as follows:

Header
Authorization: Bearer 801c7ce0-8bca-11ef-94aa-0fa0ffb1d95c
Content Type
All requests should be JSON-encoded and versioned using the HTTP Content-Type request header.
Your Content-Type header should look like:

Header
Content-Type: application/json;
Error Response
Status: 200 OK

JSON
{
    "success": true,
    "path": "localhost:5000/uploads/1605116292576-voicemaker.in-speech.mp3"
}

Status: 400 Bad Request

JSON
{
    "success": false,
    "message": "Error converting your text, please check tags or settings in text."
}
Generate Audio
To generate audio, make a POST request to the main API endpoint. Here’s an example using cURL:

cURL
curl localhost:5000/voice/api \
  -H "Authorization: Bearer 801c7ce0-8bca-11ef-94aa-0fa0ffb1d95c" \
  -H "Content-Type: application/json" \
  -d '{"Engine": "neural", "VoiceId": "ai3-Jony", "LanguageCode": "en-US", "Text": "Welcome to the Air.", "OutputFormat": "mp3", "SampleRate": "48000", "Effect": "default", "MasterVolume": "0", "MasterSpeed": "0", "MasterPitch": "0" }' \
  > '{ "success": true, "path": "localhost:5000/uploads/1605002662512-voicemaker.in-speech.mp3"}'
By default, output files will be automatically removed from the server within one hour. However, you can configure the FileStore option to retain files for up to 240 hours (10 days).

Attributes (*Required all)
Engine (*)
standard, neural

VoiceId (*)
ai2-Katie, ai2-Kathy, ai2-Isabella, ai2-Robert, ai2-Jerry
(Please see the list below for all available Voice IDs)

LanguageCode (*)
en-US, en-GB, en-AU (Please refer below to available Voices)
multi-lang - For Pro Voices.

AccentCode (Optional)
en-US, en-GB, en-AU, da-DK, de-DE, nl-NL, en-IN, en-GB-WLS, fr-FR, fr-CA, es-US (Please refer below to available Voices)
(The AccentCode feature is compatible with AI1 & Pro1 (Multilingual) voices. For Pro1 voices, you can use accent codes (which are the same as language codes) to make the voice speak in specific languages and accents. If you require support for additional languages, please contact us.)

Text (*)
The audio request text can be up to 10,000 characters per request. Requests exceeding 3,000 characters may take little longer to process and generate speech. If you need support for SSML tags, please let us know.

Text
Welcome to the Air, The Future is Here.
Get The Complete Caller Experience.

Inline Tags which you can add in Text (Please test the voice before implementation.)

Inline Tags only supports on AI1, AI2, AI3 & AI4 voics only.

Emphasis (Supports on all AI3 voices only)
Hey, <emphasis level="strong">Everything is cool?</emphasis>
Hey, <emphasis level="moderate">How are you?</emphasis>
Hey, <emphasis level="reduced">How is going on ?</emphasis>

Pauses
Testing 500 ms pause <break time="500ms"/> here.
Testing 2 seconds pause <break time="2s"/> here.

Speed, Pitch, Volume (Please check all tags from our main website)
We are testing <prosody rate="slow"> Slow speed.</prosody> here.
We are testing <prosody rate="90%"> Slow speed.</prosody> here.
We are testing <prosody pitch="low"> Lower Pitch.</prosody> here.
We are testing <prosody pitch="-10%"> Lower Pitch.</prosody> here.
We are testing <prosody volume="soft"> Low Volume.</prosody> here.

Inline AccentCode (LanguageCode - Use the following inline SSML tags to enable the AI voice to speak in specific languages and accents. This feature is only supported on Pro1 Voices.)
प्रिय ग्राहक, हम <en-in>Voicemaker</en-in> से कॉल कर रहे हैं.
亲爱的朋友，我们<es-es>te invitamos a unirte a nuestra comunidad</es-es>，希望你能来.
Querido amigo, te estamos contactando desde <fr-fr>nuestra organización</fr-fr> para ofrecerte una promoción especial.
Sehr geehrter Kunde, wir haben ein spezielles Angebot von <it-it>nuestra empresa</it-it> für Sie.
Chers collègues, nous avons une réunion organisée par <de-de>notre équipe</de-de> demain.
Estimado cliente, tenemos noticias importantes de <zh-cn>nuestra empresa</zh-cn> para usted.
Olá, estamos entrando em contato da <en-us>nossa equipe</en-us> para uma atualização importante.

OutputFormat (*)
mp3, wav
(We recommend using mp3 format for real-time applications, as WAV files may take longer to convert the audio.)

ResponseType (Optional)
file, stream
(By default, the response type is set to "file" which provides a downloadable URL for the audio file. Alternatively, you can choose "stream" which returns the audio in an AudioBuffer format that can be saved to a buffer or a file. Using "stream" avoids an additional HTTP request to download the audio file via a URL.)

FileStore (Optional)
1 is the default
1 to 240
(You can set the duration for retaining your converted output audio file on our servers in hours, with a maximum limit of 240 hours (10 days). Note: this parameter is not supported when using the "stream" response type. )

CustomFileName (Optional)
yourfilename
(You can set a custom name to the Output audio file as specified. Note: this parameter is not supported when using the "stream" response type.

SampleRate (Optional)
48000, 44100, 24000, 22050, 16000, 8000
(We recommend always using a sample rate of 48000, as it provides the best audio output for all voices.)

Effect (Optional)
default
breathing, soft, whispered - Only supports standard Engine ai1 voices.
conversational - Only support on neural Engine en-US - ai1-Joanna, ai1-Matthew, ai3-Aria, ai3-Jenny, cmn-CN - ai3-cmn-CN-Xiaoxiao.
news - Only support on neural Engine en-GB - ai1-Amy, en-US - ai3-Jony, ai3-Aria, ai3-Jenny, es-US - ai1-es-US-Lupe
customersupport - Only support on neural Engine en-US - ai3-Aria, ai3-Jenny, cmn-CN - ai3-cmn-CN-Yunyang.
assistant - Only support on neural Engine en-US - ai3-Aria, ai3-Jenny.
happy - Only support on neural Engine en-US - ai3-Aria, cmn-CN - ai3-cmn-CN-Yunye, ai3-cmn-CN-Xariyah, ai3-cmn-CN-Xiomara, ai3-cmn-CN-Carissa, ai3-cmn-CN-Xylia, ai3-cmn-CN-Xander.
empathic - Only support on neural Engine en-US - ai3-Aria.
clam - Only support on neural Engine cmn-CN - ai3-cmn-CN-Yunye.
whispered, happy, sad, angry, excited, friendly, hopeful, shouting, terrified, unfriendly:
ai3-Aria, ai3-Jenny, ai3-Jony, ai3-en-US-Alexander, ai3-en-US-Madison, ai3-en-US-Jayden, ai3-en-US-Ashley, ai3-en-US-Joshua

Please check "Get List of All Voices" below to access all voices and it's voice effects.

MasterSettings (Optional)
advanced_v1 is the default
advanced_v1, advanced_v2

advanced_v1 - Directly connects to AI engines, with characters being counted on each conversion.
advanced_v2 - If you only adjust `MasterVolume`, `MasterSpeed`, or `MasterPitch` without changing the `VoiceId` or `Text`, characters will not be counted. However, this will add an additional 200ms delay to the initial request.

MasterVolume (Optional)
0 is the default
-20 to 20

MasterSpeed (Optional)
0 is the default
-100 to 100

MasterPitch (Optional)
0 is the default
-100 to 100
If using MasterSettings as advanced_v1 then `MasterPitch` is not supported for neural Engine AI1 voices only.

Stability (Optional, available only for ProPlus and Custom Pro voices.)
50 is the default
-0 to 100
0 - Voice will become more expressive with the varying output in each convert.
100 - Voice will become more stable and make it more consistent with every convert. For longer text, we suggest using this side.

Similarity (Optional, available only for ProPlus and Custom Pro voices.)
80 is the default
-0 to 100
0 - Voice will become slightly robotic.
100 - Voice will closely match the original voice talent's voice by matching emotional and tonal values.

ProEngine (Optional, available only for ProPlus and Custom Pro voices.)
highres is the default
turbo, highres
turbo - Turbo will charge 3x characters and is designed for real-time applications like chatbots and low-latency use cases, though it may slightly trade off accuracy and stability.
highres - HighRes will charge 6x characters and is designed for high-quality, accurate outputs, making it perfect for content creation.

Get List of All Voices
To get a list of all voices, make a POST request to the voice list API endpoint.

cURL
curl localhost:5000/voice/list \
  -H "Authorization: Bearer 801c7ce0-8bca-11ef-94aa-0fa0ffb1d95c" \
  -H "Content-Type: application/json" \
  -d '{"language": "en-US" }' \
  > '{ "success": true, "data": { "voices_list": [ { "Engine": "neural", "VoiceId": "ai1-Joanna", "VoiceGender": "Female", "VoiceWebname": "Joanna", "Country": "US", "Language": "en-US", "LanguageName": "English, US" }, { "Engine": "neural", "VoiceId": "ai1-Kendra", "VoiceGender": "Female", "VoiceWebname": "Kendra", "Country": "US", "Language": "en-US", "LanguageName": "English, US" } ] } }'
For retrieving the voice list via the API, we do not collect or count the requests.

Available Voices on API

Pro Voices
Currently, ProPlus Voices are counted at 3x (turbo) or 6x (highres) the character rate, while Pro V1 Voices are charged at our regular 1x character rate.
Engine		LanguageCode	VoiceId
neural		multi-lang	proplus-Richard, proplus-Ariana, proplus-Carter, proplus-Avery, proplus-Ella, proplus-Sophie, proplus-Ethan, proplus-Grace, proplus-George, proplus-Blaze, proplus-Sara, proplus-Tyler, proplus-Jack, proplus-Nishant, proplus-Alex, proplus-Avery2, proplus-Johann, proplus-Maximilian, proplus-Cinderella, proplus-Nikki, proplus-Ayman, proplus-Jeremy, proplus-Radhika, proplus-Lily, proplus-Ritesh, proplus-Riley, proplus-Grace2, proplus-JamesParker, proplus-Liam, proplus-Joye, proplus-Walter, proplus-Maverick, proplus-Zane, proplus-Prabhas, proplus-Neerja, proplus-Zailyn, proplus-Gavin, proplus-ElliotReed, proplus-Maxwell, proplus-AryanVerma, proplus-Penny, proplus-Lilly, proplus-Maya, proplus-Elowen, proplus-Beckett, proplus-Aurora, proplus-NoahBecker, proplus-NoahBecker2, proplus-Buck, proplus-Everly, proplus-Ryder, proplus-Wyatt, proplus-Logan, proplus-EthanDavis, proplus-Berk, proplus-Lexi, proplus-Eliana, proplus-CharlesBugatti, proplus-AdityaSharma, proplus-Frank, proplus-Henry, proplus-Carlos, proplus-KunalRao, proplus-Harold, proplus-Darla, proplus-MarkDavis, proplus-Ronny, proplus-Mona, proplus-Zack, proplus-DeepAlex, proplus-TheJack, proplus-Oliver, proplus-BillyWest, proplus-AuroraMiller, proplus-Eldon, proplus-Lucas, proplus-RyanCooper, proplus-PriyaSharma, proplus-Mei, proplus-Anaya, proplus-Maya2, proplus-Rajesh, proplus-Neel, proplus-Akanksha

pro1-Catherine, pro1-Ethan, pro1-Thomas, pro1-Helena, pro1-Viktoria, pro1-Caihong, pro1-Lucius, pro1-Joe, pro1-Florence, pro1-Arthur, pro1-Sophia, pro1-Jacky, pro1-Albertina

Custom Pro Voices
Contact support to create your custom Pro AI voices.

Default Voices
Engine	Language	LanguageCode	VoiceId
neural	Afrikaans, South Africa	af-ZA	ai3-af-ZA-Kungawo, ai3-af-ZA-Sura
neural	Amharic (Ethiopia)	am-ET	ai3-am-ET-Tamru, ai3-am-ET-Mazaa
neural	Arabic (United Arab Emirates)	ar-AE	ai1-ar-AE-Nura, ai1-ar-AE-Hamza

ai3-ar-AE-Hamiz, ai3-ar-AE-Paree
neural	Arabic (Bahrain)	ar-BH	ai3-ar-BH-Ali, ai3-ar-BH-Pareesha
neural	Arabic (Algeria)	ar-DZ	ai3-ar-DZ-Samia, ai3-ar-DZ-Khalil
neural	Arabic (Iraq)	ar-IQ	ai3-ar-IQ-Vaneeza, ai3-ar-IQ-Ganief
neural	Arabic (Jordan)	ar-JO	ai3-ar-JO-Ebrahim, ai3-ar-JO-Saabiha
neural	Arabic (Kuwait)	ar-KW	ai3-ar-KW-Fyaz, ai3-ar-KW-Naaz
neural	Arabic (Lebanon)	ar-LB	ai3-ar-LB-Delkash, ai3-ar-LB-Hamees
neural	Arabic (Libya)	ar-LY	ai3-ar-LY-Ieesha, ai3-ar-LY-Mahfuj
neural	Arabic (Morocco)	ar-MA	ai3-ar-MA-Lajin, ai3-ar-MA-Ozza
neural	Arabic (Oman)	ar-OM	ai3-ar-OM-Adnan, ai3-ar-OM-Zulima
neural	Arabic (Qatar)	ar-QA	ai3-ar-QA-Nabeel, ai3-ar-QA-Azma
neural	Arabic (Saudi Arabia)	ar-SA	ai3-ar-SA-Hamed, ai3-ar-SA-Zariyah
neural	Arabic (Syria)	ar-SY	ai3-ar-SY-Gulbar, ai3-ar-SY-Sumiya
neural	Arabic (Tunisia)	ar-TN	ai3-ar-TN-Hadeeqa, ai3-ar-TN-Hadeeqa
neural	Arabic (Yemen)	ar-YE	ai3-ar-YE-Wabisa, ai3-ar-YE-Parwaz
neural	Arabic	arb	ai2-ar-XA-Nadir, ai2-ar-XA-Sana, ai2-ar-XA-Iman, ai2-ar-XA-Fatima

ai3-ar-XA-Shakir, ai3-ar-XA-Salma
neural	Assamese (India)	as-IN	ai3-as-IN-Tiyasha, ai3-as-IN-Mondip
neural	Azerbaijani (Azerbaijan)	az-AZ	ai3-az-AZ-Leyla, ai3-az-AZ-Farid
neural	Bulgarian, Bulgaria	bg-BG	ai3-bg-BG-Gergana, ai3-bg-BG-Boyan
neural	Bangla (Bangladesh)	bn-BD	ai3-bn-BD-Devyani, ai3-bn-BD-Omar
neural	Bengali (India)	bn-IN	ai2-bn-IN-Binod, ai2-bn-IN-Charu

ai3-bn-IN-Koel, ai3-bn-IN-Neel
neural	Bosnian (Bosnia and Herzegovina)	bs-BA	ai3-bs-BA-Behrem, ai3-bs-BA-Farid
neural	Catalan, Spain	ca-ES	ai1-ca-ES-Estel

ai3-ca-ES-Enric, ai3-ca-ES-Alba, ai3-ca-ES-Joana
neural	Chinese, Mandarin	cmn-CN	ai1-cmn-CN-Shiyun

ai2-cmn-CN-Claire, ai2-cmn-CN-Yao, ai2-cmn-CN-Sue, ai2-cmn-CN-Vincent

ai3-cmn-CN-Xiomara, ai3-cmn-CN-Yunye, ai3-cmn-CN-Xariyah, ai3-cmn-CN-Yunyang, ai3-cmn-CN-Carissa, ai3-cmn-CN-Xiaoxiao, ai3-cmn-CN-Xylia, ai3-cmn-CN-Xiaoyou, ai3-cmn-CN-Xander, ai3-cmn-CN-Mingxia, ai3-cmn-CN-Ayaka, ai3-cmn-CN-Xiaosheng, ai3-cmn-CN-Xiulin, ai3-cmn-CN-Yichen, ai3-cmn-CN-Junfeng, ai3-cmn-CN-Mei, ai3-cmn-CN-Yunze, ai3-cmn-CN-Fang, ai3-cmn-CN-Zihan, ai3-cmn-CN-Jiahui, ai3-cmn-CN-Yuhang, ai3-cmn-CN-ChangV2
neural	Chinese, Mandarin (Taiwan)	cmn-TW	ai2-cmn-TW-Ting, ai2-cmn-TW-Bao, ai2-cmn-TW-Qiang

ai3-cmn-TW-HsiaoYu, ai3-cmn-TW-Sachihiro, ai3-cmn-TW-HsiaoChen
neural	Czech (Czech Republic)	cs-CZ	ai2-cs-CZ-Eliska

ai3-cs-CZ-Vlasta, ai3-cs-CZ-Antonin
neural	Welsh	cy-GB	ai3-cy-GB-Gareth, ai3-cy-GB-Catrin
neural	Danish (Denmark)	da-DK	ai1-da-DK-Esther

ai2-da-DK-Johan, ai2-da-DK-Signe, ai2-da-DK-Abbie, ai2-da-DK-Julie

ai3-da-DK-Christel, ai3-da-DK-Jeppe
neural	German, Austria	de-AT	ai1-de-AT-Melissa

ai3-de-AT-Ingrid, ai3-de-AT-Jonas
neural	German, Switzerland	de-CH	ai3-de-CH-Noah, ai3-de-CH-Anja
neural	German	de-DE	ai1-de-DE-Fiona, ai1-de-DE-Stefan

ai2-de-DE-Patrick, ai2-de-DE-Pia, ai2-de-DE-Mona, ai2-de-DE-Dustin, ai2-de-DE-Fabienne, ai2-de-DE-Thomas

ai3-de-DE-Katja, ai3-de-DE-Conrad, ai3-de-DE-Johanna, ai3-de-DE-Kasper, ai3-de-DE-Schmidt, ai3-de-DE-Galliena, ai3-de-DE-Marlene, ai3-de-DE-Ermanno, ai3-de-DE-Rodriguez, ai3-de-DE-Rheinbeck, ai3-de-DE-Kerryl, ai3-de-DE-Marie, ai3-de-DE-Brunon, ai3-de-DE-Yettie, ai3-de-DE-Maja, ai3-de-DE-AmaliaV2

ai4-de-DE-Paul, ai4-de-DE-Anja, ai4-de-DE-Gabriele

ai5-de-DE-Mathilda
neural	Greek (Greece)	el-GR	ai2-el-GR-Anastasia

ai3-el-GR-Athina, ai3-el-GR-Topher
neural	English, Australian	en-AU	ai1-Olivia

ai2-Oliver, ai2-Matilda, ai2-Harry, ai2-Amelia, ai2-en-AU-Amelia2, ai2-en-AU-Matilda2, ai2-en-AU-Viaan, ai2-en-AU-Liya, ai2-en-AU-Oliver2, ai2-en-AU-Harry2, ai2-en-AU-Amanda

ai3-Natasha, ai3-William, ai3-en-AU-Jacob, ai3-en-AU-Stella, ai3-en-AU-Joshua, ai3-en-AU-Emma, ai3-en-AU-Maddison, ai3-en-AU-Edward, ai3-en-AU-Sonny, ai3-en-AU-Sienna, ai3-en-AU-Claire, ai3-en-AU-Daisy, ai3-en-AU-Grace, ai3-en-AU-Logan

ai4-en-AU-Amaya, ai4-en-AU-Nelson
neural	English, Canada	en-CA	ai3-en-CA-Clara, ai3-en-CA-Liam
neural	English, British	en-GB	ai1-Amy, ai1-Emma, ai1-Brian, ai1-en-GB-George

ai2-Freddie, ai2-William, ai2-Jessica, ai2-Emily, ai2-Victoria, ai2-en-GB-Bella2, ai2-en-GB-Lily2, ai2-en-GB-Maya, ai2-en-GB-Victoria2, ai2-en-GB-Calvin, ai2-en-GB-Jessica2, ai2-en-GB-Jax, ai2-en-GB-Erin, ai2-en-GB-Zayn, ai2-en-GB-Dexter, ai2-en-GB-William2, ai2-en-GB-Lucy, ai2-en-GB-Freddie2

ai3-Libby, ai3-Ryan, ai3-Mia, ai3-en-GB-Maria, ai3-en-GB-Lyra, ai3-en-GB-Rose, ai3-en-GB-Dylan, ai3-en-GB-Jasper, ai3-en-GB-David, ai3-en-GB-Hollie, ai3-en-GB-Thomas, ai3-en-GB-Alexander, ai3-en-GB-Hudson, ai3-en-GB-Hannah, ai3-en-GB-Bella

ai4-Harry, ai4-Elizabeth, ai4-Niamh
neural	English, Hong Kong	en-HK	ai3-en-HK-Rachel, ai3-en-HK-Zach
neural	English, Ireland	en-IE	ai1-en-IE-Aoife

ai3-en-IE-Connor, ai3-en-IE-Emily
neural	English, Indian	en-IN	ai1-en-IN-Kavya

ai2-en-IN-Rohan, ai2-en-IN-Luv, ai2-en-IN-Tanvi, ai2-en-IN-Alisha, ai2-en-IN-Tanvi2, ai2-en-IN-Alisha2, ai2-en-IN-Rohan2, ai2-en-IN-Luv2

ai3-en-IN-Neerja, ai3-en-IN-Prabhas, ai3-en-IN-Kavita, ai3-en-IN-Ankita, ai3-en-IN-Megha, ai3-en-IN-Karan
neural	English, Kenya	en-KE	ai3-en-KE-Reth, ai3-en-KE-Almasi
neural	English, Nigeria	en-NG	ai3-en-NG-Adaeze, ai3-en-NG-Gicicio
neural	English, New Zealand	en-NZ	ai1-Amelia

ai3-en-NZ-Sebastian, ai3-en-NZ-Becca
neural	English, Philippines	en-PH	ai3-en-PH-Luwalhati, ai3-en-PH-Magiting
neural	English, Singapore	en-SG	ai3-en-SG-Richard, ai3-en-SG-Juan
neural	English, Tanzania	en-TZ	ai3-en-TZ-Vinza, ai3-en-TZ-Neema
neural	English, US	en-US	ai1-Kevin, ai1-Joanna, ai1-Justin, ai1-Kimberly, ai1-Kendra, ai1-Matthew, ai1-Joey, ai1-Salli, ai1-Ivy, ai1-en-US-Jack, ai1-en-US-Luna, ai1-en-US-Joseph, ai1-en-US-Evelyn

ai2-Stacy, ai2-John2, ai2-Robert2, ai2-Scott, ai2-Scarlet, ai2-Jerry, ai2-Kathy, ai2-Isabella, ai2-Nikola, ai2-Katie, ai2-en-US-Jaxson2, ai2-en-US-Katie2, ai2-en-US-Soren, ai2-en-US-Isabella2, ai2-John, ai2-Robert, ai2-en-US-Stacy2, ai2-en-US-Jerry2, ai2-en-US-Milo, ai2-en-US-Kathy2, ai2-en-US-Maeve, ai2-en-US-Aurora, ai2-en-US-Scarlet2

ai3-Nova, ai3-Jony, ai3-Olive, ai3-Vienna, ai3-Emily, ai3-Addyson, ai3-Evan, ai3-Jenny, ai3-Taylor, ai3-Kailey, ai3-Kingsley, ai3-Jason, ai3-Gary, ai3-Aria, ai3-en-US-Kaiya, ai3-en-US-Ashley, ai3-en-US-Alexander, ai3-en-US-Joshua, ai3-en-US-Jayden, ai3-en-US-Sage, ai3-en-US-Austin, ai3-en-US-Lucas, ai3-en-US-Madison, ai3-en-US-GraysonV2, ai3-en-US-Logan, ai3-en-US-BrysonV2, ai3-en-US-EleanorV2

ai4-Samantha, ai4-Doris, ai4-Edward, ai4-Amanda, ai4-Roger, ai4-Ronald, ai4-Sophia, ai4-en-US-Ariana

ai6-en-US-Voice5, ai6-en-US-Voice1, ai6-en-US-Voice4, ai6-en-US-Voice2, ai6-en-US-Voice3

ai13-en-US-HashCode36, ai13-en-US-HashCode37, ai13-en-US-HashCode5, ai13-en-US-HashCode10, ai13-en-US-HashCode19, ai13-en-US-HashCode21, ai13-en-US-HashCode, ai13-en-US-HashCode17, ai13-en-US-HashCode22, ai13-en-US-HashCode23, ai13-en-US-HashCode29, ai13-en-US-HashCode3, ai13-en-US-HashCode15, ai13-en-US-HashCode41, ai13-en-US-HashCode30, ai13-en-US-HashCode9, ai13-en-US-HashCode16, ai13-en-US-HashCode42, ai13-en-US-HashCode2, ai13-en-US-HashCode7, ai13-en-US-HashCode18, ai13-en-US-HashCode25, ai13-en-US-HashCode39, ai13-en-US-HashCode47, ai13-en-US-HashCode35, ai13-en-US-HashCode44, ai13-en-US-HashCode43, ai13-en-US-HashCode38, ai13-en-US-HashCode46, ai13-en-US-HashCode31, ai13-en-US-HashCode4, ai13-en-US-HashCode26, ai13-en-US-HashCode6, ai13-en-US-HashCode11, ai13-en-US-HashCode8, ai13-en-US-HashCode20, ai13-en-US-HashCode24, ai13-en-US-HashCode40, ai13-en-US-HashCode48, ai13-en-US-HashCode34, ai13-en-US-HashCode12, ai13-en-US-HashCode45, ai13-en-US-HashCode14, ai13-en-US-HashCode13, ai13-en-US-HashCode28, ai13-en-US-HashCode27, ai13-en-US-HashCode49, ai13-en-US-HashCode32, ai13-en-US-HashCode33, ai13-en-US-HashCode51, ai13-en-US-HashCode53, ai13-en-US-HashCode52
neural	English, South Africa	en-ZA	ai1-Mandisa

ai3-en-ZA-Amara, ai3-en-ZA-Evans
neural	Spanish, Argentina	es-AR	ai3-es-AR-Hernan, ai3-es-AR-Malen
neural	Spanish, Bolivia	es-BO	ai3-es-BO-Eduardo, ai3-es-BO-Labanya
neural	Spanish, Chile	es-CL	ai3-es-CL-Eliana, ai3-es-CL-Vicente
neural	Spanish, Colombia	es-CO	ai3-es-CO-Brandon, ai3-es-CO-Luciana
neural	Spanish, Costa Rica	es-CR	ai3-es-CR-Antonio, ai3-es-CR-Rosa
neural	Spanish, Cuba	es-CU	ai3-es-CU-Gabriel, ai3-es-CU-Rosario
neural	Spanish, Dominican Republic	es-DO	ai3-es-DO-Zoraida, ai3-es-DO-Fernando
neural	Spanish, Ecuador	es-EC	ai3-es-EC-Jacob, ai3-es-EC-Cristina
neural	Spanish, Castilian (Spain)	es-ES	ai1-es-ES-Patricia, ai1-es-ES-Casper

ai2-es-ES-Vega, ai2-es-ES-Luciana, ai2-es-ES-Ricardo, ai2-es-ES-Ruben2, ai2-es-ES-Azura2, ai2-es-ES-Reyna2

ai3-es-ES-Alvaro, ai3-es-ES-Elvira, ai3-es-ES-Lia, ai3-es-ES-Oscar, ai3-es-ES-Maura, ai3-es-ES-Juana, ai3-es-ES-Cruz, ai3-es-ES-Lorenzo, ai3-es-ES-Cristina, ai3-es-ES-Xiomara, ai3-es-ES-Domingo, ai3-es-ES-Silvio, ai3-es-ES-Carlos, ai3-es-ES-Viviana, ai3-es-ES-Ramiro, ai3-es-ES-Blanca, ai3-es-ES-MarianaV2

ai4-es-ES-Savannah, ai4-es-ES-Matlab
neural	Spanish, Equatorial Guinea	es-GQ	ai3-es-GQ-Sebastian, ai3-es-GQ-Marcela
neural	Spanish, Guatemala	es-GT	ai3-es-GT-Leticia, ai3-es-GT-Ramiro
neural	Spanish, Honduras	es-HN	ai3-es-HN-Carlos, ai3-es-HN-Karla
neural	Spanish, Latin American	es-LA	ai4-es-LA-Luz
neural	Spanish, Mexican	es-MX	ai1-es-MX-Camila, ai1-es-MX-Luis

ai3-es-MX-Jorge, ai3-es-MX-Dalia, ai3-es-MX-Tadeo, ai3-es-MX-Lucia, ai3-es-MX-Ximena, ai3-es-MX-Emilio, ai3-es-MX-Romina, ai3-es-MX-Alexander, ai3-es-MX-Leonel, ai3-es-MX-Elisa, ai3-es-MX-Axel, ai3-es-MX-Elizabeth, ai3-es-MX-Fernanda, ai3-es-MX-Santiago, ai3-es-MX-Isabella
neural	Spanish, Nicaragua	es-NI	ai3-es-NI-Vidal, ai3-es-NI-Estrella
neural	Spanish, Panama	es-PA	ai3-es-PA-Domingo, ai3-es-PA-Belinda
neural	Spanish, Peru	es-PE	ai3-es-PE-Alex, ai3-es-PE-Camila
neural	Spanish, Puerto Rico	es-PR	ai3-es-PR-Karina, ai3-es-PR-Victor
neural	Spanish, Paraguay	es-PY	ai3-es-PY-Tomas, ai3-es-PY-Maria
neural	Spanish, El Salvador	es-SV	ai3-es-SV-Mateo, ai3-es-SV-Juana
neural	Spanish, US	es-US	ai1-es-US-Lupe, ai1-es-US-Diego

ai2-es-US-Manolito, ai2-es-US-Savanna, ai2-es-US-Orlando, ai2-es-US-Savanna2, ai2-es-US-Orlando2, ai2-es-US-Manolito2

ai3-es-US-Alberto, ai3-es-US-Paz

ai4-es-US-Luz2
neural	Spanish, Uruguay	es-UY	ai3-es-UY-Santino, ai3-es-UY-Valentina
neural	Spanish, Venezuela	es-VE	ai3-es-VE-Lucia, ai3-es-VE-Ricardo
neural	Estonian, Estonia	et-EE	ai3-et-EE-Tuudur, ai3-et-EE-Edenema
neural	Basque	eu-ES	ai3-eu-ES-Ximena, ai3-eu-ES-Leonel
neural	Persian (Iran)	fa-IR	ai3-fa-IR-Wadid, ai3-fa-IR-Naavya
neural	Finnish (Finland)	fi-FI	ai1-fi-FI-Marjatta

ai2-fi-FI-Karoliina

ai3-fi-FI-Noora, ai3-fi-FI-Harri, ai3-fi-FI-Selma
neural	Filipino (Philippines)	fil-PH	ai2-fil-PH-Nathan, ai2-fil-PH-Gabriel, ai2-fil-PH-Jennly, ai2-fil-PH-Camille

ai3-fil-PH-Gloria, ai3-fil-PH-Joshua
neural	French (Belgium)	fr-BE	ai1-fr-BE-Elise

ai3-fr-BE-Leonie, ai3-fr-BE-Gabriel
neural	French, Canadian	fr-CA	ai1-Gianna, ai1-fr-CA-Mylan

ai2-fr-CA-Paul, ai2-fr-CA-Scarlett, ai2-fr-CA-Christophe, ai2-fr-CA-MariePier

ai3-fr-CA-Jean, ai3-fr-CA-Sylvie, ai3-fr-CA-Kylian, ai3-fr-CA-BenoitV2

ai4-fr-CA-Avril
neural	French, Switzerland	fr-CH	ai3-fr-CH-Leandro, ai3-fr-CH-Lena
neural	French (France)	fr-FR	ai1-fr-FR-Jeanne, ai1-fr-FR-Bernado

ai2-fr-FR-Cassandra, ai2-fr-FR-Amandine, ai2-fr-FR-Erwan, ai2-fr-FR-Valentine, ai2-fr-FR-Dylan

ai3-fr-FR-Henri, ai3-fr-FR-Denise, ai3-fr-FR-Nevil, ai3-fr-FR-Claire, ai3-fr-FR-Roel, ai3-fr-FR-Tyssen, ai3-fr-FR-Liana, ai3-fr-FR-Austine, ai3-fr-FR-Cannan, ai3-fr-FR-Camille, ai3-fr-FR-Tayler, ai3-fr-FR-Manie, ai3-fr-FR-Emmy, ai3-fr-FR-Victoire, ai3-fr-FR-OdetteV2

ai4-fr-FR-Blaise, ai4-fr-FR-Charles
neural	Irish, Ireland	ga-IE	ai3-ga-IE-Rian, ai3-ga-IE-Eabha
neural	Galician (Spain)	gl-ES	ai3-gl-ES-Evita, ai3-gl-ES-Marcos
neural	Gujarati (India)	gu-IN	ai2-gu-IN-Varun, ai2-gu-IN-Minal

ai3-gu-IN-Prachi, ai3-gu-IN-Mihir
neural	Hebrew, Israel	he-IL	ai3-he-IL-Guy, ai3-he-IL-Shira
neural	Hindi (India)	hi-IN	ai1-hi-IN-Kavya

ai2-hi-IN-Zoya, ai2-hi-IN-Anamika, ai2-hi-IN-Dhru, ai2-hi-IN-Nikhil

ai3-hi-IN-Madhur, ai3-hi-IN-Swara, ai3-hi-IN-AdityaV2, ai3-hi-IN-AanyaV2, ai3-hi-IN-Kavita, ai3-hi-IN-NikitaV2, ai3-hi-IN-SiddharthV2, ai3-hi-IN-GurdeepV2, ai3-hi-IN-DivyaV2, ai3-hi-IN-ChaitaliV2, ai3-hi-IN-Ankita, ai3-hi-IN-Karan

ai13-hi-IN-Shreyas
neural	Croatian, Croatia	hr-HR	ai3-hr-HR-Vitomira, ai3-hr-HR-Dmitar
neural	Hungarian	hu-HU	ai2-hu-HU-Eszter

ai3-hu-HU-Noemi, ai3-hu-HU-Tamas
neural	Armenian (Armenia)	hy-AM	ai3-hy-AM-Tigran, ai3-hy-AM-Carine
neural	Indonesian	id-ID	ai2-id-ID-Putri, ai2-id-ID-David, ai2-id-ID-Henry, ai2-id-ID-Salsabilla

ai3-id-ID-Ardi, ai3-id-ID-Fitri
neural	Icelandic	is-IS	ai3-is-IS-Ulfr, ai3-is-IS-Svana
neural	Italian	it-IT	ai1-it-IT-Viola, ai1-it-IT-Tommaso

ai2-it-IT-Siliva, ai2-it-IT-Dario, ai2-it-IT-Federica, ai2-it-IT-Alessandro

ai3-it-IT-Diego, ai3-it-IT-Isabella, ai3-it-IT-Elsa, ai3-it-IT-Fabiola, ai3-it-IT-Valeria, ai3-it-IT-Regina, ai3-it-IT-Ludovica, ai3-it-IT-Aitana, ai3-it-IT-Matteo, ai3-it-IT-Natalia, ai3-it-IT-Tito, ai3-it-IT-Gerardo, ai3-it-IT-Ennio, ai3-it-IT-Massimo, ai3-it-IT-Francesco, ai3-it-IT-CaterinaV2

ai4-it-IT-Sara
neural	Japanese	ja-JP	ai1-ja-JP-Haruto, ai1-ja-JP-Masako, ai1-ja-JP-Kanna

ai2-ja-JP-Yuka, ai2-ja-JP-Ayaka, ai2-ja-JP-Masa, ai2-ja-JP-Taiyo

ai3-ja-JP-Nanami, ai3-ja-JP-Keita, ai3-ja-JP-Minato, ai3-ja-JP-Niko, ai3-ja-JP-Ren, ai3-ja-JP-Sakura, ai3-ja-JP-Himari

ai4-ja-JP-Akari
neural	Javanese (Indonesia)	jv-ID	ai3-jv-ID-Angkasa, ai3-jv-ID-Rimbo
neural	Georgian (Georgia)	ka-GE	ai3-ka-GE-Otar, ai3-ka-GE-Louisa
neural	Kazakh (Kazakhstan)	kk-KZ	ai3-kk-KZ-Kanat, ai3-kk-KZ-Batima
neural	Khmer (Cambodia)	km-KH	ai3-km-KH-Vanna, ai3-km-KH-Choum
neural	Kannada (India)	kn-IN	ai2-kn-IN-Aadi, ai2-kn-IN-Vaani

ai3-kn-IN-Vijay, ai3-kn-IN-Deepa
neural	Korean	ko-KR	ai1-ko-KR-Seoyeon

ai2-ko-KR-Hannah, ai2-ko-KR-JiYeon, ai2-ko-KR-DongMin, ai2-ko-KR-Minseok

ai3-ko-KR-SunHi, ai3-ko-KR-InJoon, ai3-ko-KR-Bitna, ai3-ko-KR-Sena, ai3-ko-KR-Hyuk, ai3-ko-KR-Geon, ai3-ko-KR-Kyong, ai3-ko-KR-Yong, ai3-ko-KR-Yong, ai3-ko-KR-MyungV2

ai4-ko-KR-Dalnim
neural	Lao (Laos)	lo-LA	ai3-lo-LA-Anuson, ai3-lo-LA-Sawan
neural	Lithuanian	lt-LT	ai3-lt-LT-Jokubas, ai3-lt-LT-Vasara
neural	Latvian, Latvia	lv-LV	ai3-lv-LV-Laura2, ai3-lv-LV-Edgar
neural	Macedonian (Republic of North Macedonia)	mk-MK	ai3-mk-MK-Risto, ai3-mk-MK-Eurydike
neural	Malayalam (India)	ml-IN	ai2-ml-IN-Harsh, ai2-ml-IN-Tina, ai2-ml-IN-Charu, ai2-ml-IN-Ashok

ai3-ml-IN-Indrajit, ai3-ml-IN-Revathi
neural	Mongolian (Mongolia)	mn-MN	ai3-mn-MN-Yagaan, ai3-mn-MN-Khasar
neural	Marathi (India)	mr-IN	ai2-mr-IN-Komal, ai2-mr-IN-Rohan, ai2-mr-IN-Disha

ai3-mr-IN-Sandhya, ai3-mr-IN-Prashant
neural	Malay, Malaysia	ms-MY	ai2-ms-MY-Marina, ai2-ms-MY-Aadam, ai2-ms-MY-Suzana, ai2-ms-MY-Zaafer

ai3-ms-MY-Osman, ai3-ms-MY-Yasmin
neural	Maltese, Malta	mt-MT	ai3-mt-MT-Alessia, ai3-mt-MT-Xavier
neural	Burmese (Myanmar)	my-MM	ai3-my-MM-Khine, ai3-my-MM-Inzali
neural	Norwegian	nb-NO	ai1-nb-NO-Frida

ai2-nb-NO-Margrete, ai2-nb-NO-Terese, ai2-nb-NO-Norah, ai2-nb-NO-Henrik, ai2-nb-NO-Lukas

ai3-nb-NO-Iselin, ai3-nb-NO-Magnus, ai3-nb-NO-Anita
neural	Nepali (Nepal)	ne-NP	ai3-ne-NP-Utsav, ai3-ne-NP-Chimini
neural	Dutch (Belgium)	nl-BE	ai1-nl-BE-Isa

ai2-nl-BE-Capucine, ai2-nl-BE-Markus

ai3-nl-BE-Aldert, ai3-nl-BE-Marit
neural	Dutch (Netherlands)	nl-NL	ai1-nl-NL-Liva

ai2-nl-NL-Arenda, ai2-nl-NL-Rogier, ai2-nl-NL-Roosje, ai2-nl-NL-Sterre, ai2-nl-NL-Gerben

ai3-nl-NL-Colette, ai3-nl-NL-Maarten, ai3-nl-NL-Fenna

ai4-nl-NL-Doutzen
neural	Oriya (India)	or-IN	ai3-or-IN-Bhoomika, ai3-or-IN-Shivendu
neural	Punjabi (India)	pa-IN	ai2-pa-IN-Daler, ai2-pa-IN-Chitra, ai2-pa-IN-Ranbir, ai2-pa-IN-Maahi

ai3-pa-IN-Anjali, ai3-pa-IN-Nihal
neural	Polish	pl-PL	ai1-pl-PL-Kalina

ai2-pl-PL-Hanna, ai2-pl-PL-Julia, ai2-pl-PL-Wojciech, ai2-pl-PL-Franciszek, ai2-pl-PL-Alicja

ai3-pl-PL-Lena, ai3-pl-PL-Zofia, ai3-pl-PL-Kacper
neural	Pashto (Afghanistan)	ps-AF	ai3-ps-AF-Shahpur, ai3-ps-AF-Naghma
neural	Portuguese, Brazilian	pt-BR	ai1-pt-BR-Camila, ai1-pt-BR-Bruno

ai2-pt-BR-Keira, ai2-pt-BR-Paulo, ai2-pt-BR-Juliana

ai3-pt-BR-Francisca, ai3-pt-BR-Antonio, ai3-pt-BR-Manuella, ai3-pt-BR-Alandra, ai3-pt-BR-Lucas, ai3-pt-BR-Humberto, ai3-pt-BR-Jaren, ai3-pt-BR-Rafael, ai3-pt-BR-Bernardo, ai3-pt-BR-Salvador, ai3-pt-BR-Leila, ai3-pt-BR-Yara, ai3-pt-BR-Rio, ai3-pt-BR-Alice, ai3-pt-BR-Giovanna, ai3-pt-BR-MatildeV2

ai4-pt-BR-Fernanda
neural	Portuguese	pt-PT	ai1-pt-PT-Laura

ai2-pt-PT-Margarida, ai2-pt-PT-Diogo, ai2-pt-PT-Ines, ai2-pt-PT-Gabriel

ai3-pt-PT-Fernanda, ai3-pt-PT-Raquel, ai3-pt-PT-Duarte
neural	Romanian	ro-RO	ai2-ro-RO-Corina

ai3-ro-RO-Alina, ai3-ro-RO-Alexandru
neural	Russian	ru-RU	ai2-ru-RU-Samara, ai2-ru-RU-Tianna, ai2-ru-RU-Czar, ai2-ru-RU-Igor, ai2-ru-RU-Tassa

ai3-ru-RU-Yelena, ai3-ru-RU-Dariya, ai3-ru-RU-Dmitry

ai5-ru-RU-Yuri, ai5-ru-RU-Vladimir, ai5-ru-RU-Alisa, ai5-ru-RU-Sofia, ai5-ru-RU-Konstantin, ai5-ru-RU-Dmitri, ai5-ru-RU-Ekaterina
neural	Sinhala (Sri Lanka)	si-LK	ai3-si-LK-Charuka, ai3-si-LK-Vedant
neural	Slovak (Slovakia)	sk-SK	ai2-sk-SK-Kristina

ai3-sk-SK-Viktoria, ai3-sk-SK-Lukas
neural	Slovenian (Slovenia)	sl-SI	ai3-sl-SI-Izabela, ai3-sl-SI-Patrik
neural	Somali (Somalia)	so-SO	ai3-so-SO-Fowsio, ai3-so-SO-Cumar
neural	Albanian (Albania)	sq-AL	ai3-sq-AL-Ilir, ai3-sq-AL-Anila
neural	Serbian, Cyrillic	sr-RS	ai3-sr-RS-Katarina, ai3-sr-RS-Nemanja
neural	Sundanese (Indonesia)	su-ID	ai3-su-ID-Pratam, ai3-su-ID-Cindy
neural	Swedish	sv-SE	ai1-sv-SE-Agnes

ai2-sv-SE-Elsa, ai2-sv-SE-Emilie, ai2-sv-SE-Victor, ai2-sv-SE-Lea, ai2-sv-SE-Ludvig

ai3-sv-SE-Sofie, ai3-sv-SE-Mattias, ai3-sv-SE-Hillevi
neural	Swahili (Kenya)	sw-KE	ai3-sw-KE-Obuya, ai3-sw-KE-Fanaka
neural	Swahili (Tanzania)	sw-TZ	ai3-sw-TZ-Peter, ai3-sw-TZ-Firyali
neural	Tamil (India)	ta-IN	ai2-ta-IN-Smita, ai2-ta-IN-Illayavan, ai2-ta-IN-Vihan, ai2-ta-IN-Bhanumathi

ai3-ta-IN-Valluvar, ai3-ta-IN-Pallavi
neural	Tamil (Sri Lanka)	ta-LK	ai3-ta-LK-Shreenika, ai3-ta-LK-Viraj
neural	Tamil (Malaysia)	ta-MY	ai3-ta-MY-Moshika, ai3-ta-MY-Surya
neural	Tamil (Singapore)	ta-SG	ai3-ta-SG-Jabin, ai3-ta-SG-Aaksara
neural	Telugu (India)	te-IN	ai3-te-IN-Mohan, ai3-te-IN-Shruti
neural	Thai (Thailand)	th-TH	ai2-th-TH-Gamon

ai3-th-TH-Narong, ai3-th-TH-Premwadee, ai3-th-TH-Achara
neural	Turkish	tr-TR	ai1-tr-TR-Burcu

ai2-tr-TR-Neylan, ai2-tr-TR-Candana, ai2-tr-TR-Tabeeb, ai2-tr-TR-Roxelana, ai2-tr-TR-Gulizar

ai3-tr-TR-Emel
neural	Ukrainian (Ukraine)	uk-UA	ai2-uk-UA-Aleksandra

ai3-uk-UA-Olena, ai3-uk-UA-Pavlo
neural	Urdu, India	ur-IN	ai3-ur-IN-Fatima, ai3-ur-IN-Salman
neural	Urdu, Pakistan	ur-PK	ai3-ur-PK-Aslam, ai3-ur-PK-Mehreen
neural	Uzbek (Uzbekistan)	uz-UZ	ai3-uz-UZ-Akbar, ai3-uz-UZ-Diliya
neural	Vietnamese (Vietnam)	vi-VN	ai2-vi-VN-Hyunh, ai2-vi-VN-Xuan, ai2-vi-VN-Thi, ai2-vi-VN-Binh

ai3-vi-VN-HoaiMy, ai3-vi-VN-Phuong
neural	Chinese (Wu, S)	wuu-CN	ai3-wuu-CN-Jiang, ai3-wuu-CN-SunLi
neural	Chinese (Cantonese, S)	yue-CN	ai3-yue-CN-Wang, ai3-yue-CN-Yang
neural	Chinese, Cantonese	zh-HK	ai3-zh-HK-WanLung, ai3-zh-HK-HiuGaai, ai3-zh-HK-HiuMaan
neural	Zulu (South Africa)	zu-ZA	ai3-zu-ZA-Gauteng, ai3-zu-ZA-Nonhle
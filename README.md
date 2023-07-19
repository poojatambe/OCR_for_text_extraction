# OCR_for_text_extraction
Different OCR techniques for text extraction.

First install requirements.
```
!pip install -r requirements.txt
```
## EasyOCR

* Parameters:
1. image_path : input image string
2. gpu : device (default= False)
3. low_text: low text bound (default= 0.4)
4. text_threshold: text confidence threshold(default= 0.7)
5. canvas_size: canvas size (default= 2560)
6. paragraph: combine result into paragraph (default= False)
7. rotation_info: rotate each text box (default= False). If True, then rotation take place [90, 180 ,270] for all possible text orientations
8. batch_size: batch size (default= 1)

* Command:
```
!python EasyOCR.py --img ./data/sample_img2.png --low_text 0.3  --text_threshold 0.8 --canvas_size 3000 --gpu True --paragraph True --rotation_info True --batch_size 1
``` 

* Output:
1. OCR with rotation

{
  "text": [
    "zop =",
    "The quick brown fox jumps over the lazy",
    "tulorial cin:ir Jes.",
    "v0 , baiic tesl bul Ihings will get more ccn Nlicsted",
    "Image",
    "In this simplc cxampe wc will tost ithc arcuracy 3 cur C# OCR librayy 0 rcid Icxl irom J PNG",
    "Iron OCR Simple Example"
  ]
}

2. OCR with paragraph enabled

{
  "text": [
    "The quick brown fox jumped over the 5 Iazy dogs!"
  ]
}

3. OCR with default settings

{
  "text": [
    "The quick brown fox",
    "jumped over the 5",
    "dogs!",
    "lazy"
  ]
}

* Reference:
1. https://github.com/JaidedAI/EasyOCR
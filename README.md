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
   
![easyocr_out](https://github.com/poojatambe/OCR_for_text_extraction/assets/64680838/dd11ab94-ff34-4abe-94e1-346fe72f2df9)

```
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
```

2. OCR with paragraph enabled

![easyocr_out1](https://github.com/poojatambe/OCR_for_text_extraction/assets/64680838/83395312-5981-4143-a866-31e65dc42637)

```
{
  "text": [
    "The quick brown fox jumped over the 5 Iazy dogs!"
  ]
}
```
3. OCR with default settings

![easyocr_out2](https://github.com/poojatambe/OCR_for_text_extraction/assets/64680838/39e59ae2-aa22-4115-b1d4-2f0497722a14)
```
{
  "text": [
    "The quick brown fox",
    "jumped over the 5",
    "dogs!",
    "lazy"
  ]
}
```
* Reference:
1. https://github.com/JaidedAI/EasyOCR

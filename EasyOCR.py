import easyocr
import cv2
import numpy as np
import argparse
import json

def OCR_text(
        image_path,  
        gpu, 
        low_text, 
        text_threshold, 
        canvas_size, 
        paragraph,
        rotation_info,
        batch_size
        ):
    img= cv2.imread(image_path)
    reader= easyocr.Reader(['en'], gpu)
    if rotation_info:
        result= reader.readtext(
            img, 
            canvas_size = canvas_size, 
            low_text = low_text, 
            text_threshold = text_threshold,
            paragraph = paragraph, 
            rotation_info =[90, 180, 270],
            batch_size = batch_size,
            )
    else: 
        result= reader.readtext(
            img, 
            canvas_size = canvas_size, 
            low_text = low_text, 
            text_threshold = text_threshold,
            paragraph = paragraph, 
            rotation_info = None,
            batch_size = batch_size,
            )
    return result, img

def display_result(
        image_path,  
        gpu, 
        low_text, 
        text_threshold, 
        canvas_size, 
        paragraph,
        rotation_info,
        batch_size
        ):
    result, img = OCR_text(
        image_path,  
        gpu, 
        low_text, 
        text_threshold, 
        canvas_size, 
        paragraph,
        rotation_info,
        batch_size
        )
    output= {'text':[]}
    for i in range(len(result)):
        output['text'].append(result[i][1])
        pts = np.array(result[i][0], dtype= np.int32)
        img = cv2.polylines(img, [pts], isClosed=True, color= (255, 255, 0), thickness=2)
        if paragraph is False:
            out = cv2.putText(img, str(round(result[i][2], 2)), pts[0], 
                              cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
        else: 
            out= img
    # cv2.imshow('output', out)
    cv2.imwrite('./output/easyocr_out2.jpg', out)
    # cv2.waitKey(0)
    return output
    

if __name__ =="__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument('--img', help='Specify input image', default= '', type=str)
    parser.add_argument('--gpu', default= False, type= bool, help='specify gpu as device')
    parser.add_argument('--low_text', default=0.4, type= float, help='Low text bound score')
    parser.add_argument('--text_threshold', default= 0.7, type= float, help= 'Text confidence threshold')
    parser.add_argument('--canvas_size', default= 2560, type= int, help='canvas size')
    parser.add_argument('--paragraph', default= False, type= bool)
    parser.add_argument('--rotation', default= False, type= bool)
    parser.add_argument('--batch_size', default= 1, type= int)
    opt= parser.parse_args()
    print(opt)
    output= display_result(
            image_path= opt.img,  
            gpu= opt.gpu, 
            low_text= opt.low_text, 
            text_threshold= opt.text_threshold, 
            canvas_size= opt.canvas_size, 
            paragraph= opt.paragraph,
            rotation_info= opt.rotation,
            batch_size= opt.batch_size
            )
    file= json.dumps(output, indent= 2)
    with open('./output/easyocr_out2.json', 'w') as f:
        f.write(file)
@ECHO OFF
SET exePath=%1
SET camName=%2
REM CD C:\Users\sonaw\Documents\Intel\OpenVINO\omz_demos_build\intel64\Debug
REM ECHO %exePath%
REM ECHO %camName%
CD/
C:
CD %exePath%
text_detection_demo.exe -i E:\Songs\sintel_trailer-480p.webm E:\gstreamer\1.0\downloaded-models\intel\text-detection-0004\FP32\text-detection-0004.xml -m_tr E:\gstreamer\1.0\downloaded-models\intel\text-recognition-0014\FP32\text-recognition-0014.xml -dt ctc -tr_pt_first -tr_o_blb_nm "logits" -cam %camName%

# aes-based-ransomware
aes 알고리즘 기반으로 만든 랜섬웨어입니다


# ⚠️ 경고
- 이 랜섬웨어에는 복구키가 따로 들어있지 않습니다.
- 중요한 폴더를 선택하지 마십시오.
- 절대 악용하지 마십시오.

# 실행
*[brew](https://brew.sh)를 이용하여 필요한 패키지들을 설치하는 것을 권장합니다.*
```
brew install python-tk
```
```
brew install python-pycryptodomex
```
필요한 패키지를 설치한 후 [GUI.py](https://github.com/Jongwoo0101/aes-based-ransomware/blob/Jongwoo0101/Main/GUI.py)를 실행합니다.   
<img width="461" alt="스크린샷 2023-06-13 오전 12 34 37" src="https://github.com/Jongwoo0101/aes-based-ransomware/assets/96978536/69a12820-af38-47a0-b6fe-a40ce58b4bac">

다음과 같은 화면이 뜨게 되고 찾아보기를 클릭하여 원하는 폴더를 선택합니다. 

*(중요한 폴더는 절대로 선택하지 마십시오!!) Test폴더를 새로 만들어서 샘플 이미지를 넣는 것을 추천합니다)*

암호화 시작 버튼을 누르면 ~~FUCKED.txt~~파일과 원래 있던파일이 .encrypted 확장자로 변하게 됩니다

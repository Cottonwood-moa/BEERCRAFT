#  :yum:BEERCRAFT  
ㅤ  
`멋쟁이 사자처럼` 인공지능 웹 개발 과정  
ㅤ  
## About The Project  
ㅤ  
`아이템 기반 협업필터링 알고리즘을 활용한 맥주 추천 시스템`  
[참고블로그](https://western-sky.tistory.com/58)  
ㅤ  
* '맥주' 키워드를 검색했을 때 네이버를 기준으로 나오는 모든 블로그의 텍스트를 전부 스크래핑 하여 워드클라우드로 만들어 트렌드를 파악하였습니다.
* 맥주간 유사도 기반 추천 -> 맥주의 평점을 기반으로 코사인 유사도를 추출하여 이용자의 입맛에 맞는 다른 맥주를 추천합니다.
* 이용자의 평점이 반영된 맥주 추천 -> 아이템 기반의 최근접 이웃 CF 알고리즘을 이용한 맥주 추천입니다.
* 최근 국산 수제맥주의 관심이 늘어남에 따라 국산 수제 맥주의 정보와 리뷰를 자유롭게 공유할 수 있는 공간도 마련되어 있습니다.
ㅤ  
ㅤ  
### Built With  
ㅤ  
```json
asgiref==3.3.4
beautifulsoup4==4.9.3
cycler==0.10.0
Django==3.1.3
django-bootstrap4==3.0.1
django-ckeditor==6.1.0
django-js-asset==1.2.2
joblib==1.0.1
kiwisolver==1.3.1
Markdown==3.3.4
matplotlib==3.4.2
numpy==1.21.1
pandas==1.3.1
Pillow==8.3.1
pyparsing==2.4.7
python-dateutil==2.8.2
pytz==2021.1
scikit-learn==0.24.2
scipy==1.7.1
six==1.16.0
soupsieve==2.2.1
sqlparse==0.4.1
threadpoolctl==2.2.0
typing-extensions==3.10.0.0
``` 
ㅤ  
## Getting Started  
먼저 서비스를 이용하려면 로그인이 필요합니다.  
ㅤ  
![image](https://user-images.githubusercontent.com/79053495/137683947-cd4a1736-611f-419c-9b19-d1f9a3a89f64.png)  
ㅤ  
시작하기 버튼을 눌러주세요.  
ㅤ  
![image](https://user-images.githubusercontent.com/79053495/137684050-caefa572-78a1-4365-9f41-229e0ab30819.png)  
ㅤ  
가장 좋아하는 맥주와 맛, 향, 목넘김 중 우선순위 한개를 선택해주세요.
ㅤ  
![image](https://user-images.githubusercontent.com/79053495/137684414-963354e7-e6d1-4ec8-80b2-1ea37962992d.png)  
ㅤ  
유사도 기반으로 맥주가 추천됩니다. 
ㅤ  
![image](https://user-images.githubusercontent.com/79053495/137684516-8f3f97d0-0fd0-4008-8f86-ec8cb612ecb4.png)  
ㅤ  
다섯가지 항목에 대한 클러스터 유형과 평점도 확인할 수 있습니다.
ㅤ  
![image](https://user-images.githubusercontent.com/79053495/137684866-bf45c8e6-65b3-4ffd-a099-1696b753393c.png)  
ㅤ  
국산 수제 맥주의 정보도 얻을 수 있습니다. 
ㅤ  
![image](https://user-images.githubusercontent.com/79053495/137685028-e1853d41-bc36-43fc-b78e-168ffc923943.png)  
![image](https://user-images.githubusercontent.com/79053495/137685052-355d54bd-4fdd-42aa-8d6a-02863ea1f93b.png)
ㅤ  
## More Info  
[깃허브 저장소](https://github.com/Cottonwood-moa/BEERCRAFT)  
[자세한 내용은 블로그를 참조해주세요!](https://cottonwood-moa.tistory.com/)

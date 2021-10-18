<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="https://tistory4.daumcdn.net/tistory/4706624/skin/images/beer.png" alt="Logo" width="80" height="80">

  <h3 align="center">BEERCRAFT</h3>

  <p align="center">
    [멋쟁이사자처럼 x K - Digital Training] 머신러닝 기반 맥주 추천 사이트 
    <br />
    <a href="http://13.209.239.133/"><strong>사이트 보기 »</strong></a>
    <br />
    <br />
    <strong>TEAM</strong><br />
            <a href="https://blog.naver.com/flowermisty">이용석</a>
            <a href="https://github.com/ijo0r98">임주란</a>
            <a href="https://cottonwood-moa.tistory.com/">박건우</a>
            <a href="https://github.com/Riah0987">주리아</a>
            <a href="https://github.com/kang1seok">강원석</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

아이템 기반 협업필터링 알고리즘을 활용한 맥주 추천 시스템  
[참고블로그](https://western-sky.tistory.com/58)  

* '맥주' 키워드를 검색했을 때 네이버를 기준으로 나오는 모든 블로그의 텍스트를 전부 스크래핑 하여 워드클라우드로 만들어 트렌드를 파악하였습니다.
* 맥주간 유사도 기반 추천 -> 맥주의 평점을 기반으로 코사인 유사도를 추출하여 이용자의 입맛에 맞는 다른 맥주를 추천합니다.
* 이용자의 평점이 반영된 맥주 추천 -> 아이템 기반의 최근접 이웃 CF 알고리즘을 이용한 맥주 추천입니다.
* 최근 국산 수제맥주의 관심이 늘어남에 따라 국산 수제 맥주의 정보와 리뷰를 자유롭게 공유할 수 있는 공간도 마련되어 있습니다.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

장고(django) 프레임워크를 기반으로 만들었으며 웹 프론트는 jquery와 Bootstrap 을 사용하였습니다.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
먼저 서비스를 이용하려면 로그인이 필요합니다.  <br />
![image](https://user-images.githubusercontent.com/79053495/137683947-cd4a1736-611f-419c-9b19-d1f9a3a89f64.png)  <br />
시작하기 버튼을 눌러주세요. <br />
![image](https://user-images.githubusercontent.com/79053495/137684050-caefa572-78a1-4365-9f41-229e0ab30819.png)  <br />
가장 좋아하는 맥주와 맛, 향, 목넘김 중 우선순위 한개를 선택해주세요.  <br />
![image](https://user-images.githubusercontent.com/79053495/137684414-963354e7-e6d1-4ec8-80b2-1ea37962992d.png) <br /> 
유사도 기반으로 맥주가 추천됩니다.  <br />
![image](https://user-images.githubusercontent.com/79053495/137684516-8f3f97d0-0fd0-4008-8f86-ec8cb612ecb4.png)  <br />
다섯가지 항목에 대한 클러스터 유형과 평점도 확인할 수 있습니다.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [] Add Additional Templates w/ Examples
- [] Add "components" document to easily copy & paste sections of the readme
- [] Multi-language Support
    - [] Chinese
    - [] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

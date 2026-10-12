# 🚀 Connect AI LAB — connectailap-artnfull-v1

> **Affiliation:** Connect AI LAB  
> **Creator:** [artnfull](https://huggingface.co/artnfull)  
> **Model:** [🤗 Hugging Face (artnfull/connectailap-artnfull-v1)](https://huggingface.co/artnfull/connectailap-artnfull-v1)  
> **Base Model:** Built with [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)  
> **License:** Apache 2.0  

---

## 📌 Overview
This repository provides the core runtime scripts and interactive web playground for **`connectailap-artnfull-v1`**, an experimental model developed as part of **Connect AI LAB** research.  
The model applies **Abliteration (weight-level orthogonal projection and removal of the refusal direction)** to the base model `Qwen3-0.6B`.

---

## 💻 Included Files
* **`connectailab-playground.html`**: Standalone browser-based playground for comparing base vs. abliterated model responses via the LM Studio local API (`http://127.0.0.1:1234/v1`).
* **`local_chat.py`**: Lightweight Python terminal chat interface powered by Hugging Face Transformers.
* **`Modelfile`**: Configuration template for importing and running the model in **Ollama**.

---

## 🚀 How to Run

### 1. Run with LM Studio
1. Download the model file from [Hugging Face](https://huggingface.co/artnfull/connectailap-artnfull-v1).
2. Drag and drop the `.gguf` file into LM Studio.
3. Start the local server (`http://127.0.0.1:1234/v1`) and connect via `connectailab-playground.html`.

### 2. Run with Ollama
```bash
# Create and launch the model in Ollama
ollama create my-qwen -f ./Modelfile
ollama run my-qwen
```

### 3. Run Python Chat
```bash
python local_chat.py
```

---

### 🌐 Hugging Face Profile
* **All Models & Collections:** https://huggingface.co/artnfull

---

### 📱 Related Project: Zero Dopamine Detox
Looking to break free from digital overload and build healthy daily habits?  
Check out our companion Android app on Google Play:

<a href="https://play.google.com/store/apps/details?id=com.zerodopamine.app">
  <img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" width="180">
</a>

---

<details>
<summary><b>🇰🇷 한국어 설명 보기 (Click to expand Korean version)</b></summary>

<br>

## 📌 프로젝트 소개
본 저장소는 **Connect AI LAB** 연구의 일환으로 제작된 `connectailap-artnfull-v1` 모델의 로컬 실행 도구 및 테스트 환경을 제공합니다.  
`Qwen3-0.6B` 기본 모델에 **Abliteration(거절 방향 벡터 직교 투영 및 가중치 제거)** 기법을 적용하여 거절 메커니즘을 조정한 실험용 도구 모음입니다.

## 📁 주요 구성 파일
1. **`connectailab-playground.html`**: LM Studio 로컬 서버와 연동하여 원본 모델과 수정 모델의 답변을 1:1로 비교할 수 있는 독립 실행형 웹 페이지
2. **`local_chat.py`**: 터미널 환경에서 내 모델과 실시간으로 대화할 수 있는 경량 파이썬 스크립트
3. **`Modelfile`**: Ollama에 내 모델을 손쉽게 등록하고 실행할 수 있는 설정 파일

## 🛠️ 실행 방법
1. **LM Studio 사용**: [허깅페이스](https://huggingface.co/artnfull/connectailap-artnfull-v1)에서 모델 다운로드 후 드래그 앤 드롭
2. **Ollama 실행**: `ollama create my-qwen -f ./Modelfile` 실행 후 `ollama run my-qwen`
3. **파이썬 대화 실행**: `python local_chat.py`

---

### 🌐 제작자 허깅페이스 전체 프로필
* **전체 모델 및 프로젝트:** https://huggingface.co/artnfull

---

### 📱 함께 개발한 앱: 제로도파민 (Zero Dopamine Detox)
도파민 중독과 스마트폰 과몰입에서 벗어나 갓생을 살고 싶다면!  
구글 플레이스토어에서 무료로 다운로드 받아보세요:

<a href="https://play.google.com/store/apps/details?id=com.zerodopamine.app">
  <img src="https://play.google.com/intl/en_us/badges/static/images/badges/ko_badge_web_generic.png" width="180">
</a>

</details>

---
*Built with Qwen by Connect AI LAB (artnfull)*

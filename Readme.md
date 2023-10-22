# 🇨🇴 Sign Language Translator 🚀

Experience the magic of sign language translation with our API! 🔮📜 Seamlessly convert spoken or written language into expressive sign language gestures. Connect, communicate, and make your content accessible to a wider audience with our easy-to-integrate API. 🌍🤝💬 #InclusiveCommunication #SignLanguageAPI

## ✒️ API Reference 📚️

#### Check service is up and running 

```http
  GET /health-check
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### WebSocket for transcribe audio and return text

```http
  GET /ws/audio-transcriber
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `message`      | `bytes` | **Required**. Audio in base 64 |


## 👩‍💻 Run Locally 💻️


Clone the project 👫

```bash
  git clone https://github.com/fabianvera728/sign-language-translator-api
```

Go to the project directory 🫚

```bash
  cd sign-language-translator-api
```

Install dependencies 🛫, virtual environment is created by default 🤝

```bash
  make install
```

Start the service 🏁

```bash
  make run
```


## 😅 Authors 🫠

- Fabian Vera [@fabianvera728](https://www.github.com/fabianvera728)
- Daniel Mantilla [@d3terit](https://www.github.com/d3terit)

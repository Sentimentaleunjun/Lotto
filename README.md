# 강현쌤을 위한 로또 추첨기 (Flask + Render)

기존 `lotto.py` 콘솔 버전을 웹사이트로 바꾼 프로젝트입니다.

## 로컬 실행

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

브라우저에서 `http://localhost:5000` 접속 후 번호를 확인하고, **다시 추첨하기** 버튼으로 새 번호를 뽑을 수 있습니다.

## Render 배포

이 저장소 루트의 `render.yaml`과 `requirements.txt`를 사용하면 Render에서 자동 배포됩니다.

1. Render에서 **New + > Blueprint** 선택
2. 이 Git 저장소 연결
3. 배포 완료 후 생성된 URL 접속

또는 수동 설정 시:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

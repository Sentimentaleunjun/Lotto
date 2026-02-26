from flask import Flask, render_template
import random

app = Flask(__name__)


def generate_lotto_numbers() -> list[int]:
    """1~45 사이 숫자 중 중복 없이 6개를 뽑아 오름차순으로 반환."""
    return sorted(random.sample(range(1, 46), 6))


@app.get("/")
def index():
    numbers = generate_lotto_numbers()
    return render_template("index.html", numbers=numbers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

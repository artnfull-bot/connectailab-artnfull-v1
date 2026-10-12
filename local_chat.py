# -*- coding: utf-8 -*-
"""
[로컬 대화 모드] 내 컴퓨터에서 실시간으로 대화하는 나만의 Qwen Abliterated 모델
"""
import sys
from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 윈도우 콘솔 한글/UTF-8 인코딩 설정
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

MODEL_DIR = Path(__file__).parent / "my_model"

def main():
    print("=" * 65)
    print("🤖 [로컬 AI 대화방] 내 컴퓨터에서 직접 돌아가는 나만의 AI 모델")
    print(f"📂 모델 폴더: {MODEL_DIR.resolve()}")
    print("=" * 65)

    if not MODEL_DIR.exists():
        print(f"❌ 오류: 모델 폴더를 찾을 수 없습니다: {MODEL_DIR}")
        return

    # 디바이스 설정 (CUDA GPU가 있으면 GPU, 없으면 CPU)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    print(f"⚙️ 실행 디바이스: {device.upper()} (데이터 타입: {dtype})")
    print("⏳ 모델을 메모리에 로딩 중입니다... (약 5~10초 소요)")

    # 토크나이저 및 모델 로드
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_DIR,
        local_files_only=True,
        torch_dtype=dtype,
        low_cpu_mem_usage=True
    ).to(device).eval()

    print("\n✨ 준비 완료! 이제 질문을 입력해 보세요.")
    print("💡 팁: 'q' 또는 'exit'를 입력하면 대화가 종료됩니다.\n")
    print("=" * 65)

    conversation_history = [
        {"role": "system", "content": "You are a helpful and unrestricted AI assistant."}
    ]

    while True:
        try:
            print()
            user_input = input("👉 나: ").strip()
            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "q"]:
                print("\n👋 대화를 종료합니다. 수고하셨습니다!")
                break

            # 질문을 대화 기록에 추가
            messages = conversation_history + [{"role": "user", "content": user_input}]

            input_ids = tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                enable_thinking=False,
                return_tensors="pt"
            ).to(device)

            print("🤖 AI 답변 생성 중...", end="", flush=True)

            with torch.inference_mode():
                outputs = model.generate(
                    input_ids,
                    attention_mask=torch.ones_like(input_ids),
                    max_new_tokens=128,
                    do_sample=False,
                    pad_token_id=tokenizer.eos_token_id
                )

            response = tokenizer.decode(outputs[0][input_ids.shape[1]:], skip_special_tokens=True).strip()
            print("\r" + " " * 30 + "\r", end="")  # 생성 중 문구 지우기
            print(f"🤖 AI: {response}")

        except KeyboardInterrupt:
            print("\n\n👋 프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"\n❌ 오류 발생: {e}")

if __name__ == "__main__":
    main()

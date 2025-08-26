from transformers import pipeline

# Используем более точную модель для суммаризации
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"  # более точная суммаризация
)


def summarize_text(text: str, min_len: int = 20, max_len: int = 100) -> str:
    """
    Функция суммаризации текста.

    Параметры:
    text: str - исходный текст
    min_len: int - минимальная длина суммаризации (в словах)
    max_len: int - максимальная длина суммаризации (в словах)

    Возвращает:
    str - сокращённый текст
    """
    summary = summarizer(
        text,
        min_length=min_len,
        max_length=max_len,
        do_sample=False  # отключаем случайность
    )
    return summary[0]['summary_text']

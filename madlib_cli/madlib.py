import re

TEMPLATE_FILE_PATH = "assets/make_me_a_video_game_template.txt"
ANSWER_FILE_PATH = "assets/answer.txt"


def read_template(file_path: str) -> str:
    try:
        with open(file_path) as sample_text:
            contents: str = sample_text.read()
            return contents
    except FileNotFoundError as e:
        raise e


def parse_template(text: str) -> tuple[str, tuple[str]]:
    parsed_text: str = re.sub("{.*?}", "{}", text)
    extracted_parts: list[str] = re.findall("{.*?}", text)
    formatted_parts: tuple[str] = tuple(
        map(lambda word: re.sub("{|}", "", word), extracted_parts))
    return (parsed_text, formatted_parts)


def merge(template: str, answers: list[str]) -> str:
    return template.format(*answers)


def save_file(text: str, file_path: str) -> None:
    with open(file_path, "w") as saved_file:
        saved_file.write(text)


if __name__ == "__main__":
    text_contents: str = read_template(TEMPLATE_FILE_PATH)
    template, parts = parse_template(text_contents)
    greeting = "Hello and welcome to the Madlib! \nTo play, please follow the prompt"
    answers: list[str] = []

    print(greeting)

    for part in parts:
        user_input: str = input(f"Enter {part} \n> ")
        answers.append(user_input)

    final_text = merge(template, answers)

    print(final_text)
    save_file(final_text, ANSWER_FILE_PATH)

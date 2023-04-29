import random
from typing import Callable, List, Tuple


def gpt_4(prompt: str) -> str:
    # Placeholder function to simulate GPT-4 model response
    # In practice, this should be replaced with a proper GPT-4 API call
    return random.choice(["Identity", "InvertedResidual_3_3", "InvertedResidual_5_6"])


def run(model: str) -> float:
    # Placeholder function to simulate running a model configuration and returning accuracy
    # This function should be replaced with actual model training and evaluation code
    return random.random()


def problem_encoding() -> str:
    # Placeholder function for encoding the NAS problem
    return "Please recommend a neural architecture configuration."


def genius(
    gpt_4: Callable[[str], str],
    problem_encoding: Callable[[], str],
    run: Callable[[str], float],
    T: int,
) -> Tuple[str, float]:

    best_model = None
    best_accuracy = -1

    for t in range(T):
        if t == 0:
            model = gpt_4(problem_encoding())
        else:
            prompt = f"By using this model, we achieved an accuracy of {accuracy * 100:.2f}%. Please recommend a new model that outperforms prior architectures based on the above mentioned experiments. Also, please provide a rationale explaining why the suggested model surpasses all previous architectures."
            model = gpt_4(prompt)

        accuracy = run(model)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model

    return best_model, best_accuracy


if __name__ == "__main__":
    T = 5  # Number of iterations
    best_model, best_accuracy = genius(gpt_4, problem_encoding, run, T)
    print(f"Best Model Configuration: {best_model}")
    print(f"Best Accuracy: {best_accuracy * 100:.2f}%")

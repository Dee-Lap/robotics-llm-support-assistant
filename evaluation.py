import pandas as pd


def evaluate_logs():

    data = pd.read_csv("data/conversations.csv")

    print("Chatbot Evaluation")

    print(
        "Total conversations:",
        len(data)
    )

    avg_response_length = (
        data["response"]
        .str.len()
        .mean()
    )

    print(
        "Average response length:",
        round(avg_response_length, 2)
    )

    empty_responses = (
        data["response"]
        .isna()
        .sum()
    )

    print(
        "Empty responses:",
        empty_responses
    )


if __name__ == "__main__":
    evaluate_logs()
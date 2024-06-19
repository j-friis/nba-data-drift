import os
import pandas as pd


def load_data() -> pd.DataFrame:
    filename = os.path.join("..", "data", "raw", "games.csv")

    try:
        # Check if the file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file {filename} does not exist.")

        # Load the data
        games_df = pd.read_csv(filename)
        print(f"Successfully loaded data from {filename}")

        return games_df

    except FileNotFoundError as e:
        print(e)


def save_data(df: pd.DataFrame) -> None:
    output_filename = os.path.join('..', 'data', 'processed', 'games_processed.csv')
    df.to_csv(output_filename, index=False)
    print(f"DataFrame saved to {output_filename}")

    return

def data_selection_transformation(df: pd.DataFrame) -> pd.DataFrame:
    subset_columns = [
        "SEASON",
        "HOME_TEAM_ID",
        "VISITOR_TEAM_ID",
        "PTS_home",
        "PTS_away",
        "FG3_PCT_home",
        "FG3_PCT_away",
        "FT_PCT_home",
        "FT_PCT_away",
    ]

    df_subset = df[subset_columns].copy()

    df_subset["total_points"] = df_subset["PTS_home"] + df_subset["PTS_away"]
    df_subset["FG3_PCT_avg"] = (
        df_subset["FG3_PCT_home"] + df_subset["FG3_PCT_away"]
    ) / 2
    df_subset["FT_PCT_avg"] = (df_subset["FT_PCT_home"] + df_subset["FT_PCT_away"]) / 2

    return df_subset


def main():
    print("This is the main function.")
    df_games = load_data()
    df_games = data_selection_transformation(df_games)
    save_data(df_games)


if __name__ == "__main__":
    main()

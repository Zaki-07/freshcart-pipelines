
from sklearn.model_selection import train_test_split

# Allow this file to work both inside and outside Mage.
try:
    from mage_ai.data_preparation.decorators import transformer
except ImportError:
    def transformer(func):
        return func


@transformer
def transform(df, *args, **kwargs):
    target_column = "target"

    if target_column not in df.columns:
        raise ValueError(f"Missing target column: {target_column}")

    train_indices, test_indices = train_test_split(
        df.index,
        test_size=0.3,
        random_state=42,
        stratify=df[target_column]
    )

    output = df.copy()
    output["split"] = "train"
    output.loc[test_indices, "split"] = "test"

    return output

"""
Script para treinar e exportar os modelos do notebook
para o diretório models/ da API.

Uso:
    python scripts/train_and_export.py
"""

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


def main():
    # Por enquanto estamos usando dados fictícios — quando o notebook estiver pronto,
    # substitua este trecho pelo carregamento do dataset real com as 44 features clínicas.
    print("Carregando dados...")
    X = pd.DataFrame({"feature_1": [1, 2, 3], "feature_2": [4, 5, 6]})
    y = [0, 1, 0]

    num_cols = X.columns.tolist()
    num_pipeline = Pipeline(
        [("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )

    preprocessor = ColumnTransformer([("num", num_pipeline, num_cols)])

    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("model", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )

    pipeline.fit(X, y)

    joblib.dump(pipeline, "models/logistic_regression.pkl")
    print("Modelo salvo em models/logistic_regression.pkl")


if __name__ == "__main__":
    main()

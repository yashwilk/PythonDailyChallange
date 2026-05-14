import numpy as np
import joblib
import sklearn
from sklearn.datasets import make_classification

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, classification_report

X,y=make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=10, random_state=42)

print(X.shape,y.shape)

rng=np.random.default_rng(42)
missing_mask=rng.random(X.shape)<0.1
X[missing_mask]=np.nan

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


pipeline=Pipeline([
    ("imputer",SimpleImputer(strategy="mean")),
    ("scaler",StandardScaler()),
    ("model", LGBMClassifier(random_state=42))])


param_grid={"model__n_estimators":[100,200],
            "model__learning_rate":[0.01,0.1,0.05],
            "model__max_depth":[-1,5,10],
            "model__num_leaves":[15,31,63]}

gs=GridSearchCV(estimator=pipeline,
                          param_grid=param_grid,scoring="accuracy",
                          cv=5,n_jobs=-1,
                          verbose=2)


gs.fit(X_train,y_train)
gs.fit(X_train,y_train)
print("Best Parameters:",gs.best_estimator_)
print("Best Score:",gs.best_score_)
print("best parameters:",gs.best_params_)
print("best score:",gs.best_score_)

best_pipeline=gs.best_estimator_

y_pred = best_pipeline.predict(X_test)



print("\nTest Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))



best_imputer = best_pipeline.named_steps["imputer"]
best_scaler = best_pipeline.named_steps["scaler"]
best_model = best_pipeline.named_steps["model"]


joblib.dump(best_pipeline, "best_lightgbm_pipeline.pkl")

print("\nBest pipeline saved as best_lightgbm_pipeline.pkl")

# 9. Load and test later
# -----------------------------
loaded_pipeline = joblib.load("best_lightgbm_pipeline.pkl")

new_predictions = loaded_pipeline.predict(X_test)

print("\nLoaded model accuracy:")
print(accuracy_score(y_test, new_predictions))
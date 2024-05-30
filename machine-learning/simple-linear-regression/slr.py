import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # これがsimple-linear-regression model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# ダミーデータの作成
np.random.seed(0)
X = 2 * np.random.rand(200, 1)
y = 4 + 3 * X + np.random.randn(200, 1)

# 訓練データとテストデータへの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# モデルの選択と訓練
model = LinearRegression()
model.fit(X_train, y_train)

# 予測
y_pred = model.predict(X_test)

# モデルの評価
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# 係数と切片の表示
print(f"Coefficient: {model.coef_[0][0]}")
print(f"Intercept: {model.intercept_[0]}")

# 訓練データと予測直線プロット
plt.scatter(X, y, color="blue")
plt.plot(X_test, y_pred, color="red", linewidth=2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.show()
#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#%%
df = pd.read_csv("data_cleaned.csv")

# %%

numerical_features = ['loc_x', 'loc_y', 'minutes_remaining', 'period', 'shot_distance']
categorical_features = ['combined_shot_type', 'playoffs','shot_zone_area', 'shot_zone_basic', 'shot_zone_range', 'opponent']

df_categorical_one_hot = pd.get_dummies(df[categorical_features])
X = pd.concat([df[numerical_features], df_categorical_one_hot], axis=1)
Y = df['shot_made_flag']
# %%

num_train = 20000
num_test = len(X) - num_train
X_train = X[:num_train]
X_test = X[num_train:]
Y_train = Y[:num_train]
Y_test = Y[num_train:]

# %%
from sklearn.tree import DecisionTreeClassifier
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, Y_train)

#%%
# get importance
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': decision_tree.feature_importances_})
top_features = feature_importance.sort_values(by=['importance'], ascending=False).head(10)
sns.barplot(x='importance', y = 'feature', data = top_features)

# %%
from sklearn.metrics import accuracy_score, precision_score, recall_score
Y_pred = decision_tree.predict(X_test)
print('Accuracy:', accuracy_score(Y_test, Y_pred))
print('Precision:', precision_score(Y_test, Y_pred))
print('Recall:', recall_score(Y_test, Y_pred))

# %%
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(decision_tree, X_test, Y_test)
# %%

# %%

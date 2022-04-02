# Q.5 Write a Program in python for Developing and implementing Decision Tree model on the dataset.
# Code
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import classification_report,confusion_matrix

# In[23]:
import pandas as pd
path=r"C:\Users\Admin\Desktop\Iris.csv"
df=pd.read_csv(path)
#print(df.head(50))

# In[21]:
target=df['Species']
X=df.copy()
X=X.drop('Species',axis=1)

# In[22]:
print(X)

# In[24]:
le=LabelEncoder()
target=le.fit_transform(target)
target

# In[28]:
y=target

#spliting the data in 80:20 ratio
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("Training Split Input-", X_train.shape)
print("Testing Split Input-", X_test.shape)

# In[29]:
dtree=DecisionTreeClassifier()
dtree.fit(X_train,y_train)
print('Decision tree classifier Created')

# In[32]:
#prdicting the values of test data
y_pred=dtree.predict(X_test)
print(y_pred)
print("Classification report-\n",classification_report(y_test,y_pred))

# In[34]:
plt.figure(figsize=(20,20))
dec_tree=plot_tree(decision_tree=dtree,feature_names=X.columns,class_names=["sentosa","versicolor","verginica"],filled=True, precision=4)

# HOUSE-PRICE-PRADICTION-USING-MACHINE-LEARNING
Goal for this project is to build an end to end solution or application that is capable of predicting the house prices better than individuals.
In this project we compare different machine learning methods performance in __predicting the house price of houses based on a number of features such as the area, the number of bhk and availability and the geographical position.__

1.	Data Collection<br>
__Here data collected from kaggle__, the statistics were gathered house prices, the information includes many variables such as area type, availability, location, BHK, society, total square feet, bathrooms, and balconies.

2.	Decision Tree Regression<br>
It is an object that trains a tree-structured model to predict data in the future in order to provide meaningful continuous output. The core principles of decision trees, Maximizing Information Gain, Classification trees, and Regression trees are the processes involved in decision tree regression. The essential notion of decision trees is that they are built via recursive partitioning. Each node can be divided into child nodes, beginning with the root node, which is known as the parent node. These nodes have the potential to become the parent nodes of their resulting offspring nodes. The nodes at the informative features are specified as the maximizing information gain, to establish an objective function that is to optimize the tree learning method.
__Here we decided to implement decision tree technique in our project,__ decision tree contain two type of algorithm 1. Random-Forest and 2. Xgboost

3.	Random-Forest Regression<br>
Random forest is a Supervised Machine Learning Algorithm that is used widely in Classification and Regression problems. It builds decision trees on different samples and takes their majority vote for classification and average in case of regression.

3.1	Classification Trees<br>
Classification trees are used to forecast the object into classes of a categorical dependent variable based on one or more predictor variables.
 
3.2	Regression Trees<br>
It supports both continuous and categorical input variables. Regression trees are regarded as research with
various machine algorithms for the regression issue, with the Decision Tree approach providing the lowest loss. __In this project the R-Squared value for the Random-Forest Regression is 0.998, indicating that it is an excellent model.__ The Decision Tree was used to complete the web development.

3.3	Flask<br>
After completing preprocessing and modeling, __Here design (GUI) model base on web app to predict price using Flask Programming__

![1](https://user-images.githubusercontent.com/74731969/178756252-573a44ae-24bb-486d-9388-a596de8f4722.jpg)
![2](https://user-images.githubusercontent.com/74731969/178756316-9e872802-6a45-47ee-b223-da09886ba68f.jpg)
![Picture1](https://github.com/KarthikDarvesh/HOUSE-PRICE-PRADICTION-USING-MACHINE-LEARNING/assets/74731969/4fcc3af9-19bf-4d9d-b148-2f6ca4f89b58)
![Picture2](https://github.com/KarthikDarvesh/HOUSE-PRICE-PRADICTION-USING-MACHINE-LEARNING/assets/74731969/34e4d6ca-60a9-4b1d-b6af-98261c53323e)
![Picture3](https://github.com/KarthikDarvesh/HOUSE-PRICE-PRADICTION-USING-MACHINE-LEARNING/assets/74731969/b8f15b6f-8c8a-4f2c-914e-1a36d1b84661)
![5](https://user-images.githubusercontent.com/74731969/178756345-b2eb7047-8f38-4a2a-8f3e-492c8929b10d.jpg)

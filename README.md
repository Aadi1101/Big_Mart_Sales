
![Logo](https://miro.medium.com/max/1400/1*HA5LVUE38Ern5hX2jQGa5A.png)


# Big Mart Sales Analysis

Through this sales prediction the outlets will be helped by knowing what challenges they can face this will help the sales team to understand on which product they should focus and promote to increase their sales. 


## Lessons Learned

_What did you learn while building this project?_

Using this analysis I predicted the price of each product using various features.

_What challenges did you face and how did you overcome them?_

- The features were categorical so converted them to numerical using LabelEncoder function.
- Few features had null values so used various analytical methods to replace the null values with the appropriate categorical value. 
    
## Features

- Item_Identifier              
- Item_Weight                  
- Item_Fat_Content             
- Item_Visibility              
- Item_Type                    
- Item_MRP                     
- Outlet_Identifier            
- Outlet_Establishment_Year    
- Outlet_Size                  
- Outlet_Location_Type         
- Outlet_Type                  

## Installation

Install Required Packages on terminal

```terminal
pip install numpy
pip install pandas
pip install matplotlib.pyplot
pip install sklearn
pip install seaborn
pip install xgboost
```


## Usage/Examples

```python
import pandas as pd
data = pd.read_csv("dataset_file_path")
```


## FAQ

#### Q1. Why I used XGBoost Regressor for this analysis?

The default base learners of XGBoost are tree ensembles. The tree ensemble model is a set of classification and regression trees (CART). 
Trees are grown one after another, and attempts to reduce the misclassification rate are made in subsequent iterations.


## Dataset Link

[Big Mart Sales](https://www.kaggle.com/datasets/mrmorj/big-mart-sales)


## Documentation

[XGBoost](https://xgboost.readthedocs.io/en/stable/python/python_api.html) ,
[Pandas](https://pandas.pydata.org/docs/) ,
[Numpy](https://numpy.org/doc/) ,
[Matplotlib](https://matplotlib.org/stable/index.html) ,
[Seaborn](https://seaborn.pydata.org/)

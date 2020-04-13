# PL_results_Prediction
Premier League's results prediction with GUI using XGBoost, Random forest and gradient boosting.
The application tells chances in percentage for win of home or away team and of tie.

## Dataset
Dataset was collected from [here](http://football-data.co.uk/englandm.php) for 2000-2019 season.

## Usage
pip3 install numpy scikit-learn pandas matplotlib imblearn
python3 gui.py
XGBoost notebook is being executed in python2, all else are in python3.

## Results
Getting average validation accuracy of 75% after oversampling data using SMOTE. Before oversampling, the accuracy was around 62%.

![image](https://user-images.githubusercontent.com/28213136/79128457-fc64a780-7dbc-11ea-8696-7c7750ce3bb4.png)

![image](https://user-images.githubusercontent.com/28213136/79128789-86ad0b80-7dbd-11ea-9087-2b5bfc5edb75.png)

![image](https://user-images.githubusercontent.com/28213136/79128875-a8a68e00-7dbd-11ea-9309-b49551becaf8.png)

![image](https://user-images.githubusercontent.com/28213136/79128922-bc51f480-7dbd-11ea-8fa2-0bb31a3268de.png)

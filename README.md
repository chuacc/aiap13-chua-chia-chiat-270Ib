# AIAP Batch 13 Technical Assessment

Name : Chua Chia Chiat<br>



***Folder Structure:***<br>

![Screenshot from 2023-01-16 14-39-47](https://user-images.githubusercontent.com/122468655/212614720-79ad6e7c-c70e-48de-ab67-a9886f4f5975.png)

***Executing the pipeline***<br>

The pipeline can be executed from the main directory using command "bash run.sh"

***Pipeline***<br>
![Screenshot from 2023-01-16 17-55-42](https://user-images.githubusercontent.com/122468655/212654331-6f0c33c9-0ad2-4c8c-a6fd-6ba0f6cbbadb.png)
<ol>
    <li>Train data are sent into the pipeline. The train data are transformed into an appropriate format and fit the model</li>
    <li>Test data are being sent thru the pipeline. The same data transformation process is being applied on the test data. The fitted model makes prediction base on the test data inputs.</li>

</ol>


***How features are being Processed***<br>
![Screenshot from 2023-01-16 15-44-59](https://user-images.githubusercontent.com/122468655/212624120-7f809d6d-4ec9-4f2c-8608-7bc628dff28c.png)


***Choice of models for machine learning task:***<br>
In this ML assessment, the objective is to predict the occurence failure of car.
This is a supervised classification problem.
Models suitable are such as :
- Random Forest
- Supported vector classifier
- Ensemble Decision Tree
- Gradient Boost classifier

***Evaluation matrics***<br>

Assuming this automotive company is a car leasing company and maintainence of the car is under the responsibility of the company. F1 score, precision and recall are suitable evaluation metrics. A good precision would mean less false positive would help the company to save some cost if the maintanence cost are high as car less prone to failure can be serviced less regularly.


***Finding from EDA***<br>

1) The data set is imbalance (10% of cars with failure)
2) 3 factories ("Bedok, Germany", "Newton, China", "Shang Hai, China") produces car with high failure percentage 



# petrus-ml

ModelV1 (Linear regression without feature selection)

Input-
'Age', 'MaturitySize', 'FurLength', 'Quantity', 'Fee', 'VideoAmt','Description', 'PhotoAmt', 'Type_2', 'Gender_2', 'Gender_3', 'Color1_2',
'Color1_3', 'Color1_4', 'Color1_5', 'Color1_6', 'Color1_7','Vaccinated_2', 'Vaccinated_3', 'Dewormed_2', 'Dewormed_3','Sterilized_2', 'Sterilized_3', 'Health_2', 'Health_3',


Output-
'AdoptionSpeed'


ModelV1 (Linear regression with feature selection)

Input-
'Age','Vaccinated_2','Sterilized_2'

Output-
'AdoptionSpeed'

ModelV3 (Neural network)

Input-
'Type','Name','Age','Gender', 'MaturitySize', 'FurLength',
       'Quantity', 'Fee', 'VideoAmt', 'Description','PhotoAmt', 'Color1_2',
       'Color1_3', 'Color1_4', 'Color1_5', 'Color1_6', 'Color1_7',
       'Vaccinated_2', 'Vaccinated_3', 'Dewormed_2', 'Dewormed_3',
       'Sterilized_2', 'Sterilized_3', 'Health_2', 'Health_3'
       
Output-
'AdoptionSpeed_0', 'AdoptionSpeed_1', 'AdoptionSpeed_2',
       'AdoptionSpeed_3', 'AdoptionSpeed_4'

To run ML service, in terminal at root directory run:`flask run`

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import gdown

st.markdown('# Predicting Customer Ability to Pay Credits')
temp_dict = {
    'CNT_CHILDREN' : 0,
    'AMT_CREDIT' : 0,
    'AMT_GOODS_PRICE' : 0,
    'REGION_POPULATION_RELATIVE' : 0,
    'DAYS_BIRTH' : 0,
    'DAYS_REGISTRATION' : 0,
    'DAYS_ID_PUBLISH' : 0,
    'HOUR_APPR_PROCESS_START' : 0,
    'DAYS_LAST_PHONE_CHANGE' : 0,
    'NAME_CONTRACT_TYPE_Cash loans' : 0,
    'NAME_CONTRACT_TYPE_Revolving loans' : 0,
    'CODE_GENDER_F' : 0,
    'CODE_GENDER_M' : 0,
    'CODE_GENDER_XNA' : 0,
    'FLAG_OWN_CAR_No' : 0,
    'FLAG_OWN_CAR_Yes' : 0,
    'NAME_INCOME_TYPE_Businessman' : 0,
    'NAME_INCOME_TYPE_Commercial associate' : 0,
    'NAME_INCOME_TYPE_Maternity leave' : 0,
    'NAME_INCOME_TYPE_Pensioner' : 0,
    'NAME_INCOME_TYPE_State servant' : 0,
    'NAME_INCOME_TYPE_Student' : 0,
    'NAME_INCOME_TYPE_Unemployed' : 0,
    'NAME_INCOME_TYPE_Working' : 0,
    'NAME_EDUCATION_TYPE_Academic degree' : 0,
    'NAME_EDUCATION_TYPE_Higher education' : 0,
    'NAME_EDUCATION_TYPE_Incomplete higher' : 0,
    'NAME_EDUCATION_TYPE_Lower secondary' : 0,
    'NAME_EDUCATION_TYPE_Secondary / secondary special' : 0,
    'NAME_FAMILY_STATUS_Civil marriage' : 0,
    'NAME_FAMILY_STATUS_Married' : 0,
    'NAME_FAMILY_STATUS_Separated' : 0,
    'NAME_FAMILY_STATUS_Single / not married' : 0,
    'NAME_FAMILY_STATUS_Unknown' : 0,
    'NAME_FAMILY_STATUS_Widow' : 0,
    'NAME_HOUSING_TYPE_Co-op apartment' : 0,
    'NAME_HOUSING_TYPE_House / apartment' : 0,
    'NAME_HOUSING_TYPE_Municipal apartment' : 0,
    'NAME_HOUSING_TYPE_Office apartment' : 0,
    'NAME_HOUSING_TYPE_Rented apartment' : 0,
    'NAME_HOUSING_TYPE_With parents' : 0,
    'FLAG_EMP_PHONE_No' : 0,
    'FLAG_EMP_PHONE_Yes' : 0,
    'FLAG_WORK_PHONE_No' : 0,
    'FLAG_WORK_PHONE_Yes' : 0,
    'FLAG_PHONE_No' : 0,
    'FLAG_PHONE_Yes' : 0,
    'REGION_RATING_CLIENT_High' : 0,
    'REGION_RATING_CLIENT_Low' : 0,
    'REGION_RATING_CLIENT_Medium' : 0,
    'ORGANIZATION_TYPE_Advertising' : 0,
    'ORGANIZATION_TYPE_Agriculture' : 0,
    'ORGANIZATION_TYPE_Bank' : 0,
    'ORGANIZATION_TYPE_Business Entity Type 1' : 0,
    'ORGANIZATION_TYPE_Business Entity Type 2' : 0,
    'ORGANIZATION_TYPE_Business Entity Type 3' : 0,
    'ORGANIZATION_TYPE_Cleaning' : 0,
    'ORGANIZATION_TYPE_Construction' : 0,
    'ORGANIZATION_TYPE_Culture' : 0,
    'ORGANIZATION_TYPE_Electricity' : 0,
    'ORGANIZATION_TYPE_Emergency' : 0,
    'ORGANIZATION_TYPE_Government' : 0,
    'ORGANIZATION_TYPE_Hotel' : 0,
    'ORGANIZATION_TYPE_Housing' : 0,
    'ORGANIZATION_TYPE_Industry: type 1' : 0,
    'ORGANIZATION_TYPE_Industry: type 10' : 0,
    'ORGANIZATION_TYPE_Industry: type 11' : 0,
    'ORGANIZATION_TYPE_Industry: type 12' : 0,
    'ORGANIZATION_TYPE_Industry: type 13' : 0,
    'ORGANIZATION_TYPE_Industry: type 2' : 0,
    'ORGANIZATION_TYPE_Industry: type 3' : 0,
    'ORGANIZATION_TYPE_Industry: type 4' : 0,
    'ORGANIZATION_TYPE_Industry: type 5' : 0,
    'ORGANIZATION_TYPE_Industry: type 6' : 0,
    'ORGANIZATION_TYPE_Industry: type 7' : 0,
    'ORGANIZATION_TYPE_Industry: type 8' : 0,
    'ORGANIZATION_TYPE_Industry: type 9' : 0,
    'ORGANIZATION_TYPE_Insurance' : 0,
    'ORGANIZATION_TYPE_Kindergarten' : 0,
    'ORGANIZATION_TYPE_Legal Services' : 0,
    'ORGANIZATION_TYPE_Medicine' : 0,
    'ORGANIZATION_TYPE_Military' : 0,
    'ORGANIZATION_TYPE_Mobile' : 0,
    'ORGANIZATION_TYPE_Other' : 0,
    'ORGANIZATION_TYPE_Police' : 0,
    'ORGANIZATION_TYPE_Postal' : 0,
    'ORGANIZATION_TYPE_Realtor' : 0,
    'ORGANIZATION_TYPE_Religion' : 0,
    'ORGANIZATION_TYPE_Restaurant' : 0,
    'ORGANIZATION_TYPE_School' : 0,
    'ORGANIZATION_TYPE_Security' : 0,
    'ORGANIZATION_TYPE_Security Ministries' : 0,
    'ORGANIZATION_TYPE_Self-employed' : 0,
    'ORGANIZATION_TYPE_Services' : 0,
    'ORGANIZATION_TYPE_Telecom' : 0,
    'ORGANIZATION_TYPE_Trade: type 1' : 0,
    'ORGANIZATION_TYPE_Trade: type 2' : 0,
    'ORGANIZATION_TYPE_Trade: type 3' : 0,
    'ORGANIZATION_TYPE_Trade: type 4' : 0,
    'ORGANIZATION_TYPE_Trade: type 5' : 0,
    'ORGANIZATION_TYPE_Trade: type 6' : 0,
    'ORGANIZATION_TYPE_Trade: type 7' : 0,
    'ORGANIZATION_TYPE_Transport: type 1' : 0,
    'ORGANIZATION_TYPE_Transport: type 2' : 0,
    'ORGANIZATION_TYPE_Transport: type 3' : 0,
    'ORGANIZATION_TYPE_Transport: type 4' : 0,
    'ORGANIZATION_TYPE_University' : 0,
    'ORGANIZATION_TYPE_XNA' : 0,
}

uniq = {
    'CNT_CHILDREN' : 0,
    'AMT_CREDIT' : 0,
    'AMT_GOODS_PRICE' : 0,
    'REGION_POPULATION_RELATIVE' : 0,
    'DAYS_BIRTH' : 0,
    'DAYS_REGISTRATION' : 0,
    'DAYS_ID_PUBLISH' : 0,
    'HOUR_APPR_PROCESS_START' : 0,
    'DAYS_LAST_PHONE_CHANGE' : 0,
    'NAME_CONTRACT_TYPE' : ['Cash loans', 'Revolving loans'],
    'CODE_GENDER' : ['M', 'F', 'XNA'],
    'FLAG_OWN_CAR' : ['Yes', 'No'],
    'NAME_INCOME_TYPE' : ['Working', 'State servant', 'Commercial associate', 'Pensioner', 'Unemployed',
                          'Student', 'Businessman', 'Maternity leave'],
    'NAME_EDUCATION_TYPE' : ['Secondary / secondary special', 'Higher education', 'Incomplete higher',
                             'Lower secondary', 'Academic degree'],
    'NAME_FAMILY_STATUS' : ['Single / not married', 'Married', 'Civil marriage', 'Widow', 'Separated',
                            'Unknown'],
    'NAME_HOUSING_TYPE' : ['House / apartment', 'Rented apartment', 'With parents',
                           'Municipal apartment', 'Office apartment', 'Co-op apartment'],
    'FLAG_EMP_PHONE' : ['Yes', 'No'],
    'FLAG_WORK_PHONE' : ['Yes', 'No'],
    'FLAG_PHONE' : ['Yes', 'No'],
    'REGION_RATING_CLIENT' : ['High', 'Medium', 'Low'],
    'ORGANIZATION_TYPE' : ['Business Entity Type 3', 'School', 'Government', 'Religion', 'Other', 'XNA',
                            'Electricity', 'Medicine', 'Business Entity Type 2', 'Self-employed',
                            'Transport: type 2', 'Construction', 'Housing', 'Kindergarten',
                            'Trade: type 7', 'Industry: type 11', 'Military', 'Services',
                            'Security Ministries', 'Transport: type 4', 'Industry: type 1', 'Emergency',
                            'Security', 'Trade: type 2', 'University', 'Transport: type 3', 'Police',
                            'Business Entity Type 1', 'Postal', 'Industry: type 4', 'Agriculture',
                            'Restaurant', 'Culture', 'Hotel', 'Industry: type 7', 'Trade: type 3',
                            'Industry: type 3', 'Bank', 'Industry: type 9', 'Insurance', 'Trade: type 6',
                            'Industry: type 2', 'Transport: type 1', 'Industry: type 12', 'Mobile',
                            'Trade: type 1', 'Industry: type 5', 'Industry: type 10', 'Legal Services',
                            'Advertising', 'Trade: type 5', 'Cleaning', 'Industry: type 13',
                            'Trade: type 4', 'Telecom', 'Industry: type 8', 'Realtor', 'Industry: type 6'],
}

col_dict = {
    'CNT_CHILDREN' : 'Number of Children', 
    'AMT_CREDIT' : 'Credit Amount',
    'AMT_GOODS_PRICE' : 'Goods Price',
    'REGION_POPULATION_RELATIVE' : 'Region Population',
    'DAYS_BIRTH' : 'Age of Client',
    'DAYS_REGISTRATION' :  'How many days before the application did client change his registration?',
    'DAYS_ID_PUBLISH' : 'How many days before the application did client change the identity document with which he applied for the loan?',
    'HOUR_APPR_PROCESS_START' : 'Approximately at what hour did the client apply for the loan?',
    'DAYS_LAST_PHONE_CHANGE' : 'How many days before application did client change phone?',
    'NAME_CONTRACT_TYPE' : 'Contract Type',
    'CODE_GENDER' : 'Gender',
    'FLAG_OWN_CAR' : 'Does Client Own a Car?',
    'NAME_INCOME_TYPE' : 'Income Type', 
    'NAME_EDUCATION_TYPE' : 'Education Type',
    'NAME_FAMILY_STATUS' : 'Family Status',
    'NAME_HOUSING_TYPE' : 'Housing Type',
    'FLAG_EMP_PHONE' : 'Does Client have a Work Phone?',
    'FLAG_WORK_PHONE' : 'Does Client have a Home Phone?',
    'FLAG_PHONE' : 'Does Client have a Phone?',
    'REGION_RATING_CLIENT' : 'Client Region Rating',
    'ORGANIZATION_TYPE' : 'Type of organization where client works',
}

val_col = [
    'CNT_CHILDREN',
    'AMT_CREDIT',
    'AMT_GOODS_PRICE',
    'REGION_POPULATION_RELATIVE',
    'DAYS_BIRTH',
    'DAYS_REGISTRATION',
    'DAYS_ID_PUBLISH',
    'HOUR_APPR_PROCESS_START',
    'DAYS_LAST_PHONE_CHANGE',
    'NAME_CONTRACT_TYPE',
    'CODE_GENDER',
    'FLAG_OWN_CAR',
    'NAME_INCOME_TYPE',
    'NAME_EDUCATION_TYPE',
    'NAME_FAMILY_STATUS',
    'NAME_HOUSING_TYPE',
    'FLAG_EMP_PHONE',
    'FLAG_WORK_PHONE',
    'FLAG_PHONE',
    'REGION_RATING_CLIENT',
    'ORGANIZATION_TYPE',
]

type_dict = {
    'CNT_CHILDREN'       :             'int64',
    'AMT_CREDIT'             :       'float64',
    'AMT_GOODS_PRICE'            :   'float64',
    'REGION_POPULATION_RELATIVE'  :  'float64',
    'DAYS_BIRTH'                :      'int64',
    'DAYS_REGISTRATION'        :     'float64',
    'DAYS_ID_PUBLISH'           :      'int64',
    'HOUR_APPR_PROCESS_START'     :    'int64',
    'DAYS_LAST_PHONE_CHANGE'    :    'float64',
}

for i in val_col:
    if type(uniq[i]) == list:
        temp_dict[i] = st.selectbox(col_dict[i], uniq[i])
        for j in uniq[i]:
            if j == temp_dict[i]:
                str_temp = str(i) + '_' + str(j)
                temp_dict[str_temp] = 1
            else:
                str_temp = str(i) + '_' + str(j)
                temp_dict[str_temp] = 0
        temp_dict.pop(i)
    else:
        if(type_dict[i] == 'int64'):
            temp_dict[i] = st.number_input(col_dict[i], value=0, step=1)
            if i == 'DAYS_BIRTH':
                temp_dict[i] = temp_dict[i] * 365
        else:
            temp_dict[i] = st.number_input(col_dict[i], value=0.0, step=0.1)

@st.cache(allow_output_mutation=True)
def load_model():
    url = 'https://drive.google.com/uc?id=1-HkXELzbwlZ9xR2wP7ePf5vrMkHR1hqg'
    output = 'model.pkl'
    gdown.download(url, output, quiet=True)
    model = pickle.load(open('model.pkl', 'rb'))
    return model
model = load_model()
df_test = pd.DataFrame(temp_dict, columns=temp_dict.keys(), index=[0])
# st.write(temp_dict)

def predict_credit(model, df_test):
    if model.predict(df_test)[0] == 0:
        st.markdown('### Credit is Approved')
    else:
        st.markdown('### Credit is Rejected')

if st.button('Predict'):
    predict_credit(model, df_test)

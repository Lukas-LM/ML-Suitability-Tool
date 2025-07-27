import streamlit as st

st.title("ML-Suitability-Tool")

st.write("The tool enables departments to quickly and accurately assess whether a problem is suitable for Machine Learning.")

st.write("This tool does not provide a binding recommendation, but is used solelyto assess whether a problem could suitable for Machine Learning from the perspective of data structure and goal definition!")
             
            

def evaluate_problem(problem_score, data_size_score, data_structure_score, data_cleaning_score, goal_score):
    # problem_score and goal_score are the most important scores to decide if the problem is for Machine Learning
    # if one of these scores have a scoring of zero points, it is not suitable for a Machine Learning model
    if problem_score == 0 or goal_score == 0:
        return "Your problem is not solvable for Machine Learning: A Machine Learning model needs a measurable goal such as a" \
        " target feature or a grouping task. The result should be a prediction or classification. Also, data is required for training."
    
    total_score = problem_score + data_size_score + data_structure_score + data_cleaning_score + goal_score
    # 65 points is the smallest possible score, because it is the sum of every ask question with the lowest points above zero
    # So if the answer is on every question not the number of the highest and lowest points, we got 65 points
    if total_score < 65:
        return "Your problem is not solvable for Machine Learning: A Machine Learning model needs a measurable goal such as a" \
        " target feature or a grouping task. The result should be a prediction or classification. Also, data is required for training."
    else:
        return "Your problem is solvable for Machine Learning"

# I am asking questions to assess whether a problem is suitable for Machine Learning and create a score based on the answers
options1=["Predicting a number or a class based on given data",
                                     "Sorting data based on similar characteristics",
                                     "Something other"]
# This question aims for the base of Machine Learning, it is a important question, if the answer is "Something other" it could not be
# supervised or unsupervised Learning
# -> predict something is supervised Learning
# -> sorting data is clustering -> unsupervised Learning
problem_type = st.selectbox("What kind of result do you expect from the solution ?",
                            options1)
if problem_type == options1[2]:
        problem_score = 0
elif problem_type == options1[0]:
        problem_score = 20
else:
        problem_score = 10

# This question aims for the suitability for Machine Learning. A Machine Learning model needs data to train, what means, that the 
# dataset needs a minimum of data to provide a good training for the model
# -> less than 1.000 entries are a very low number of entries, if you clean the data you got a very low amount of data
# -> the lower section of this area is the bare minimum. The higher the number of entries, the better is the training
# -> with more than 10.000 entries you got after cleaning a very good amount of data
options2=["Less than 1.000 entries", "Between 1.000 and 10.000 entries", "More than 10.000 entries"]
data_size = st.selectbox("What is the size of your dataset. How many entries does it contain ?", options2)
if data_size == options2[0]:
        data_size_score = 0
elif data_size == options2[1]:
        data_size_score = 10
else:
        data_size_score = 20

# This question aims at the effort.
# -> only numerical features means, that you miss some infos. This increases preprocessing effort, but training is still feasible
# -> categorical and numerical is the best case, you have every important information and a small effort
# -> only categorical is a very high effort. You have to convert every column.
options3=["Only numbers", "Numbers and categorical", "Categorical/pictures"]
data_structure = st.selectbox("What kind of columns has your dataset ?", options3)
if data_structure == options3[0]:
        data_structure_score = 15
elif data_structure == options3[1]:
        data_structure_score = 20
else:
        data_structure_score = 5

# As before this aims for the effort. You have to clean the dataset before using it for the training
# -> with many missing values, it is difficult or impossible for the model to train and a uncleaned data raises the effort
# -> with individual missing values it is possible to train the model. Medium effort to clean the data
# -> with no missing values and a clean dataset, you are very close to start the model instantly
options4=["Many missing values and unclean", "Individual missing values, partially clean", "No missing values and clean data"]
data_cleaning = st.selectbox("How complete and cleaned is the dataset ?", options4)
if data_cleaning == options4[0]:
        data_cleaning_score = 5
elif data_cleaning == options4[1]:
        data_cleaning_score = 10
else:
        data_cleaning_score = 20

# This is also a very important question. You need a target feature with the classes or the number that should be predicted
options5=["Yes", "No"]
goal = st.selectbox("Is there a clear measurable goal ?", options5)
if goal == options5[0]:
        goal_score = 20
else:
        goal_score = 0  

# the button calculate the score and return the evaluation 
if st.button("Evaluate problem"):
    evaluation = evaluate_problem(problem_score, data_size_score, data_structure_score, data_cleaning_score, goal_score)
    st.write(evaluation)

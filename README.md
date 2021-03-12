# Analytics
This Repo is an accumulation of personal study.


## Data Description:
The dataset is from U.S. Bureau of Labor Statistics(BLS), which contains presents data of employment by occupation (2019) and projection of employment for those occupations in 2029. Due to the large number of variables in this dataset, the definition of each variable and its value will be shown in the following list of "Data Variables & Related Values Definitions".

Here is the link of the dataset:

https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm

https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx

## Goal:
Our purpose of exploring this employment data is to find out which factors have the greatest impact on the level of annual median wage, so as to provide some reference for those people who are interested in working in the United States.

For example, some people might want to know what extent the education level will affact the wage? Does the work experience help to improve salary? What are the differences in the impac tof the work experience advantage in terms of wage levels by degree? What are the other secondary factors that affect wages?

## Catergory
HeatMap:Examining the correlation between factors and Median Annual Wages in 2019 of occupations

Main factors

Education: Occupations Entry-level Qualifications (7 levels of education levels）
Work Experience: Minimum number of years of work required （More than 5/ Less than 5/None）
Part 1. Education

For the listed occupations in general, the higher the Entry-level education need, the higher the Median Wage

Education Attribute Composition: Bar Chart

Data Support: Density Plot

Hypothesis testing: one-way ANOVA & Tukey HSD

Part 2. Work Exp

For the listed occupations in general, the higher the threshold of years of Work Experience, the higher the Median Wage

Work Experience Attribute Composition: Pie Chart

Data Support: Bar Plot

Hypothesis testing: Z-test

Part 3. A combination of education and work experience

For the listed occupations in general, Education level and Work Experience combine to influence Median Annual Wages

Data Support: Violin Plot

Hypothesis testing: ANOVA

Part 4. Regression of Median Annual Wages

Quantify all characteristics, find an correlation perdicting model with prediction tool: Random Forest

Conlusion


## Data Variables & Related Values Definitions
2019 National Employment Matrix title and code. Includes most categories of jobs title in the United States as of 2019.

Occupation type: contains the classification of subordinate job categories.

Values: Summary, Line item

Employment 2019 & 2029. The number of employment in each occupation position in 2019 and the number of employment projected by the BLS to be in that position in 2029.

Values: Numerical data

Employment change, number. The numerical change in employment measures the projected number of job gains or losses.

Values: Numerical data

Employment change, percent. The percent change in employment measures the projected rate of change of employment in an occupation. A rapidly growing occupation may indicate favorable prospects for employment.

Values: Numerical data

Median annual wages. (Source: Occupational Employment Statistics (OES) survey) These are data on median annual wages for wage and salary employees in each occupation.

Values: Numerical data

Typical education needed for entry. This category best describes the typical level of education that most workers need to enter the occupation.

Values(8 education levels in descending order):

Doctoral or professional degree. Completion of a doctoral degree (Ph.D.) usually requires at least 3 years of full-time academic work beyond a bachelor's degree.

Master's degree. Completion of this degree usually requires 1 or 2 years of full-time academic study beyond a bachelor's degree.

Bachelor's degree. Completion of this degree generally requires at least 4 years, but not more than 5 years, of full-time academic study beyond high school.

Associate's degree. Completion of this degree usually requires at least 2 years but not more than 4 years of full-time academic study beyond high school.

Postsecondary nondegree award. These programs lead to a certificate or other award, but not a degree. The certificate is awarded by the educational institution and is the result of completing formal postsecondary schooling.

Some college, no degree. This category signifies the achievement of a high school diploma or equivalent plus the completion of one or more postsecondary courses that did not result in a degree or award.

High school diploma or equivalent. This category indicates the completion of high school or an equivalent program resulting in the award of a high school diploma or an equivalent, such as the General Education Development (GED) credential.

No formal educational credential. This category signifies that a formal credential issued by an educational institution, such as a high school diploma or postsecondary certificate, is not typically needed for entry into the occupation.

Work experience in a related occupation. For some occupations, work experience in a related occupation may be a typical method of entry.

Values(3 categories)：

5 years or more. This is assigned to occupations if 5 or more years of work experience in a related occupation is typically needed for entry.

Less than 5 years. To enter occupations in this category, workers typically need less than 5 years of work experience in a related occupation.

None. No work experience in a related occupation is typically needed.

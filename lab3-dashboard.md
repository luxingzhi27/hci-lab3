# lab3-dashboard

## Introduction

I choose the college salaries dataset to complete the data analysis task. Now I’ll introduce the task from the follow two aspects, that is the characteristics of the dataset and our goal of the task.

## characteristics of the dataset

This dataset shows how employment salaries are associated with majors, types of universities, and regions. Of course, it is very meaningful to explore what the change in salary is most related to. It can give you some references to choose your own job. So I decided to show these relationships in three tables.

## goal of the task

The goal of this task is to use three different charts to show the relationship between salary and major types, graduate schools, and geographical regions. Through this task, I can be familiar with the method of displaying data visualization with dash and learn the principles of human-computer interaction’s skill.

## design

### full view

![image-20230522220106184](https://raw.githubusercontent.com/luxingzhi27/picture/main/image-20230522220106184.png)

![image-20230522220150981](https://raw.githubusercontent.com/luxingzhi27/picture/main/image-20230522220150981.png)

![image-20230522220221649](https://raw.githubusercontent.com/luxingzhi27/picture/main/image-20230522220221649.png)

### layout

![image-20230522220346606](https://raw.githubusercontent.com/luxingzhi27/picture/main/image-20230522220346606.png)

1. the main title
2. the drop down box to select the three charts
3. the origin table contents
4. the radio buttons to select salary for different periods
5. the chart

### data analysis

For the three charts, we can select different drop-down boxes to switch. 

- the relationship between salary and major

  In the first chart, I used a histogram to show the average salary of different majors. Through the radio buttons, we can show the relationship between the average salary of different majors and majors from the beginning to the 90th year.

  ![Screenshot_20230522_221247](https://raw.githubusercontent.com/luxingzhi27/picture/main/Screenshot_20230522_221247.png)

  ![Screenshot_20230522_221330](https://raw.githubusercontent.com/luxingzhi27/picture/main/Screenshot_20230522_221330.png)

  We can see that the salaries of all majors are getting higher over time.

- the relationship between salary and college type

  In the second chart, I use a scatter plot to represent the relationship between salary and different types of universities. The abscissa is the starting salary, and the ordinate can change from the starting salary to the salary after 90 years depending on the radio button.

  ![Screenshot_20230522_222031](https://raw.githubusercontent.com/luxingzhi27/picture/main/Screenshot_20230522_222031.png)
  
  ![Screenshot_20230522_222159](https://raw.githubusercontent.com/luxingzhi27/picture/main/Screenshot_20230522_222159.png)
  
  We can see that the types of universities are Engineer and Lvy League, whether it is the starting salary or the salary of the next few decades, the salary is very high, while the salary of the university types is Party, Liberal Arts and States are relatively average.
  
- the relationship between salary and region
  
  In the third chart, I used a box plot to represent the relationship between salary and different regions, and the salary of different periods can be selected through the radio button.
  
  ![Screenshot_20230522_222914](https://raw.githubusercontent.com/luxingzhi27/picture/main/Screenshot_20230522_222914.png)
  
  ![Screenshot_20230522_222958](https://raw.githubusercontent.com/luxingzhi27/picture/main/Screenshot_20230522_222958.png)
  
  We can see that California and the Northeastern have higher salaries than the rest of the region, while Western, Midwestern, and Southern are all similar, with lower salaries than the other two regions.
  
  

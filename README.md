PYTHON: Bayes Theorem

  Algorithm obtains input from the user and uses bayes theorem to calculate statistics for each possible
  subcategory given that the object is from the given category.
  
  Input can be entered in 2 ways:
  First example will be 3 urns (red, blue and green), and in the urns 2 stones (black and white). We will calculate
  the possibility that if you draw a stone it will be black or white depending on which urn you draw from.
    First enter the number of categories - 3
    Enter the number of subcategories - 2
    Enter category name - Red
    Enter category name - Blue
    Enter category name - Green
    Enter subcategory name - Black
    Enter subcategory name - White
    Enter the number of black stones in Red Urn - 20
    Enter the number of white stones in Red urn - 30
    Enter the number of black stones in Blue Urn - 40
    Enter the number of white stones in Blue urn - 50
    Enter the number of black stones in Green Urn - 60
    Enter the number of white stones in Green urn - 70
    
    Results
    --------------Probability Tree----------------
    Probability from Category Red is: 19%
        Probability from subcategory Black is: 40%
        Probability from subcategory White is: 60%
    Probability from Category Blue is: 34%
        Probability from subcategory Black is: 45%
        Probability from subcategory White is: 56%
    Probability from Category Green is: 49%
        Probability from subcategory Black is: 47%
        Probability from subcategory White is: 54%

    -----------------Bayes Theorem-------------------
    Probability subject is from Red given from sub-category Black is: 17%
    Probability subject is from Blue given from sub-category Black is: 34%
    Probability subject is from Green given from sub-category Black is: 50%
    Probability subject is from Red given from sub-category White is: 20%
    Probability subject is from Blue given from sub-category White is: 34%
    Probability subject is from Green given from sub-category White is: 47%
    
  Second example will be probability based on a percentage, we will use if your stock grows given whether
  the economy decreases or increases.
  
    First enter the number of categories - we will use 2
    Now enter number of subcategories - we will also use 2 for this
    Name first category - increases
    Now enter the probability - .75 (this is 75%)
    Name second category - decreases
    Now enter the probability - .25 (this is 25%, notice 75% + 25% = 100%)
    Now enter subcategory name - grows
    Now enter second subcategory name - declines
    Now enter the value of grows in increases - .70 (70% chance your stock grows if economy increases)
    Now enter the value of declines in increases - .30 (30% chance, 70% + 30% = 100%)
    Now enter the value of grows in decreases - .40 (40% chance your stock grows if economy declines)
    Now enter the value of declines in decreases - .60 (60% + 40% = 100%)
    
    Results:
    --------------Probability Tree----------------
    Probability from Category increases is: 75%
        Probability from subcategory grows is: 70%
        Probability from subcategory declines is: 30%
    Probability from Category decreases is: 25%
        Probability from subcategory grows is: 40%
        Probability from subcategory declines is: 60%

    ---------Addition Probability---------------
    Probability of being from increases AND grows: 53%
    Probability of being from increases AND declines: 23%
    Probability of being from decreases AND grows: 10%
    Probability of being from decreases AND declines: 15%

    -----------------Bayes Theorem-------------------
    Probability subject is from increases given from sub-category grows is: 84%
    Probability subject is from decreases given from sub-category grows is: 17%
    Probability subject is from increases given from sub-category declines is: 60%
    Probability subject is from decreases given from sub-category declines is: 40%

import csv

def get_data_list(filename):
    # reading the csv file
    datafile = open(filename, "r") 
    datareader = csv.reader(datafile, delimiter=';')

    # placing the file data in a list
    list_data = []
    for row in datareader:
        list_data.append(row)
    return list_data

# Calculating the monthly average from the list
def get_monthly_average(data):
    # last month in the list
    mth = data[-1][0].split(',')[0].split('/')[0]

    # last year in the data list             
    yr = data[-1][0].split(',')[0].split('/')[2] 

    tmpAvgLst = []          # empty list to store the monthly average temporarily

    num = 0                 # numerator for computing the average
    den = 0                 # denominator for computing the average

    for row in data[1:]:
        strData = row[0] # converting the data in list to string for ease of splitting
        strLst = strData.split(',') # splitting each element in the list by ','
        dateString = strLst[0]      # separating the date from the current row of the list
        month = dateString.split('/')[0] # separating the month from date
        year=dateString.split('/')[2]    # separating the year from date
        vol = float(strLst[6])         # volume in the current row in the list
        adjClose = float((strLst[5]))  #AdjClose in the current row in the list
        volAdjClose = float(vol*adjClose) # Volume and AdjClose multiplied to be used later for computing avg
        
        if mth != month:
            num = volAdjClose
            den = vol         
            mth = month
            yr = year
        else:
            num = num+volAdjClose
            den = den+vol
            avg = num/den
            avg = float(round(avg,2))
            avgLst = [month + '/' + year, avg]
            tmpAvgLst.append(avgLst)

    monthlyAvgLst = [tmpAvgLst[i] for i in range(len(tmpAvgLst)-1) if tmpAvgLst[i][0] != tmpAvgLst[i+1][0]]
    monthlyAvgLst.append(tmpAvgLst[-1])
    return monthlyAvgLst

# reformatting the date in the max average list
def reformat_max_res(highavg):
    rowlist=[]
    max_res_ref = ""    
    for row in highavg: 
        ref = int(row[0].split('/')[0])
        if ref == 1:
           max_res_ref = 'Jan' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 2:
           max_res_ref = 'Feb' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 3:
           max_res_ref = 'Mar' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 4:
           max_res_ref = 'Apr' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 5:
           max_res_ref = 'May' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 6:
           max_res_ref = 'Jun' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 7:
           max_res_ref = 'Jul' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 8:
           max_res_ref = 'Aug' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 9:
           max_res_ref = 'Sep' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 10:
           max_res_ref = 'Oct' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 11:
           max_res_ref = 'Nov' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 12:
           max_res_ref = 'Dec' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])    
        rowlist.append(max_res_ref)
    return rowlist

# reformatting the date in the min average list
def reformat_min_res(lowavg):
    rowlist=[]
    min_res_ref = ""    
    for row in lowavg: 
        ref = int(row[0].split('/')[0])
        if ref == 1:
           min_res_ref = 'Jan' + ' ' + row[0].split('/')[1] + ': ' + str(row[1]) 
        elif ref == 2:
           min_res_ref = 'Feb' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 3:
           min_res_ref = 'Mar' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 4:
           min_res_ref = 'Apr' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 5:
           min_res_ref = 'May' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 6:
           min_res_ref = 'Jun' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 7:
           min_res_ref = 'Jul' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 8:
           min_res_ref = 'Aug' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 9:
           min_res_ref = 'Sep' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 10:
           min_res_ref = 'Oct' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 11:
           min_res_ref = 'Nov' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])            
        elif ref == 12:
           min_res_ref = 'Dec' + ' ' + row[0].split('/')[1] + ': ' + str(row[1])    
        rowlist.append(min_res_ref)

    return rowlist    

def find_six_highest_lowest_monthly_average_price(avgLst):
    # sorting through the 2D list using lambda function
    six_highest_avg = sorted(avgLst, key=lambda x:x[1], reverse=True)[:6]
    six_lowest_avg = sorted(avgLst, key=lambda x:x[1])[:6]

    maxAvg = reformat_max_res(six_highest_avg)
    minAvg = reformat_min_res(six_lowest_avg)

    return maxAvg, minAvg

# printing the final result in this function
def print_info(mthlyAvg):
    print()
    print("Google Stock Prices Between Jan 01, 2016 and Dec 31, 2020\n")
    print("Six Highest Monthly Average Prices:")
    
    for i in find_six_highest_lowest_monthly_average_price(mthlyAvg)[0]: 
            print(i)
    print()
    print("Six Lowest Monthly Average Prices:")

    for i in find_six_highest_lowest_monthly_average_price(mthlyAvg)[1]: 
            print(i)


def main():

    filename = input("Please enter the name of your csv file:" )
    
    print_info(get_monthly_average(get_data_list(filename)))
    

if __name__ == '__main__':
    main()
    

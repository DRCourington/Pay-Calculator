def pay_calc(hours_worked_per_week, hourly_pay, days_per_week):
    
    daily = hourly_pay * (hours_worked_per_week / days_per_week)
    
    daily = round(daily, 2)

    weekly = daily * days_per_week
    
    biweekly = weekly * 2
    
    monthly = biweekly * 2
    
    quarterly = monthly * 3
    
    biannual = quarterly * 2
    
    annual = biannual * 2
    
    print("Calculation complete!\n")

    print("I have generated your daily, weekly, bi-weekly, monthly, quarterly, bi-annual, and annual income.\n")
        
    while True:
        report = input("Would you like to see the whole report?\n")
        
        if report == "Yes" or report == "yes":
            
            print()

            print(f"Your daily pay will be: ${daily}. \n")
            
            print(f"Your weekly pay will be: ${weekly}.\n")
            
            print(f"Your bi-weekly pay will be: ${biweekly}\n")
            
            print(f"Your monthly pay will be: ${monthly}.\n")
            
            print(f"Your quarterly pay will be: ${quarterly}.\n")
            
            print(f"Your bi-annual pay will be: ${biannual}.\n")
            
            print(f"Your annual pay will be: ${annual}.\n")

            break
        
        if report == "No" or report == "no":
            
            report_options = input("What part of the report would you like to see?\n")
            
            if report_options == "daily" or report_options == "Daily":
                
                print(daily)
                
                break
            
            if report_options == "weekly" or report_options == "Weekly":
                
                print(weekly)
                
                break
            
            if report_options == "bi-weekly" or report_options == "Bi-weekly" or report_options == "Bi-Weekly":
                
                print(biweekly)
                
                break
            
            if report_options == "monthly" or report_options == "Monthly":
                
                print(monthly)
                
                break
            
            if report_options == "quarterly" or report_options == "Quarterly":
                
                print(quarterly)
                
                break
            
            if report_options == "bi-annual" or report_options == "Bi-annual" or report_options == "Bi-Annual":
                
                print(biannual)
                
                break
            
            if report_options == "annual" or report_options == "Annual":
                
                print(annual)
                
                break
        
            if report_options == "Quit" or report_options == "quit":
                
                break
        
        else:
            
            print("Please use yes to access the full report, no for specific information, or quit to exit.")
            
            continue

pay_calc(hours_worked_per_week=float(input("How many hours will you work this week?\n")), hourly_pay=float(input("What is your hourly wage?\n$")), 
days_per_week=float(input("How many days per week do you work?\n")))
